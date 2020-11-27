# def sum_func(x1,x2,x3=100):
#     result =0
#     result=x1+x2+x3
#     return result 
# def display ():
#     Sum=0
#     a,b,c =10,20,30
#     Sum=sum_func(a,b)
#     print("매개 변수 2개 호출 : ", Sum)
#     Sum=sum_func(a,b,c)
#     print("매개 변수 2개 호출 : ", Sum)
# display ()

# def alda(day=30,time=8,won=8500):
#     result = day*time*won
#     return result
# def display ():
#     num=int(input('1.기본 급\n2.일한 날짜 입력\n'))
#     if num==1:
#         result =alda()
#     elif num==2:
#         day =int(input('일한 날짜 입력(몇일):'))
#         result= alda(day)
#     print("당신의 급여: {}원 입니다.".format(result))
# display()

# #★★
# def sum_func(*par):
#     result =0 
#     print("type:", type(par))
#     print("par:",par)
#     for num in par:
#         result =result+num
#         print("nim:%d"% num)
#     return result
# Sum=0
# Sum=sum_func(10,20)
# print("매개 변수 2개 호출 : %d"% Sum)
# Sum=sum_func(10,20,30,40)
# print("매개 변수 4개 호출 : %d"% Sum)

# def dic_func(**par):
#     print("type:", type(par))
#     for  k in par.keys():
#         print("{}:{} 명입니다".format(k,par[k]))

# dic_func(똭뚝뽹=123,꿔익꿔익=8, test='테스뚜')       

# def change(a,b,c):
#     return a+10,b+20,c+30

# a,b,c,=change(10,20,30)
# d= change(10,20,30)
# print("a,b,c :", a,b,c )
# print("d:{},type{}".format(d,type(d)))


# def swap(x,y):
#     return y,x

# a=10;b=20
# print("바꾸기전:",a,b)
# a,b= swap(a,b)
# print("바꾼 후:",a,b)



# swap= lambda a,b:[b,a] #람다함수 / : 때문에 [] 리스트나, () 튜플로 묶어줘야함. 
# #/ 자주 사용하지 않으면서 한줄로 표현 할수있는 것들은 lambda함수로 표현
# a= swap(10,20) 
# print("swap 결과",a)
# print(type(a))

# lam= lambda a: a*10
# hap= lambda a,b:a+b
# noData = lambda : print("인자 값 없는 람다")

# print(lam(10))
# print(hap(5,10))
# noData()

# def startGame():
#     print("Game Start!!!")
# def tast():
#     print("1.게임시작")
#     print("2.게임종료")
#     num= input("선택:")
#     if num =="1":
#         startGame()
#     elif num =="2":
#         end()
# end= lambda : print("게임 종료")
# tast()

# 모듈
# 함수나 변수, 클레스 들을 모아 놓은 파일이다
# 파이썬에서는 자주 사용하는 기능들을 표준 모듈로 수성해주어 함께
# 설치하므로 해당 모듈들을 언제든지 불어와 사용할 수 있다.

# 표준 모듈: 이미 설치된 모듈(파이썬에서 정의된 모듈)
# 사용자 모듈 : 개발자(사용자)가 직접 정의한 모듈

# 오ㅣ부모듈을 불러 사용할때 ㅑmport  사용

# import math #가져오다
# import 모듈명 -import a  import ㅘ고 뒤에 이름이 바로 오면 모듈명이다
# 즉 모듈에 저장되있는 함수 전체를 가져다 놓고 작동 시키겠ㄷㅏ 입니다.

# print(math.pi) 
# print(math.factorial(5)) #5!=5x4x3x2x1
# print(math.sqrt(5))
# print(math.log10(2))

# Import 선언은 모듈에 정의된 변수,함수,클래스들 전부 현재 모듈에 불러옴

# from math import factorial,sqrt,pi 
# print(factorial(5))
# print(sqrt(5))
# print(log10(2)) #모듈에 정의되어있지 않기에 함수로 인식

# ----------------------------------------------------------------

# from math import factorial,sqrt,pi  #쓸 함수 지정 
# import math #모듈 전체를 가져옴 .출처 발히기

# print(factorial(5))
# print(sqrt(5))
# print(math.log10(2))
# print(math.log10(3))
# print(math.gcd(12,18))#최대공약수

# # ====================================================================
# import statistics

# points =[65,775,55]
# print('평균:', statistics.mean(points))
# print('분산:', statistics.variance(points))
# print('표준편차:', statistics.stdev(points))
# #---------------------------------------------
# import statistics as st #치환 (알리아스, 리눅스에서 )

# points=[65,75,55]
# print('평균:', st.mean(points))
# print('분산:', st.variance(points))
# print('표준편차:', st.stdev(points))

# 외부모듈은 숫자로 시작하면 에러남. 영문자로 저장하기
# import calculator as cal
# for calculator import info

# print("1dlscl: %2fcm"% cal.inch)
# print("1~10까지의 합 누적 :",cal.calc_sum(10))

# info()
# info()
# info()


# ========랜덤함수=================
# import random
# i=0
# for i in range(5):
#     print(i,"",random.random())

# import random
# i=0
# for i in range(5):
#     print(i,"",int(random.random()*100))


# import random
# i=0
# for i in range(5):
#     print(i,"",random.randrange(1,10)) #1~9까지 의 범위 나오는 범위

#문제 1.Computer 는 램덤하게 가위,바위,보 결정 , 사용자는 가위,바위 보 중 선택하여 승, 패, 무 결과를 출력

# user = input("입력 : "))

# su = random.randrange(1,4)

# if su ==1: com ="가위"
# elif su==2 : com ="바위"
# elif su ==3: com = "보"

# if user == com  :print ("비겼습니다.") 
# elif user = "가위" and com "바위" : print("졌습니다")
# elif user = "가위" and com "보" : print("이겼습니다")
# elif user = "바위" and com "가위" : print("졌습니다")
# elif user = "바위" and com "보" : print("졌습니다")
# elif user = "보" and com "바위" : print("졌습니다")
# elif user = "보" and com "가위" : print("이겼습니다")









# # 풀이====


# import random


# a1 = int (input("가위,바위,보 게임\n 0.가위, 1.바위, 2.보 \n>>>"))








#문제 2. 간단한 로또 프로그램 만드시오 (중복되는 값 체크)
import random

lott =[]

while True:
    su = random.randrange(1,46)
    if lott.count(su) == 0:
        lott.append (su)

    if len (lott) ==6 :
        break
print(lott)

# te=True
# while te :
#     import random
    















