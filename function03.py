import time
import os, sys
from my_lib import inject_data_into_bmp


def function03():
    """
    파일의 LSB를 조작하여 데이터 숨기기
    """

    file_path = input("파일 경로 입력 >> ")
    source_path = input("숨길 데이터 파일 경로 입력 >> ")

    try:
        inject_data_into_bmp(file_path, source_path)
        input("[+] 계속하시려면 엔터를 누르세요")

    except FileNotFoundError:
        print("[!] 해당하는 파일이 없습니다.", file=sys.stderr)
        input("[+] 계속하시려면 엔터를 누르세요")
        return -1


def function03_extract_data():
    """
    기능3에 의해 삽입된 데이터 추출
    """
    file_path = input("파일 경로 입력 >> ")
    extract_file_path = "./extract.data"

    try:
        old_file = open(file_path, "rb")
        new_file = open(extract_file_path, "wb")

    except FileNotFoundError:
        print("[!] 해당하는 파일이 없습니다.", file=sys.stderr)
        input("[+] 계속하시려면 엔터를 누르세요")
        return -1

    old_file.seek(54)
    # Read injected file size
    data_size = 0
    for i in range(0, 64):
        if (ord(old_file.read(1)) & 0x01) > 0:
            data_size |= 1 << (63 - i)

    # Read injected file data
    for i in range(0, data_size):
        value = 0
        for j in range(0, 8):
            if (ord(old_file.read(1)) & 0x01) > 0:
                value |= 1 << (7 - j)

        byte = chr(value).encode()
        new_file.write(byte)

    old_file.close()
    new_file.close()

    print("[+] 숨겨진 데이터가 정상적으로 추출되었습니다.")
    print("위치 : {}".format(os.path.realpath(extract_file_path)))
    input("[+] 계속하시려면 엔터를 누르세요")
