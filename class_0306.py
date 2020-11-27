# =================while(무한반복) =================

# i=0
# while i<5:
#     print(i,"종속문장")
#     i+=1
# # print(i)  - 마지막 i는 5까지 대입해서 결과값이 나옴. 
# print("다음문장")

# for i in range(0,5) :
#     print(i,"종속문장")
# print("다음문장")

# i=1
# odd,even=0,0
# while i<=10:
#     if i %2 ==0:
#         even+=i
#     else:
#         odd+=i
#     i+=1
# print("1-10 짝수의 합:",even)
# print("1-10 홀수의 합:",odd)

# ##
# i=1
# odd,even=0,0
# for i in range(1,11,1):
#     if i %2 ==0:
#         even+=i
#   else:
#         odd+=i
# print("1-10 짝수의 합:",even)
# print("1-10 홀수의 합:",odd)


# i=1
# while True:
#     print(i,"종속문장",end="")
#     i+=1

# i=1
# flag= True #변수 대입
# while flag:
#     print(i,"종속문장",end="")
#     if i ==10 :
#         flag = False
#     i+=1
# # flag = 깃발 (상태,표시,스위치 용도(True-False,+-1, 양극화))

# # ============기타제어문============
# *break문
# -for,while 문에서 실행 루프로부터 벗어나려고 할떄
# *comtinue 문
# -for,while 문에서 실행 내에서 실행 순서를 무조건 제어 루프의 조건식으로 옮겨서 다음번 반복 실행


# i=0
# while True :
#     if i ==3:
#         break
#         print("3출력")
#     print(i,"출력")
#     i+=1

# i=0
# while True :
#     if i ==3:
#         print("3출력")
#         break
#     print(i,"출력")
#     i+=1

#@@
# i=0
# while i<5:
#    i+=1
#    if i == 3:
#        continue
#        print("3출력")
#     print(i,"출력")
# print("다음문장")
# @@
# for i in range(1,6)
#    if i == 3:
#        continue
#        print("3출력")
#     print(i,"출력")
# print("다음문장")

#예제
# num,result,i =0,0,1
# while True:
#     num = int(input("1~10사이의 숫지 입력:"))
#     if num <1 or num>10:
#         print("잘못 입력 다시")
#         continue
#     break
# else:
#     print("naxt...")
# while i<=num:
#     result+=i; i+=1
# else:
#     print("1~",num,"까지의 합:",result)

#1.풀이
# num,result,i =0,0,1
# while True:
#     num = int(input("1~10사이의 숫지 입력:"))
#     if num <1 or num>10:
#         print("잘못 입력 다시")
#         continue
#     break
# print("naxt...")
# while i<=num:
#     result+=i; i+=1
# else:
#     print("1~",num,"까지의 합:",result)

# 2.풀이
# num,result,i =0,0,1
# while True:
#     num = int(input("1~10사이의 숫지 입력:"))
#     if num <1 or num>10:
#         print("잘못 입력 다시")
#         continue
#     print("naxt...")
#     break
# while i<=num:
#     result+=i; i+=1
# else:
#     print("1~",num,"까지의 합:",result)

# 풀이3@@
# num,result,i =0,0,1
# flag=True
# while flag:
#     num = int(input("1~10사이의 숫지 입력:"))
#     if num <1 or num>10:
#         print("잘못 입력 다시")
#         continue
#     else:
#         flag=True
# else:
#     print("naxt...")
    
# while i<=num:
#     result+=i; i+=1
# else:
#     print("1~",num,"까지의 합:",result)

# for 문 예제
# for i in range (0,3,1):
#     for k in range (0,5,1):
#         if k ==3:
#             break
#         print("(i:%d\tk:%d)"%(i,k))

# 중첩 while문 바꾸기
# i=0
# while i <3:
#     k=0
#     while k <5 :
#         if k == 3:
#             break
#         print("(i:%d\tk:%d)"%(i,k))
#         k+=1
#     i+=1

# 쌀 100통 (1통당=1kg , 총100000g) , 암수1쌍(2마리) ,하루 20g씩 먹고 10일(10,20,30) 마다 쥐수 2배씩 증가
# 몇일 만에 창고의 쌀이 모두 주의 먹이가 될까, 쥐는 총 몇마리

totl_eat = 100000
eat =0
mouth=2
day=10

while eat < 100000:
    eat+=mouth*20
    if day 
        while
        break*i (mouth*=2)
        









    















