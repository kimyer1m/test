Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#3.1
100 > 200
False
100 >= 200
False
100 < 200
True
100 <= 200
True
100 == 200
False
100 != 200
True
200 = 200
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
200 == 200
True
200 != 200
False
True or True
True
True and False
False
True and True
True
True or True and False
True
True and True or False
True
'Morning' < 'morning'
True
'A' > 'B'
False

#3.3
age=int(input("나이를 입력하시오: "))
나이를 입력하시오: 22
height=int(input("키를 입력하시오: "))
키를 입력하시오: 165
if age > 19 and height > 150:
    print("입장할 수 있습니다")

    
입장할 수 있습니다

#3.5
