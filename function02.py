import sys
import os
from my_lib import search_bytes_r, insert_bytes_into_file, remove_bytes_a_to_b

# start of exif
SOE = b"\xFF\xE1\x00\x11\x45\x78\x69\x66\x00\x00\x4D\x4D\x00\x2A\x00\x00\x00\x08"


def function02():
    """
    jpg file header 이후에 데이터 삽입하기.
    (exif format을 추가하여 데이터를 삽입하는 방식)
    """

    file_path = input("파일 경로 입력 >> ")
    data = input("삽입할 데이터(문자열) 입력 >> ")

    try:
        data = SOE + data.encode()

        insert_bytes_into_file(file_path, 20, data)

        print("[+] <기능2> 완료!")
        input("[+] 계속하시려면 엔터를 누르세요")
        return 0

    except FileNotFoundError:
        print("[!] 해당하는 파일이 없습니다.", file=sys.stderr)
        input("[+] 계속하시려면 엔터를 누르세요")
        return -1


def function02_extract_data():
    """
    jpg file header 이후에 삽입된 데이터 출력
    """

    file_path = input("파일 경로 입력 >> ")

    try:
        start_idx = search_bytes_r(file_path, SOE) + len(SOE)
        end_idx = search_bytes_r(file_path, b"\xff\xdb")

        with open(file_path, "rb") as f:
            f.seek(start_idx)
            data = f.read(end_idx - start_idx)
            print("[+] 숨겨진 데이터: ")
            print(data)

        input("[+] 계속하시려면 엔터를 누르세요")
        return 0

    except FileNotFoundError:
        print("[!] 해당하는 파일이 없습니다.", file=sys.stderr)
        input("[+] 계속하시려면 엔터를 누르세요")
        return -1
