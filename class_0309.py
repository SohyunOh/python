# 리스트 :데이터의 목록을 다루는 자료형
# 목차,목록 "나열하다"
# []대괄호로 명명
# 리스트 안애는 어떠한 자료형도 포함될수 있다.

# Ls=[] - 초기화
# Ls=["서울,""경기도"...]
# Ls=["서울,"100,1.111...]
# ls=[10,20,30,40]
# 리스트는 변수를 한줄로 붙인 뒤에 박스 전체의 이름(aa)를 지정
# 각각 aa[0],aa[1], aa[2], aa[3] 과 같이 번호(첨자)를 붙여 사용

# ls=[500,200,300,400]; Sum = 0 
# print("ls:",ls)
# print("ls[0]:",ls[0])
# print("ls[1]:",ls[1])
# print("ls[2]:",ls[2])
# print("ls[3]:",ls[3])
# print()
# print("ls:",ls)
# print("ls[]:",ls[-4])
# print("ls[]:",ls[-3])
# print("ls[]:",ls[-2])
# print("ls[]:",ls[-1])

# 양수는 0~N까지.음수는 -1~-n 까지


# ls=[0,0,0,0]; Sum=0 #[]는 
# ls[0]=int(input("첫번째 숫자 입력:"))
# ls[1]=int(input("두번째 숫자 입력:"))
# ls[2]=int(input("세번째 숫자 입력:"))
# ls[3]=int(input("네번째 숫자 입력:"))

# Sum=ls[0]+ls[1]+ls[2]+ls[3]

# print("ls[0]:",ls[0])
# print("ls[1]:",ls[1])
# print("ls[2]:",ls[2])
# print("ls[3]:",ls[3])

# print("리스트의 합:%d"%Sum)

# ls=[0,0,0,0]; Sum=0 #[]는 
# ls[-4]=int(input("-4번째 숫자 입력:"))
# ls[-3]=int(input("-3번째 숫자 입력:"))
# ls[-2]=int(input("-2번째 숫자 입력:"))
# ls[-1]=int(input("-1번째 숫자 입력:"))

# Sum=ls[-4]+ls[-3]+ls[-2]+ls[-1]

# print("ls[-4]:",ls[-4])
# print("ls[-3]:",ls[-3])
# print("ls[-2]:",ls[-2])
# print("ls[-1]:",ls[-1])

# print("리스트의 합:%d"%Sum)


# ls=[0,0,0,0]; Sum=0
# print("len(ls):",len(ls)) #len 길이 변환 함수
# for i in range(len(ls)):
#     ls[i]=int(input(str(i)+"째 숫자 입력:"))
#     Sum +=ls[i]

# for i in range(len(ls)):
#     print("ls[%d]:" % i,ls[i])
# print("리스트의 합:", Sum)


# ls=[0,0,0,0]
# Sum , i =0,0
# while i<len (ls):
#     ls[i]=int(input(str(i)+" 번째 숫자 입력:"))
#     Sum+=ls[i]
#     i+=1
# else: i=0;
# while i<len (ls):
#     print("ls[%d]"%i,ls[i])
#     i+=1 

# ls=[0,0,0,0]
# Sum=0, i =0,0
# j=0
# while i<len (ls):
#     is[i]=int(input(str(i)+" 번째 숫자 입력:"))
#     Sum+=ls[i]
#     i+=1
# while j<len (ls):
#     print("ls[%d]"%j,ls[i])
#     j+=1


#스라이씽(slicing) 짤라쓰기 

# ls=[10,20,30,40]

# print("ls:",ls)

# print("\nls [1:3]=> ls [1]~[2]:",ls[1:3])
# print("ls [0:3]=> ls [0]~[2]:",ls[0:3])
# print("ls [2:]=> ls [2]~[끝까지]:",ls[2:])
# print("ls [:2]=> ls [0]~[1]:",ls[:2])


# print("\nls [1:3]=> ls [1]~[2]:",ls[-4:-1]) #음수 사용 가능하나 왼쪽부터 대입가능 = -1보다 짝은수로 입력 



#****** 리스트 [얕은 복사]*******
# ls=[10,20,30,40]
# arr = ls
# print("ls :{}ls,id:{}".format(ls,id(ls)))
# print("arr :{}arr,id:{}".format(arr,id(arr)))

# ls=[10,20,30,40]
# arr = ls
# arr[2]=20000
# print("ls :{}ls,id:{}".format(ls,id(ls)))
# print("arr :{}arr,id:{}".format(arr,id(arr)))


#****** 리스트 [깊은 복사]*******

# ls=[10,20,30,40,]
# arr = ls[:] #슬라이씽 처음부터 끝까지 대입
# arr[2]=20000
# print("ls :{}ls,id:{}".format(ls,id(ls)))
# print("arr :{}arr,id:{}".format(arr,id(arr)))


# import copy #키워드 가져오다, 수입하다. / 모튤 
# ls = [10,20,30,40]
# #arr = ls[:]
# arr = copy.deepcopy(ls)
# arr[2] = 'deepc'

# print("ls:{},ls id :{}".format(ls,id(ls)))
# print("arr:{},arr id :{}".format(arr,id(arr)))

# from copy import deepcopy
# # import copy #키워드 가져오다, 수입하다. / 모튤 
# ls = [10,20,30,40]
# #arr = ls[:]
# # arr = copy.deepcopy(ls)
# arr = deepcopy(ls)
# arr[2] = 'deepc'

# print("ls:{},ls id :{}".format(ls,id(ls)))
# print("arr:{},arr id :{}".format(arr,id(arr)))


# ls = [10,20,30]
# arr=[40,50,60]

# print("ls:",ls)
# print("arr:", arr)

# Str=ls+arr
# print("ls+arr => Str:",Str)

# string = ls*3
# print("ls+arr => Str:",string)

####
ls = [10,20,30]
arr=[40,50,60]
Str=[0,0,0]
string = [0,0,0]
for i in range(len(ls)):
    Str[i]=ls[i]+arr[i]
print(Str)
for i in range(len(ls)):
    string[i]=ls[i]*3
print(string)


#선택정렬 
#1.오름차순 낮->높
#2.내림차순 높->낮


# a[i]>a[j]
# a[i]>a[j]
# a[i]a[j]=a[j]a[i]
