# Simple-Steganography-Tool
시스템보안 스테가노그래피 팀프로젝트

## 기능
기능은 크게 총 4가지가 있다.
추가적으로 1, 2, 3번 기능은, **스테가노그래피로 숨겨진 텍스트 또는 파일을 출력해주는 부가 기능**을 가지고 있다.

 1. **JPG 파일의 EOI 이후**에 사용자가 입력하는 텍스트 삽입하기
 
3. **JPG 파일의 Header 이후**에 사용자가 입력하는 텍스트 삽입하기
	- Header 이후에 exif를 삽입하여 텍스트를 삽입하였음.
	
 4. **BMP 파일 안에다가 파일 삽입**하기
	 - LSB를 조작하는 방식으로 파일을 삽입하였음.

 5. 두 개의 파일을 입력받아서 서로 상이한 부분을 출력하기
	 - 단순히 두 파일의 index를 서로 비교하면서 다른 값을 출력하는 형식으로 구현하였음.

### 기능3 추가 설명
sample.bmp
![origin](./sample_images/sample.bmp)

cat.bmp
![cat](./sample_images/cat.bmp)

기능 3을 이용하여,
sample.bmp 안에다가 cat.bmp를 숨긴 파일 new_sample.bmp
![result](./sample_images/new_sample.bmp)

원본 이미지 sample.bmp와
기능 3으로 cat.bmp를 숨긴 이미지는 육안으로 차이를 구별할 수 없다.

## 사용법
main.py로 실행시키면 된다.


