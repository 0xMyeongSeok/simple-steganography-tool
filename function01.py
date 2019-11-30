import sys
import os
from my_lib import search_bytes_r


# jpg file의 EOI 뒤에 데이터 삽입하기
def function01():
    
    file_path = input("파일 경로 입력 >> ")
    data = input("삽입할 데이터(문자열) 입력 >> ")

    file_name = os.path.basename(file_path)
    new_file_path = "./new_" + file_name

    try:
        idx = search_bytes_r(file_path, b"\xff\xd9") + 2

        with open(file_path, "rb") as old_file, open(new_file_path, "wb") as new_file:
            new_file.write(old_file.read(idx))
            new_file.write(data.encode())

        print("[+] <기능1> 완료!")
        input("[+] 계속하시려면 엔터를 누르세요")
        return 0

    except FileNotFoundError:
        print("[!] 해당하는 파일이 없습니다.", file=sys.stderr)
        return -1


# 삽입된 데이터 추출
def function01_extract_data():

    file_path = input("파일 경로 입력 >> ")

    try:
        idx = search_bytes_r(file_path, b"\xff\xd9") + 2

        with open(file_path, "rb+") as f:
            f.seek(idx)
            data = f.read()
            print("[+] 숨겨진 데이터: ")
            print(data)
        
        input("[+] 계속하시려면 엔터를 누르세요")
        return 0

    except FileNotFoundError:
        print("[!] 해당하는 파일이 없습니다.", file=sys.stderr)
        return -1
