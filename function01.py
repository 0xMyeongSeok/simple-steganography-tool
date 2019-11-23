import sys
import os
from my_lib import search_bytes_r

"""
jpg file의 EOI 뒤에 데이터 삽입하기
"""

def function01():
    
    file_path = input("파일 경로 입력 >> ")
    data = input("삽입할 데이터(문자열) 입력 >> ")

    try:
        idx = search_bytes_r(file_path, b"\xff\xd9") + 2

        with open(file_path, "rb+") as f:
            f.seek(idx, os.SEEK_SET)
            f.write(data.encode())
            print("[+] <기능1> 완료!")
            return 0

    except FileNotFoundError:
        print("[!] 해당하는 파일이 없습니다.", file=sys.stderr)
        return -1


"""
jpg file의 EOI 뒤에 삽입된 데이터 지우기
"""

def function01_recover():

    file_path = input("복구할 파일 경로 입력 >> ")

    try:
        idx = search_bytes_r(file_path, b"\xff\xd9") + 2

        with open(file_path, "rb+") as f:
            f.truncate(idx)
            print("[+] <기능1> 복구 완료!")
            return 0

    except FileNotFoundError:
        print("[!] 해당하는 파일이 없습니다.", file=sys.stderr)
        return -1
