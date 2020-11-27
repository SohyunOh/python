# print("시작값, 끝값, 증가값(1) 입력받아 시작과 끝 값 사이의 7의 배수를 출력하시오.")
# su1=0
# su2=0
# su1=int(input("시작 값 :"))
# su2=int(input("끝 값 :"))
# for i in range (su1, su2+1,1) :
#     if i%7==0: print(i)

# print("시작값, 끝값, 증가값(1) 입력받아 시작과 끝 값 사이의 7의 배수를 출력하시오.")#
# st=int(input("시작 값  입력:"))
# en=int(input("끝 값 입력:"))
# pt=int(input("증가 값 입력:"))
# for a in range (st, en+1,pt) : # i 외에도 다른 문자 가능
#     if i%7==0: 
#         print("%d"%a,end=" ")

# print("1~100 사이의 값 중 3의 배수 이며, 5의 배수에 해당하는 합을 구하시오.")
# i,sum= 0,0
# for i in range (1,100+1,1):
#     if i %3 == 0 and i %5 == 0: 
#         sum=sum+i
# print(sum)

# print("1~100 사이의 값 중 3의 배수 이며, 5의 배수에 해당하는 합을 구하시오.")#
# sum_= 0
# for i in range (1,101):
#     if i %3 == 0 and i %5 == 0: 
#         sum_+=i
# print(sum_)

# print ("두수를 입력 받아 입력 받은 두수의 범위 안의 합을 구하시오.")
# su1=int(input("임의의 수1:"))
# su2=int(input("임의의 수2:"))
# i,sum= 0,0
# if su1 > su2 :
#     for i in range (su2,su1+1,1):  
#         sum=sum+i
#     print(sum)
# else:
#     for i in range (su1,su2+1,1):  
#         sum=sum+i
#     print(sum)

# print ("두수를 입력 받아 입력 받은 두수의 범위 안의 합을 구하시오.")#
# sum_= 0
# num1=int(input("첫번쨰 정수 입력:"))
# num2=int(input("두번쨰 정수 입력:"))
# if num1<num2 :
#     for i in range (num1,num2+1,1):  
#         sum_+=i
#     print(sum_)
# #elif num2<num1: -로 범위 지정 가능
# else:
#     for i in range (num2,num1+1,1):  
#         sum_+=i
#     print(sum_)

# # print ("첫날에 10원을 예금하고, 다음날에는 전날의 2배를 예금하는 방식으로 한달(30일) 동안 저축한 금액중 저금액을 구하시오\n")
# save=10 #첫날에 저축된것
# money=10
# for day in range(2,31):
#     money*=2
#     save+=money
# print("마지막 입금액:",money)
# print("총 저축된 금액:",save)

# =================================================================================================
# #리스트 자료형 - 변수에 차례대로
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print("i:",i)

# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print("상준썜 짱")

# Is=[1,2,3,4,5,6,7,8,9,10]
# for i in ls:
#     print("i:",i)
# for i in ls:
#     print(i,end="")

# #range - 범위 / 변수를 리스트로 만들어서 출력 

# ls=[10,"test",123.123] # 정수 문자열 실수 등 각각다른 자료형 대입 
# print("list:",ls)
# print()
# for i in ls:
#     print("i에 ",i,"대입한 후 print () 실행")
#     print(type(i))

# st="Hello python" #단일문자로 인덱스 존재 
# for i in st:
#     print("i:",i)
# for i in st:
#     print(i,end="")
# print()
# # a=0
# # for i in st:
# #     a+=1
# #     print("%d"%a)


# st="It is a fun Python class"

# a,b,c = 0,0,0
# for i in st:
#     if i =="a" : a+=1
#     # print("a의 개수:%d"%a)
#     if i == "s" : b+=1
#     # print("s의 개수:%d"%b )
#     c+=1
# print(a)
# print(b)
# print("i:",c)


# st="It is a fun Python class"
# to_cnt=0
# a_cnt=0
# s_cnt=0
# for i in st:
#     to_cnt+=1
#     if i =='a':
#         a_cnt+=1
#     if i =='s':
#         s_cnt+=1
#     # to_cnt+=1 
# print("총 개수:%d\na의 개수: %d\ns의 개수: %d\n"% (to_cnt,a_cnt,s_cnt))



# # ======포맷 함수 (출력함수) #순서 지정 대로 호출 
# print("{0}+{1}={2}".format(10,2,10+2))
# print("{2}+{1}={0}".format(10,2,10+2))
# print("{}+{}={}".format(10,2,10+2))

# print("{:,}".format(1000000))

# print("{:<10}, 왼쪽정렬 ,{:0<10}".format('첫번째','두번쨰'))
# print("{:>10}, 오른쪽정렬 ,{:9>10}".format('첫번째','두번쨰'))
# print("{:^10}, 정렬 ,{:5^10}".format('첫번째','두번쨰'))
# print("{:^10}, 정렬 ,{:-^10}".format('첫번째','abc')) 
# # %(서식제어문)는 -c언어 , .format는 python

# print("{:=^16}".format('첫번째'))

# for i in range(0,3,1):
#     for k in range(0,5,1):
#         print("이중 for 문(i:%d\tk:%d)"%(i,k))


# print("{:-^60}".format('구구단'))
# print("2단\t3단\t4단\t5단\t6단\t7단\t8단\t9단")
# print("{:-^63}".format(''))

# for i in range(1,10,1):
#     for j in range(2,10,1):
#         print("%d*%d=%d"%(j,i,i*j),end="\t")
#     print()    


# print("{:-^61}".format('구 구 단'))
# for i in range(2,10):
#     print("{:^5}".format('%d단'%i),end="\t")
# print()  
# print("-"*64)  
# for i in range(1,10,1):
#     for j in range(2,10,1):
#         print("%d*%d=%d"%(j,i,i*j),end="\t")
#     print()    

# for i in range(0,5,1):
#     print("상위 포문%d 일때 하위 포문 :"%i, end="")
#     for j in range(0,5,1):
#         print(i*j, end=" ")
#     print()

# for i in range(5):
#     print("상위 포문%d 일때 하위 포문 :"%i, end="")
#     for j in range(5):
#         print(i*j, end=" ")
#     print()

# for i in range(1,22,5): #세로 규칙 
#     for j in range(5):
#         print(i+j,end="\t")
#     print()
  
# for i in range(1,22,5):  
#     print(i,end="\t")
#     for j in range(1,5):
#         print(i+j,end="\t")

# for i in range(1,22,5):
#     print(i,end='')
#     for j in range(1,5):
#         print(j+i,end='')
#     print()

# for i in range(0,5):
#     for j in range(1,6):
#         print(j+5*i,end='\t')
#     print()    


num=0
su1=1
for i in range(1,6,1):
    num=i*5
    for k in range(su1,num+1,1):
        print(k,end='\t') 
    print()
    su=num+1


   






















