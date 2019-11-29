import time
import os, sys
from my_lib import inject_data_into_bmp


def function03():

    file_path = input("적용할 파일 경로 입력 >> ")
    source_path = input("숨길 데이터 파일 경로 입력 >> ")

    try:
        inject_data_into_bmp(file_path, source_path)

    except FileNotFoundError:
        print("[!] 해당하는 파일이 없습니다.", file=sys.stderr)
        return -1


if __name__ == "__main__":
    function03()
