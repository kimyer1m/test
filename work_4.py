#5.1
list_ex=[10,20,30,40,50,60,70]
high=5
low=3
list_ex[low]
40
list_ex[low+2]
60
list_ex[high-low]
30
list_ex[low-high]
60
list_ex[-1]
70
list_ex[-low]
50
list_ex[2*3]
70
list_ex[2]*3
90
list_ex[5%4]
20
len(list_ex)
7

#5.3
list1=[3, 5, 7]
list2=[2, 3, 4, 5, 6]
for num1 in list1:
    for num2 in list2:
        product=num1*num2
        print(f'{num1}*{num2}={product}')

#5.5
list1=['I like', 'I love']
list2=['pancakes.', 'kiwi juice.', 'espresso.']
for a in list1:
    for b in list2:
        print(a, b)

#5.7
n_list=[10, 20, 30, 50, 60]
total=0
for num in n_list:
    total += num

print("리스트 원소들의 합: ", total)

#5.9
n_list=[10, 20, 30, 50, 60]
max_value=n_list[0]

for num in n_list:
    if num>max_value:
        max_value=num
        
print("가장 큰 값: ", max_value)

#5.11
nums=map(int,input("정수를 다섯 개 입력하시오: ").split())
정수를 다섯 개 입력하시오: 45 67 20 34 2

print("합: ", sum(nums))
print("평균: ", sum(nums)/len(nums)
print("최댓값: ", max(nums))
print("최솟값: ", min(nums))

#5.13
nums=map(int,input("10개의 수를 입력하세요: ").split())
10개의 수를 입력하세요: 45 67 20 34 2 100 23 45 67 89

print("합: ", sum(nums))
print("평균: ", sum(nums)/len(nums))

#5.15
greet='Have a beautiful day.'
greet[0:4]
greet[7:16]
greet[17:20]

#5.17
(1)
animals=['dog', 'cat', 'tiger', 'lion']
print("animals= ", animals)
(2)
animals.append(animals.pop(0))
print(animals)

#5.19
s_list=['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
del s_list[2]
del s_list[5]

print("new_s_list", s_list)

#5.21
src='a2b3c6a2c3f1g1'

for ch in src:
      if ch.is numeric():
          for i in range(int(ch)):
          print(ch_old,end='')
      else:
          ch_old=ch

#5.23
person1=['온달', 20, 1, 100.0, 100.0]
person2=['이사부', 25, 1, 170.0, 70.0]
person3=['평강', 22, 0, 169.0, 60.0]
person4=['혁거세', 40, 1, 150.0, 50.0]

(1)
person_list=person1+person3+person4
n_persons=how_many_persons(person_list)
print(str(n_persons), '명의 정보가 담겨 있습니다.')
(2)
person_list=person1+person3+person4
average_age=compute_average_age(person_list)
print('평균 나이는', str(average_age), '세 입니다.')
(3)
person_list=person1+person2+person3+person4
n_male, n_female=count_males_females(person_list)
print('리스트에는 남자가', n_male, '명, 여자가', n_female, '명 입니다.')
(4)
person_list=person1+person2+person3+person4
display_persons(person_list)

