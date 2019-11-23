from function01 import function01, function01_recover
from function02 import function02, function02_recover


def print_menu():
    print("""
----------------------------------------------
1) <기능1> JPG 파일의 EOI 이후에 data 삽입하기
2) 기능1 적용된 파일 복구하기
3) <기능2> JPG 파일의 헤더 이후에 data 삽입하기
4) 기능2 적용된 파일 복구하기
----------------------------------------------""")

if __name__ == "__main__" :
    
    while(True):
        print_menu()
        try:
            choice = int(input("원하시는 기능의 번호를 입력하세요: "))
            if choice not in [1,2,3,4]:
                raise ValueError

            if choice == 1:
                function01()
            
            elif choice == 2:
                function01_recover()

            elif choice == 3:
                function02()
            
            elif choice == 4:
                function02_recover()
        
        except ValueError:
            print("[!] 올바른 번호를 입력하세요..")

        

    