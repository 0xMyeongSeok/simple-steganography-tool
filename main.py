from function01 import function01, function01_recover
from function02 import function02, function02_recover
from function04 import function04


def print_menu():
    print("""
----------------------------------------------
1) <기능1> JPG 파일의 EOI 이후에 data 삽입하기
2) 기능1에 의해 숨겨진 데이터 추출하기
3) <기능2> JPG 파일의 헤더 이후에 data 삽입하기
4) 기능2에 의해 숨겨진 데이터 추출하기
5) <기능3> BMP 파일에 데이터 숨기기 (LSB steganography)
6) 기능3에 의해 숨겨진 데이터 추출하기
7) <기능4> 두 파일에서 다른 부분 구하기
0) 종료
----------------------------------------------""")

if __name__ == "__main__" :
    
    while(True):
        print_menu()
        try:
            choice = int(input("원하시는 기능의 번호를 입력하세요: "))
            if choice not in [1,2,3,4,5,6,7,0]:
                raise ValueError

            if choice == 1:
                function01()
            
            elif choice == 2:
                function01_recover()

            elif choice == 3:
                function02()
            
            elif choice == 4:
                function02_recover()

            elif choice == 5:
                pass

            elif choice == 6:
                function04()
            
            elif choice == 7:
                pass

            elif choice == 0:
                break
        
        except ValueError:
            print("[!] 올바른 번호를 입력하세요..")

        

    