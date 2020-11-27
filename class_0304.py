# name = input("이름 입력:")
# hak = input("학번 입력:")
# kor = int(input("국어 점수:"))
# eng = int(input("영어 점수:"))
# math = int(input("수학 점수:"))
# sum_= kor+eng+math
# avg= sum_/3
# if avg >= 90: level ='A'
# elif avg >= 80: level ='B'
# elif avg >= 70: level = 'C'
# elif avg >=60: level = 'D' 
# else: level='F'
# print("==================학생정보===========================")
# print("이름\t학번\t국어\t영어\t수학\t총합\t평균\t학점")
# print("%s\t%s\t%d\t%d\t%d\t%d\t%.2f\t%s"%(name,hak,kor,eng,math,sum_,avg,level))


# cof=int(input("주문할 커피 수량 입력:"))
# cof1= cof*2000
# cof2= cof1 - ((cof-10)*500)
# if cof > 10 :
#     print ("%d원"% cof2)
# else :
#     print ("%d원"% cof1)

# num=int(input("주문할 커피 수량 입력:"))
# if num > 10 :
#     money=20000 + (num-10)*1500
# else :
#     money=2000*num
# print ("주문한 커피의 금액 : %d원"% money)


# num=int(input("임의의 정수 입력:"))
# if num == 0: print("0은 3의 배수도 4의 배수도 아닙니다")
# elif num%3==0 and num%4 == 0: print("3배수이면서 4의 배수입니다")
# elif num %3 == 0: print("3배수 입니다")
# elif num %4 == 0: print("4배수 입니다")
# else: print("3의 배수도 4의 배수도 아닙니다")

# money=30000
# time=int(input("비행기 탑승 시간:"))
# time-=30
# if time >0 :
#     if time%10==0 :
#         money=money+time//10*5000
#     else:
#         money=money+time//10*5000+5000
# print("비행기 탑승 요금 : %d"%money)
    
 
# money=30000
# time=int(input("비행기 탑승 시간:"))
# time-=30
# if time > 0 :
#      money=money+(5000+((time-1)//10)*5000)
# print("비행기 탑승 요금 :%d원"%money)

#========================조건문 END=========================================

#========================반복문 (제어문)=================================
# for i in range(1,11,1):
# #  for (i=1;i<11;i=i+1) #C언어식 표현 조건절
#     print(i)

# print('다음문장')

# for i in range(1,11,1):
#     print("상준쌤 짱") # 필요에 따라 어미값을 얼만큼 반복할지 활용할수 있음.

# print('다음문장') 

# for i in range(0,3,1,):
#     print("i:",i,"for문 이해하기^^")

# print('다음 문장들 실행')


# for i in range(1,11,1):
#     if i %2==0:
#         print("i=",i,":값 확인")  # 반복 10번

# print("다음문장")


# for i in range(0,11,2):
#     print("i=",i,":값 확인") #반복 6번 

# print("다음문장")

# for i in range(10,-1,-1):
# #for (i=10,i>-1;i-=1)#C언어식 표현 조건절
#     print(i,":10~0까지 출력") 

# sum_=0
# for i in range(1,11,1):
#     sum_+=i
# print(sum_) 

# for i in range(1,11,1):
#     print(i,end="") #\n,\t 생략


# for i in range(1,11,1):
#     print(i,end=" ") #\n,\t 생략 
#     #TypeError: end must be None or a string, not int - 끝에는 정수,실수 즉 실수는 안됨.

# for i in range(1,31,1):
#     print(i,end= "\t")
#     if i%5==0 :
#         print()

# print()
# for i in range(1,31,1):
#     print(i,end= "\t")
#     if i%5==0 :
#         print("\n")

# i, sum =0,0
# num=0
# num=int(input("값 입력:"))
# for i in range(1, num+1,1):
#     sum=sum+i
# print("1에서 %d까지의 합:%d"% (num,sum))


# for i in range(0,10): #증강값 양수1 생략 가능
#     print(i)

# for i in range(10): #시작 값과 증값감 생략 가능 , 끝값은 0 값/ 증값값은 양수1이 기본값
#     print(i)

# for i in range(10,2): 
#     print(i)

# for i in range(0,10,2):
#     print(i)

# print("시작값, 끝값, 증가값(1) 입력받아 시작과 끝 값 사이의 7의 배수를 출력하시오.")
# su1=0
# su2=0
# su1=int(input("시작 값 :"))
# su2=int(input("끝 값 :"))
# for i in range (su1, su2+1,1) :
#     if i%7==0: print(i)

# print("1~100 사이의 값 중 3의 배수 이며, 5의 배수에 해당하는 합을 구하시오.")
# i,sum= 0,0
# for i in range (1,100+1,1):
#     if i %3 == 0 and i %5 == 0: 
#         sum=sum+i
# print(sum)
        

print ("두수를 입력 받아 입력 받은 두수의 범위 안의 합을 구하시오.")
su1=int(input("임의의 수1:"))
su2=int(input("임의의 수2:"))
i,sum= 0,0
if su1 > su2 :
    for i in range (su2,su1+1,1):  
        sum=sum+i
    print(sum)
else:
    for i in range (su1,su2+1,1):  
        sum=sum+i
    print(sum)




# print ("첫날에 10원을 예금하고, 다음날에는 전날의 2배를 예금하는 방식으로 한달(30일) 동안 저축한 금액중 저금액을 구하시오\n")







    






