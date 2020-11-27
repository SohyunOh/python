# flt=13.123
# print("%.3f+%.3f=%.3f"%(flt,321.321,flt+321.321))
# print(flt,"+",321.321,"=",flt+321.321)

# ch1,ch2,ch3="파",'2',"썬"
# print("%c+%c+%c=%s"%(ch1,ch2,ch3,ch1+ch2+ch3))
# print(ch1,"+",ch2,"+",ch3,"=",ch1+ch2+ch3 )

# str_1="python";str_2="test"
# str_3=str_1+str_2
# print("%s+%s=%s"%(str_1,str_2,str_1+str_2))
# print(str_1,"+",str_2,"=",str_1+str_2)

# =========================
# *변수의 자료형 확인
# class int -정수
# class float - 실수형
# class str -문자열
# class bool -블형
# =========================

# A=10
# B=5
# print("type:",type(A<B));print("type:",(A<B))
# num=100;print("type:%s"%type(num))
# flt=321.321;print("type:%s"%type(flt))
# ch="A";print("type:%s"%type(ch))
# st="test";print("type:%s"%type(st))

# num=100
# print("type:%s\tid:%s"%(type(num),id(num)))
# num=321.321
# print("type:%s\tid:%s"%(type(num),id(num)))
# num="A"
# print("type:%s\tid:%s"%(type(num),id(num)))
# num="test"
# print("type:%s\tid:%s"%(type(num),id(num)))


# st1="Python"
# st2=" Test"
# su=100
# flt=1.11

# num="100"

# print(flt+su)
# print(st1+st2)
# #print(su+num)

# su=100

# print('type(su):',type(su))
# print('type(str(su)):',type(str(su)))  #강제 형변환
# print('type(float(su)):',type(float(su)))

#오더에서만 일회성으로 변환

# su=200
# num='100' 
# flt="1.111"

# print(su+int(num))
# print(su+float(flt))
# print(str(su)+num)

# print("숫자 입력")
# num1= input()
# print("입력받은값:",num1)

# print("이름입력")
# mame=input()
# print("나이입력")
# age=input()

# print("이름입력:")
# mame=input()
# print("나이입력:")
# # age=input()
# print("%s님의 나이는 %d살 입니다"%(name,age))


# print("두수의 합을 구해 줍니다")
# print("두 수 입력")

# num1=input()
# num2=input()
# num3= int(num1)+int(num2) 
# print("두 수의 합",num1,"+",num2,"=",num3)

# num1=int(input())
# num2=int(input())

# result=num1+num2
# print(num1,"+",num2,"=",result)

# result=num1-num2
# print(num1,"-",num2,"=",result)

# result=num1*num2
# print(num1,"*",num2,"=",result)

# result=num1/num2
# print(num1,"/",num2,"=",result)

# print("문자열 입력")
# name=input()
# print("정수 입력")
# age=int(input())
# print("실수 입력")
# flt=float(input())

# print("name 값:",name,"\ttype:,",tape(name))
# print("age 값:",age,"\ttype:,",tape(age))
# print("flt 값:",mflt,"\ttype:,",tape(flt))


# name=input("이름을 입력하세요:")
# age=int(inpuut("나이를 입력하세요:"))
# addr=input("주소를 입력하세요:")
# print("이름:",name,"\n나이:",age,"\n주소:",addr)

# name=input("이름을 %d번쨰 입력하세요"% 10)
# name=input("이름을""10번쨰""입력하세요")
# 콤미로 구별되는 순간 에러남. name=input("이름을",10,"번쨰""입력하세요")

# age=int(inpuut("나이를 입력하세요:"))
# addr=input("주소를 입력하세요:")
# print("이름:",name,"\n나이:",age,"\n주소:",addr)

# mame=input("이름을 입력 하세요:")
# age=int(input("나이를 입력 하세요:"))
# addr=input("주소를 입력 하세요")
# print("이름:",name,"\t나이:",age,"\n주소:",addr)

# ye=int(input("올해의 년도를 4자리로 입력하세요?:"))
# br=int(input("당신이 태어난 년도를 4자리로 입력하세요."))
# age=ye-br+1
# print("당신의 나이는 %d 살 입니다"%age)

# ye=int(input("올해의 년도를 4자리로 입력하세요?:"))
# br=int(input("당신이 태어난 년도를 4자리로 입력하세요."))
# print("당신의 나이는 %d 살 입니다"% (ye-br+1))

# print("첫번째 물건의 무게를 입력하시오?:")
# num1=float(input())
# print("두번째 물건의 무게를 입력하시오?:")
# num2=float(input())
# print("현재 엘레베이터에 허용 무게는 %.2f 입니다"%(600-num1-num2))

print=("키를 입력하세요?" )
cm=int(input())

avg_=(cm-100)*0.9
print=("표준체중은%f?"%avg_)


# cm=float(input("키를 입력하세요?"))
# nowkg=float(input("현재 체중을 입력하세요?"))
# pr=(cm-100)*0.9
# bimando=(nowkg/pr)*100
# print("표준체중은 %.2fkg이고 비만도는 %.2f%%이다"%(pr,bimando))

name=input("학생이름:")
k=int(input("국어 점수:"))
e=int(input("영어 점수:"))
m=int(input("수학 점수:"))

sum_=k+e+m
avg=sum_/3

print("국어\t영어\t수학\t합계\t평균\t")
print(name,k,e,m,sum_,avg)



print("국어영어\t수학\t합계\t평균\t")



