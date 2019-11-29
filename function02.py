import sys
import os
from my_lib import search_bytes_r, insert_bytes_into_file, remove_bytes_a_to_b


def function02():
    """
    jpg file header 이후에 데이터 삽입하기.
    (exif format을 추가하여 데이터를 삽입하는 방식)
    """

    file_path = input("파일 경로 입력 >> ")
    data = input("삽입할 데이터(문자열) 입력 >> ")

    try:
        data = (
            b"\xFF\xE1\x00\x11\x45\x78\x69\x66\x00\x00\x4D\x4D\x00\x2A\x00\x00\x00\x08"
            + data.encode()
        )

        insert_bytes_into_file(file_path, 20, data)

        print("[+] <기능2> 완료!")
        return 0

    except FileNotFoundError:
        print("[!] 해당하는 파일이 없습니다.", file=sys.stderr)
        return -1

    except PermissionError:
        print("[!] Permission denied. 해당 파일이 열려있는지 확인하세요.", file=sys.stderr)
        return -1


def function02_recover():
    """
    jpg file header 이후에 삽입된 데이터 지우기
    exif format 데이터를 제거하는 방식
    """

    file_path = input("복구할 파일 경로 입력 >> ")

    try:
        start_idx = search_bytes_r(file_path, b"\xff\xe1")
        end_idx = search_bytes_r(file_path, b"\xff\xdb") - 1
        remove_bytes_a_to_b(file_path, start_idx, end_idx)

        print("[+] <기능2> 복구 완료!")
        return 0

    except FileNotFoundError:
        print("[!] 해당하는 파일이 없습니다.", file=sys.stderr)
        return -1

    except PermissionError:
        print("[!] Permission denied. 해당 파일이 열려있는지 확인하세요.", file=sys.stderr)
        return -1
