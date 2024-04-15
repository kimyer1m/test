#9.1
(1)
(123).__add__(334)
(2)
(123).__sub__(334)
(3)
(123).__mul__(334)
(4)
(123).__truediv__(3)

#9.3
pop() 사용 불가능
sort() 사용 불가능
append() 사용 불가능
upper() 사용 가능
insert() 사용 불가능
remove() 사용 불가능

#9.5
a=1       
b=1       
c=2       
d=3       
e=3

if a is b:
    print('a와 b는 같은 객체인가? True')
else:
    print('a와 b는 같은 객체인가? False')
if b is c:
    print('b와 c는 같은 객체인가? True')
else:
    print('b와 c는 같은 객체인가? False')
if c is d:
    print('c와 d는 같은 객체인가? True')
else:
    print('c와 d는 같은 객체인가? False')
if d is e:
    print('d와 e는 같은 객체인가? True')
else:
    print('d와 e는 같은 객체인가? False')

#9.7
class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return 'Dog('+self.name+', '+self.age+')'
    
my_dog=Dog('이름은 Mango', '나이는 3살')
print(my_dog)

#9.9
class Counter:
    def __init__(self, number=0):
        if number >= 100 or number <= -1:
            self.__number=0
        else:
            self.__number=number
    def reset(self):
        self.__number=0
    def inc(self):
        self.__number=(self.__number+1) if self.__number<100 else 0
    def dec(self):
        self.__numer=(self.__number-1) if self.__number>0 else 0
    def __str__(self):
        return f'C({self.__number})'
    def __add__(self, other):
        if isinstance(other, Counter):
            return Counter(self.__number+other.__number)
        return NotImplemented
    def __sub__(self, other):
        if isinstance(other, Counter):
            return Counter(self.__number-other.__number)
        else:
            return NotImplemented

c1=Counter(10)
c2=Counter(20)
c3=c1+c2
c4=c1-c2
print('c3=', c3)
print('c4=', c4)

#9.11
name=input('학생의 이름을 입력하세요: ')
student_id=input('학생의 학번을 입력하세요: ')

student=Student(name, student_id)

korean_quiz=int(input('학생의 국어 성적을 입력하세요: '))
math_quiz=int(input('학생의 수학 성적을 입력하세요: '))
science_quiz=int(input('학생의 과학 성적을 입력하세요: '))

class Student:
    def __init__(self, name, student_id):
        self.name=name
        self.student_id=student_id
        self.__korean_quiz=0
        self.__math_quiz=0
        self.__science_quiz=0
        self.__total_score=0
    def set_name(self, name):
        self.name=name
    def get_name(self):
        return self.name
    def set_student_id(self, student_id):
        return self.student_id
    def get_student_id(self):
        return self.student_id
    def set_korean_quiz(self, score):
        self.__korean_quiz=score
    def get_korean_quiz(self):
        return self.__korean_quiz
    def set_math_quiz(self, score):
        self.__math_quiz=score
    def get_math_quiz(self):
        return self.__math_quiz
    def set_science_quiz(self, score):
        self.__science_quiz=score
    def get_science_quiz(self):
        return self.__science_quiz
    def calculate_total_score(self):
        self.__total_score=self.__korean_quiz+self.__math+quiz+self.__science_quiz
    def get_total_score(self):
        return self.__total_score

student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)
print(student)

#9.13
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def contains(self, other):
        return (self.x <= other.x and
                self.y <= other.y and
                self.x+self.w >= other.x+other.w and
                self.y+self.h >= other.y+other.h)
    def overlaps(self, other):
        return (self.x < other.x+other.w and
                self.x+self.w > other.x and
                self.y < other.y+other.h and
                self.y+self.h>other.y)
    def area(self):
        return self.w*self.h
    def __str__(self):
        return f"Rectangle: (x={self.x}, y={self.y}, w={self.w}, h={self.h}), 면적: {self.area()}"

r1=Rectangle(0, 0, 100, 100)
r2=Rectangle(0, -10, 10, 10)
r3=Rectangle(-100, 0, 120, 100)

print('r1=', r1)
print('r2=', r2)
print('r3=', r3)

print('r1 contains r2: ', r1.contains(r2))
print('r1 contains r3: ', r1.contains(r3))
print('r1 contains r2: ', r1.overlaps(r2))
print('r1 contains r3: ', r1.overlaps(r3))
