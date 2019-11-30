import os
import struct
import subprocess
import sys


if sys.platform.startswith("win"):
    def clear_screen():
        subprocess.call(["cmd.exe", "/C", "cls"])
else:
    def clear_screen():
        subprocess.call(["clear"])


def search_bytes_r(file_path, marker, buffer_size=1024):
    """ 
    Search specific bytes(marker) from the end of a file, 
    and then, return start offset of the bytes. 
 
    Arguments: 
        file_path {file} 
        marker {bytes} -- specific bytes to find. e.g. b'\\xff\\xd9' 
     
    Keyword Arguments: 
        buffer_size {int} -- (default: {1024}) 
 
    Returns: 
        int -- if found, return start offset of the bytes. else, return -1. 
    """

    with open(file_path, "rb") as f:
        f.seek(0, os.SEEK_END)  # 파일의 끝에서부터 탐색
        remaining_size = file_size = f.tell()
        offset = 0

        while remaining_size > 0:
            offset = min(file_size, offset + buffer_size)
            f.seek(-offset, os.SEEK_END)
            # 버퍼에 데이터 저장 및 탐색
            buffer = f.read(min(remaining_size, buffer_size))
            remaining_size -= buffer_size
            idx = buffer.find(marker)
            # marker를 못찾았다면,
            # 버퍼 크기에 따라 marker가 잘리는 경우도 있으므로 확인해야 함
            if idx == -1:
                offset = offset + len(marker) - 1
                if offset < file_size:
                    f.seek(-offset, os.SEEK_END)
                    buffer = f.read(len(marker) * 2 - 2)
                    idx = buffer.find(marker)

            # marker를 찾았다면 위치 offset 반환
            if idx != -1:
                return file_size - offset + idx

        return -1


def insert_bytes_into_file(file_path, idx, data):
    """
    Create a new file with data inserted
    
    Arguments:
        file_path {file}
        idx {int} -- index into which data will be insert
        data {bytes} -- data you want to insert
    """

    file_name = os.path.basename(file_path)
    new_file_path = "./new_" + file_name

    with open(file_path, "rb") as old_file, open(new_file_path, "wb") as new_file:
        new_file.write(old_file.read(idx))
        new_file.write(data)
        new_file.write(old_file.read())


def remove_bytes_a_to_b(file_path, start, end):
    """
    Create a new file with data removed start_index to end_index
    
    Arguments:
        file_path {[type]} -- [description]
        start {[type]} -- [description]
        end {[type]} -- [description]
    """

    file_name = os.path.basename(file_path)
    new_file_path = "./recover_" + file_name

    with open(file_path, "rb") as old_file, open(new_file_path, "wb") as new_file:
        new_file.write(old_file.read(start))
        old_file.seek(end + 1, os.SEEK_SET)
        new_file.write(old_file.read())


def search_longest_repeated_byte(data):
    """
    Search longest_repeated_byte
    e.g. search_longest_repeated_byte(b"aabbbbccd") returns 2, 4
    
    Arguments:
        data {bytes}
    
    Returns:
        int -- return the index of longest repeated byte, and the length of it.
    """

    target = temp = data[0]
    target_idx = temp_idx = 0
    target_len = temp_len = 1

    for idx, byte in enumerate(data[1:], start=1):
        if temp == byte:
            temp_len += 1

        else:
            if temp_len > target_len:
                target = temp
                target_idx = temp_idx
                target_len = temp_len

            temp = byte
            temp_idx = idx
            temp_len = 1

    if temp_len > target_len:
        target = temp
        target_idx = temp_idx
        target_len = temp_len

    return target_idx, target_len



# References:
# https://github.com/BrankoMalbasic/bitmap-steganography/blob/master/Bitmap%20Steganography/Steganography.cs
def inject_data_into_bmp(target_path, source_path):
    """
    source 데이터를 target(.bmp)에다가 삽입한다.
    LSB를 이용한 스테가노그래피 기법 사용.
    """

    target_size = os.path.getsize(target_path)
    source_size = os.path.getsize(source_path)

    # target file에 source data가 들어가는지 검증
    # 54byte: bmp header, 64byte: file length
    if target_size < source_size * 8 + (54 + 64):
        print("[!] 숨길 데이터 크기가 원본 크기보다 큽니다.")
        return -1

    target_file = open(target_path, "rb")
    source_file = open(source_path, "rb")
    output_file = open("./new_{}".format(os.path.basename(target_path)), "wb")

    # write bmp header
    output_file.write(target_file.read(54))

    print("writing bmp header complete...")

    # write source size (by using LSB steganography)
    for i in range(0, 64):
        if (source_size & (1 << (63 - i))) > 0:
            output_file.write(struct.pack("B", ord(target_file.read(1)) | 0x01))

        else:
            output_file.write(struct.pack("B", ord(target_file.read(1)) & 0xFE))

    print("source size injection complete...")

    # write source data (by using LSB steganography)
    for i in range(0, source_size):
        byte = source_file.read(1)
        for j in range(0, 8):
            if (ord(byte) & (1 << (7 - j))) > 0:
                output_file.write(struct.pack("B", ord(target_file.read(1)) | 0x01))

            else:
                output_file.write(struct.pack("B", ord(target_file.read(1)) & 0xFE))

    print("source data injection complete...")

    # write remaining bytes
    output_file.write(target_file.read())

    target_file.close()
    source_file.close()
    output_file.close()

    print(
        "[+] All completed. {} created".format("new_" + os.path.basename(target_path))
    )

    return 0


if __name__ == "__main__":
    inject_data_into_bmp("./dog.bmp", "./source")
    