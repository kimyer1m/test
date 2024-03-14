Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#2.1
print(100,'+',200,'=',100+200)
100 + 200 = 300
print(200,'+',300,'+',400,'=',200+300+400)
200 + 300 + 400 = 900

#2.3
width=30
height=60
print(width*height)
SyntaxError: multiple statements found while compiling a single statement

#2.3
width=30
height=60
print(width*height)
1800

#2.5
a=int(input("정사각형의 밑변을 입력하시오: "))
정사각형의 밑변을 입력하시오: 40
print(a**2)
1600

#2.7
a=(1*2*3*4*5*6*7*8*9)
print("10!=3628800")
10!=3628800

#2.9
txt1='섭씨\n0\n10\n20\n30\n40\n50'
txt2='화씨\n32.0\n50.0\n68.0\n86.0\n104.0\n122.0'
print(txt1), (txt2)
섭씨
0
10
20
30
40
50
(None, '화씨\n32.0\n50.0\n68.0\n86.0\n104.0\n122.0')

#2.11
int(input("화씨 온도를 입력하세요: "))
화씨 온도를 입력하세요: 86
86
int(input("화씨 온도를 입력하세요: "))86
SyntaxError: invalid syntax

#2.11
a=int(input("화씨 온도를 입력하세요: "))
화씨 온도를 입력하세요: 86
print(a*(9/5)+32)
186.8
print(a/(9/5)+32)
79.77777777777777
print(a/(9/5)-32)
15.777777777777779
print(a/(5/9)-32)
122.79999999999998
print(a/(9*5)-32)
-30.08888888888889
print(-(a/(9*5)-32))
30.08888888888889

#2.11
a=int(input("화씨 온도를 입력하세요: "))
화씨 온도를 입력하세요: 86
n=-(a/(9*5)-32)
print("화씨 a도는 섭씨 n도 입니다.")
화씨 a도는 섭씨 n도 입니다.

#2.11
a=int(input("화씨 온도를 입력하세요: "))
화씨 온도를 입력하세요: 86
print(-(a/(9*5)-32))
30.08888888888889

#2.13
PI=3.141592
a=int(input("원의 반지름을 입력하세요: "))
원의 반지름을 입력하세요: 11
print("원의 둘레",  2.0*PI*a, "원의 면적", PI*a*a)
원의 둘레 69.115024 원의 면적 380.13263200000006

#2.15
a=int(input("밑변을 정수로 입력하세요: "))
밑변을 정수로 입력하세요: 3
b=int(input("높이를 정수로 입력하세요: "))
높이를 정수로 입력하세요: 4
print((a**2+b**2)**0.5)
5.0
