import binascii
import sys
import os


def function04():
    file1_path = input("파일 1 경로 입력 >> ")
    file2_path = input("파일 2 경로 입력 >> ")

    try:
        myFile1 = open(file1_path, mode="rb")
        myFile2 = open(file2_path, mode="rb")
        string1 = myFile1.read()
        string2 = myFile2.read()

        len1 = len(string1)
        len2 = len(string2)
        base = 0

        if len1 > len2:
            base = len1
            for pos in range(0, len1 - len2):
                string2 += b"@"
            print("경고! 파일 1의 크기가 더 크므로 파일 2를 @으로 패딩했습니다")

        elif len1 < len2:
            base = len2
            for pos in range(0, len2 - len1):
                string1 += b"@"
            print("경고! 파일 2의 크기가 더 크므로 파일 1을 @으로 패딩했습니다")
        elif len1 == len2:
            base = len1

        for pos in range(0, base):
            if string1[pos] == string2[pos]:
                continue
            elif string1[pos] != string2[pos]:
                print(
                    "인덱스 :",
                    pos,
                    ", 파일1 내용 :",
                    chr(string1[pos]),
                    ", 파일2 내용 :",
                    chr(string2[pos]),
                )

        print("비교 끝")
        myFile1.close()
        myFile2.close()
        input("[+] 계속하시려면 엔터를 누르세요")
        return 0

    except FileNotFoundError:
        print("[!] 해당하는 파일이 없습니다.", file=sys.stderr)
        input("[+] 계속하시려면 엔터를 누르세요")
        return -1
