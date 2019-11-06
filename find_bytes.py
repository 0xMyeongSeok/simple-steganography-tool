import os


def find_bytes(file_path, sig, buffer_size=1024):
    """Function that find specific bytes, and then return offset.

    Arguments:
        file_path {file}
        sig {bytes} -- specific bytes to find.
    
    Keyword Arguments:
        buffer_size {int} -- (default: {1024})

    Returns:
        int -- if found, return start offset of bytes. else, return -1.
    """
    
    with open(file_path, "rb") as f:
        f.seek(0, os.SEEK_END)  # 파일의 끝에서부터 탐색
        remaining_size = file_size = f.tell()
        offset = 0

        while(remaining_size > 0):
            offset = min(file_size, offset + buffer_size)
            f.seek(-offset, os.SEEK_END)
            # 버퍼에 데이터 저장 및 탐색
            buffer = f.read(min(remaining_size, buffer_size))
            remaining_size -= buffer_size
            idx = buffer.find(sig)
            # sig를 찾았다면 위치 offset 반환
            if(idx != -1):
                return file_size - offset + idx

        return -1


if __name__ == "__main__":            
    print(find_bytes("./test.jpg", b"\xff\xd9"))