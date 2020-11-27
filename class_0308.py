# i=0
# while i<5:
#     print(i,"종속문장")
#     i+=1
# print("다음문장")

# i=0
# for i in range (5):
#     print(i,"종속문장")

# i=1
# odd,even=0,0
# while i<=10:
#     if i%2==0:
#         even+=i
#     else :
#         odd+=i
#     i+=1
# print("1-10 짝수의 합: ",even)
# print("1-10 홀수의 합: ",odd)

# odd,even=0,0
# for i in range (1,11,1):
#     if i%2==0:
#         even+=i
#     else :
#         odd+=i
 # print("1-10 짝수의 합: ",even)
# print("1-10 홀수의 합: ",odd)


# i=0
# while i<5:
#     print(i,"종속문장")
#     i+=1
# else :
#     print("조건식이 거짓일 경우:",i)
# print()    

# i=1
# while True:
#     print(i,"종속문장",end="")
#     i+=1

# i=1
# flag=True
# while flag:
#     print(i,"종속문장",end="")
#     if i == 10:
#         flag=False
#     i+=1

# i=0
# while True:
#     if i == 3:
#         break
#         print("3출력")
#     print(i,"출력")
#     i+=1
# print("다음 문장")

# i=0
# while i<5:
#     i+=1
#     if i == 3:
#         continue
#         print("3출력")
#     print(i,"출력")
# print("다음 문장")


# for i in range(1,6,1):
#     if i == 3:
#         continue
#         print("3출력")
#     print(i,"출력")
# print("다음 문장")

# num,result,i=0,0,1
# while True:
#     num = int(input("1~10사이의 숫자 입력 : "))
#     if num<1 or num>10:
#         print("잘못 입력 다시")
#         continue
#     break
# else:
#     print("next...")
# while i<=num:
#     result+=i; i+=1
# else:
# print("1~",num,"까지의 합 : ",result)


# num,result,i=0,0,1
# while True:
#     num = int(input("1~10사이의 숫자 입력 : "))
#     if num<1 or num>10:
#         print("잘못 입력 다시")
#         continue
#     break
# print("next...")
# while i<=num:
#     result+=i; i+=1
# else:
#     print("1~",num,"까지의 합 : ",result)


# num,result,i=0,0,1
# while True:
#     num = int(input("1~10사이의 숫자 입력 : "))
#     if num<1 or num>10:
#         print("잘못 입력 다시")
#         continue
#     print("next...")
#     break
# while i<=num:
#     result+=i; i+=1
# else:
#     print("1~",num,"까지의 합 : ",result)


# num,result,i=0,0,1
# flag = True
# while flag:
#     num = int(input("1~10사이의 숫자 입력 : "))
#     if num<1 or num>10:
#         print("잘못 입력 다시")
#         continue
#     else:
#         flag= False
# while i<=num:
#     result+=i; i+=1
# else:
#     print("1~",num,"까지의 합 : ",result)

# for i in range ( 0 , 3 , 1):
#     for k in range ( 0 , 5 , 1):
#         if k == 3:
#             break
#         print("(i : %d\tk : %d)" % (i , k ))

# i=0
# while i< 3:
#     k=0
#     while k<5:
#         if k == 3:
#             break
#         print("(i : %d\tk : %d)" % (i , k ))
#         k+=1
#     i+=1


#100통 1kg
rice = 100000
mouse = 2
day=1
while rice>0:
    rice -= mouse*20
    if day%10 ==0:
        mouse *= 2
    if rice <= 0:
        break
    day+=1
    print(day,'일',mouse,'마리')
    


# money,j=0,0;
# money = int(input('요금을 투입 하세요 : '))
# while True:
#     print("==========커피 자판기==========")
#     print("1. 커피(200)\t2. 코코아(250)\t3. 반환\t4. 종료\n")
#     j = int(input("메뉴를 선택하세요>>> "))
#     if j == 4: break
#     elif ((j == 1 and money < 200) or (j == 2 and money< 250)):
#         print("요금이 부족합니다")
#     elif j == 1: print("맛있게 드세요");money -= 200
#     elif j == 2: print("맛있게 드세요");money -= 250
#     elif j == 3:print('반환 금액 : ',money);money=0
#     else: print("잘못입력하셨습니다")
# print('프로그램 종료')














