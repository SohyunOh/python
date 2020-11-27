#변수 (변하는값) <-> 상수
# : 한가지 값으로 고전되지 않고 여러가지 값으로 변할수 있는 공간(메모리)
# ->데이터를 사용하기 위해 메모리에 공간을 할당 받는데 
# 할당 받는 공간에 이름을 정해 두고 원할 떄 꺼내 쓰거나,변경 할 수 있음.
#직접 참조(직접찾아가는 참조) <-> 간접참조(정보를 따른 개체를 이용해서 알아서 찾아가는것,C언어)
#절차지원언어 좌에서 우 ,위에서 아래 로 읽고는 다시 위로 읽지 않음.
# 메모리 할당 예제

# ############################################################################
# ******
# <변수명 작명 규칙>
# *변수의 이름은 알파벳,숫자,언더바(_)로 구성
# *대소문자 구분 #대문자,소문자 는 각각 서로 다른 변수로 인식
# *변수의 이름은 숫자로 시작할 수 없음
# *키워드(예약어)는 변수이름으로 사용 불가능 
# #함수(표준함수-내장함수(ex.print),외장함수(불러오는함수))를 포함한 모든 함수포함.
# *공백이나 특수 기호는 포함될 수 없음 #공백이 있으면 인식을 못함 대신_(언더바)로 이어주기

# *작명 요령
# 1.변수 명은 가급적이면 그 프로그램 내에서 어떤 역할, 어떤 데이터를 담는건지 쉽게 연상 할 수 있게 지어주는 것이 좋다.
#  :나이(age) , 이름(name)
# 2.한글변수 사용 가능 - 가급적이면 한글변수는 사용하지 않는것이 바람직하다.

# *예약어
# *프로그래망 언어중에서 의미가 고정되어 있고,
#  사용자가 작성하는 프로그램 상태에 따라서 의미를 변경 할수 없는 단어
# ############################################################################

# num=100 # =는 대입연산자로 우측에서 좌측으로 대입 /변수는 상수,변수(값),연산수, 함수 만 대입가능
# print("정수 형 변수 사용:%d"%num)
# print("정수 형 변수 사용:",num)
# print("정수 형 변수 사용: num") -변수가 아니게됨.

# num=5
# print("변경전 num:",num)
# num=num+10
# print("변경후 num:",num)

# num1=5;
# num2=10;
# sum_=num1+num2 #sum은 함수로 인식하기에 변수로 인식시킬수있게 변경 _또는 대문자 변경
# print("두 수의 합:",sum_) # 또는 print("두 수의 합:",Sum)

# num1=5
# num2=10
# sum_=num1+num2 
# print("id num1:",id(num1))
# print("id num2:",id(num2))
# print("id sum:",id(sum_))
# print(id(15))
# # id : 메모리에 할당된 주소 함수, 개체가 같은지 다른지 확인 활용
# #C언어 같은 경우는 결과만 남음.

# num1=10
# num2=20
# print("num1(%d)+num2(%d)=%d"%(num1,num2,num1+num2))
# print("num1(",num1,")+num2(",num2,")=",num1+num2)

# # 가감승제
# num1=7 
# num2=5
# sum_=(num1+num2)
# print("num1(%d)+num2(%d)=%d"%(num1,num2,sum_))
# sub=(num1-num2)
# print("num1(%d)-num2(%d)=%d"%(num1,num2,sub))
# mul=(num1*num2)
# print("num1(%d)*num2(%d)=%d"%(num1,num2,mul))
# div=(num1/num2)
# print("num1(%d)/num2(%d)=%f"%(num1,num2,div))


# num1=7
# num2=5
# sum_=(num1+num2)
# sub=(num1-num2)
# mul=(num1*num2)
# div=(num1/num2)
# print("%d+%d=%d"%(num1+num2,sum_))
# print("%d-%d=%d"%(num1-num2,sud))
# print("%d*%d=%d"%(num1*num2,mul))
# print("%d+%d=%f"%(num1+num2,div))

# #파이썬 100점
# num1=100
# print("파이썬%d점"%(num1))
# #나는 27살이다.
# age=27
# print("나는 %d살이다."%(age))
# # 파이썬, C언어,java 3과목의 점수 입력, 합계와 평균 (평균 소수점2자리까지)
# num2=90
# num3=80
# sum_=(num1+num2+num3)
# vud=(sum_/3)
# print("3과목의 합계:%d"%(sum_) )
# print("3과목의 평균:%.2f"%(vud) )

# 파이썬=100
# print("파이썬%d점"%파이썬)
# age=27
# print("나는 %d살이다."%age)
# py=99
# clang=97
# java=88
# sum_=py+clang+java
# avg=sum_/3
# print("총점:%d\n평균:%.2f"%(sum_,avg))


# #당신은 놀이공원을 가기 위해 11개의 지하철역을 지나왔다.
# #출발 역에서 도착역까지 37분이 걸렸다면한역을 지나는데 걸리는 시간은 얼마인가?(수소점 자리까지)
# sta=11
# time=37
# avg=time/sta
# print("한역의 평균시간 : %.2f"%(avg))

# station=11
# time=37
# avg=time/station
# print("한정거장당 걸리는 시간은 %.2f분이다"%avg)

flt=123.567
print("round(flt):",round(flt))
print("round(flt,1)",round(flt,1))
print("round(flt,2):",round(flt,2))
print("round(flt,-1):",round(flt,-1))
#round 합수는 음수를 사용하면 정수도 반올림가능함
#%f는 가공 불가능,표현만그러함 / round 합수는 재가공가능 

# # 호텔 한 층의 높이는 260cm 총 높이14개의 층
# # 1층은 500.23cm라면 이 건물의 높이는 총 몇m인가?
# flo=260
# fas=500.23
# flo13=flo*13
# flo14=flo13+fas
# print("이건물의 높이는:",round(flo14,5),"m이다")

# avg_f1=260
# total=14
# oen_f1=500.23
# total_f1=avg_f1*(total-1)+oen_f1
# print("이건물의 높이는:%.3fmdlek"%(total_f1/100))


# 전동 자전거로 100m 11.27초 1시간 후 몇Km ?(소수점2자리까지)
# 1시간은 3600초 
# vik100=11.27
# hou=3600
# avg=3600/11.27
# print("1시간동안 간 거리는:%.2f "% (avg/10) )

second=60*60 #한시간을 초단위로 환산
ret=second/11.27 # 1시간동안 11027초가 몇번 진행되는지
result=ret*100 #위에 항에서 나온결과는 서이사 아니라 100m 단위로 환산해준다(100m/11.27)
kilo=result/1000 #위에 결과가 m단위로 나온 결과이므로 Km단위로 변환
print("1시간동안 이동할수 있는 거리는",round(kilo,2),"km이다.")




