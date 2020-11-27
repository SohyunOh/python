# print("키:")
# cm=int(input())
# print("몸무게:")
# kg=int(input())
# print("평균:")
# avg_=int(input((cm-100)*0.9))

# 산술연산자 
# =   a=b     대입 연산자 (우측에서 좌측) #함수,복합연산식,산술연산자,논리연산자등 우측항에 대입가능
# +   a+b     더하기
# -   a-b     빼기
# *   a*b     곱하기
# /   a/b     나누기
# //  a//b    나누기(몫)  #몫값만 나눠줌
# %   a%b     나머지 값
# **  a**b    제곱 #거듭제곱 

# num1 =9; num2=2
# print(num1,"+",num2,"=",num1+num2)
# print(num1,"-",num2,"=",num1-num2)
# print(num1,"*",num2,"=",num1*num2)
# print(num1,"/",num2,"=",num1/num2)
# print(num1,"//",num2,"=",num1//num2)
# print(num1,"%",num2,"=",num1%num2)
# print(num1,"**",num2,"=",num1**num2)

# 관계연산자 #조건을 만목하면 참거짓 (True, False)
# 관계연산자  사용 예       의미
# <           a<b       a가b보다 작다 #미만
# >           a>b       a가b보다 크다 #초과
# <=          a<=b      a가b보다 작거나 같다 #이하
# >=          >=        a가b보다 크거나 같다 #이상,
# ==          ==        a와b와 같다. 
# !=          !=        a가b 와 같지 않다

# su1=3.1; su2=3
# print("su1 >= su:",(su1>=su2))
# print("su1 <= su:",(su1<=su2))
# print("su1 == su:",(su1==su2))
# print("su1 != su:",(su1!=su2))

# # 서식제어문 : 참이면 1, 거짓이면0
# su1=3.1; su2=3
# print("su1 >= su:%d"%(su1>=su2))
# print("su1 <= su:%s"%(su1<=su2))
# print("su1 == su:%c"%(su1==su2))
# print("su1 != su:%f"%(su1!=su2))



# #0을 모든 숫자는 참값, 0은 거짓

# 복합 대입연산자 b는 상수나 변수등 데이터, a는 변수
# +=  a+b      a=a+b
# -=   a-=b      a=a-b
# *=   a*=b      a=a*b
# /=   a/=b      a/=a/b
# %=   a%=b      a=a%b
# **=   a**=b      a=a**b

# su1=su2=5
# su1+=1
# print("su1+1=",su1)
# su1-=1
# print("su1-1=",su1)
# su1*=su2
# print("su1*su2=",su1)
# su1//=su2
# print("su1//su2=",su1)
# su1%=su2
# print("su1%su2=",su1)

# su1=5
# su2=3
# su1**=su2
# su1-=2
# print("su1/4=",su1/4)
# print("su1//4=",su1//4)
# print("su1%4=",su1%4)

# 논리연산자등 #좌측부터 연산
# and     (a>b) and (a<c) #좌측이 거짓이면 우측은 해석하지 않음
# or         (a>b) and (a<c)
# not     not(a==b) #결과 부정

# print(0 or 0,":",False or False)
# print(1 or 0,":",True or False)
# print(0 or 1,":",False or True)
# print(1 or 1,":",True or True)
# print("not:",not(0 or 0), ":",not (False or False)
# print("not:",not(1 or 1), ":",not (True or True)


# a=20
# b=10
# print(0 or 0, ":", False or (a+b))  #논리연산자는 정수를 만나면 정수출력
# print(1 or 0, ":", True or (a+b))
# print(0 and 0, ":", False or (a+b))
# print(1 and 0, ":", True or (a+b))

# 비트연산자

# num1 =3
# num2=5
# result=num1|num2
# print(result)

# num1 =3
# num2=5
# result=num1&num2
# print(result)

num1 =3
num2=5
result=num1^num2
print(result)

# num1 =5
# ret=num1<<2
# print(ret)

# num1 =5
# ret=num1>>6
# print(ret)

# num1=10
# num2=5
# if num1 > num2:
#     print("num1 이 num2보다 크다")

# num1=10
# num2=5
# if num1 > num1:
#     print("num1 이 num2보다 크다")  #실행은됨

# num1=int(input("수 입력:"))
# if num1%2 == 0:
#     print("num1:",num1,"짝수다")
# print("나는 다음 문장")

# num1=int(input("수 입력:"))
# if num1%2 == 0:
#     print("num1:",num1,"짝수다")
#     print("num1:",num1,"2의 배수이다")
# print("나는 다음 문장")

# print("1.easy game")
# print("2.hard game")
# print("3.exit")
# num1=int(input("선택:"))
# if num1 ==1:
#     print("easy game start")
# if num1 ==2:
#     print("hard game start")
# if num1 ==3:
#     print("game exit")

# num1=int(input("날짜입력:"))
# if num1 %7== 1:
#     print("월요일이다.")
# if num1 %7== 2:
#     print("화요일이다.")
# if num1 %7== 3:
#     print("수요일이다.")
# if num1 %7== 4:
#     print("목요일이다.")
# if num1 %7== 5:
#     print("금요일이다.")
# if num1 %7== 6:
#     print("토요일이다.")
# if num1 %7== 0: #나머지가 7이 나올수 없기에 7이 난 0으로 표기
#     print("일요일이다.") 

# print("입력한 데이터가 3의 배수인 경우 출력")
# num1=int(input("데이터 입력:"))
# if num1 %3 == 0: 
#     print(num1,"은 3의 배수이다")

# print("절대값을 구하는 프로그램 작성")
# num2=int(input("데이터 입력:"))
# if num2 >= 0 : print(num2)
# if num2 < 0 : print(-num2)

# print("수를 입력받아 짝,홀수를 구분하여 출력하시오")
# num3=int(input("수 입력:"))
# if num3 %2 == 0: 
#     print("짝수")
# if num3 %2 == 1: 
#     print("홀수")

# print("두 수를 입력받아 큰수를 출력하시오")
# su1 =int(input("1수 입력:"))
# su2 =int(input("2수 입력:"))
# if su1 > su2 : print(su1) 
# if su1 < su2 : print(su2)

# print("세 수를 입력받아 큰수 출력")
# su1=int(input("입력"))
# su2=int(input("입력"))
# su3=int(input("입력")) 
# if su1<su2:
#     if su2<su3:
#       print(su3)
# if su1<su3:
#     if su3<su2:
#          print(su2)
# if su2<su1:
#     if su1<su3:
#       print(su3)
# if su2<su3:
#     if su3<su1:
#       print(su1)
# if su3<su2:
#     if su2<su1:
#       print(su1)
# if su3<su1:
#     if su1<su2: 
#       print(su2)



# print("두수를 입력받아 큰수가 짝수이면 출력")
# su1 = int(input("입력:"))
# su2 = int(input("입력:"))
# if su1 > su2 :
#      if su1 %2 == 0:
#       print(su1)
# if su1 < su2 :
#     if su2 %2 == 0:
#       print(su2)

# print("두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력")
# su1 = int(input("1.입력:"))
# su2 = int(input("2.입력:"))
# if (su1+su2) %2 == 0 :
#     if (su1+su2) %3 == 0 :
#         print((su1+su2),"는 짝수이며 3의 배수이다")



