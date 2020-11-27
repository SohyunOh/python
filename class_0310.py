# a[i]>a[j]
# a[i]>a[j]
# a[i]a[j]=a[j]a[i]

# ls =[4,8,2,7,6]
# for i in range(len(ls)):
#     i[0] < i [1:4]
#     for i in range(len(ls)):
#         i[1] < i [2:4]


# ls =[4,8,2,7,6]
# for i in range(len(ls)-1):
#     for j in range(i+1,len(ls)):
#         if ls[i] > ls[j]:
#             if ls[i]>ls[j]:
#                 ls[i],ls[j]=ls[j],ls[i]
# print(ls)

# 순위구하기

# ls=[82,85,76,79,96]
# ls_con=[1,1,1,1,1]
# for i in range(len(ls)):
#     for j in range(len(ls_con)):
#         if ls[i]<ls[j]:
#             ls_con[i]+=1
# print(ls)
# print(ls_con)


# ls=[10,20,30]
# ls.append(1000)

# for i in range(len(ls)):
#     print("ls[{}]:{}".format(i,ls[i]))
# print("리스트의 총 개수 :", len (ls))
# print("ls:",ls)
# ls=[]
# print("ls 초기화 후:",ls)

# ls=[]
# for i in range(0,4):
#     ls.append(0)
# Sum=0

# for i in range(0,len(ls)):
#     ls[i]=int(input(str(i+1)+"번째 숫자:"))
#     Sum+=ls[i]    

# for i in range(0,len(ls)):
#     print("입력받은 값 ls[{}]:{}".format(i,ls[i]))
# print("합계:%d"%Sum)

# num=int(input('몇개의 공간 만들겠습니까?:'))
# ls=[]
# Sum=0
# for i in range(num):
#     ls.append(int(input(str(i+1)+"번째 숫자:")))
#     Sum+=ls[i]

# for i in range(0,len(ls)):
#     print("입력받은 값 ls[{}]:{}".format(i,ls[i]))
# print("합계:%d"%Sum)

# List =[30,20,10]
# print("현재 리스트:",List)

# List.append(40)
# print("append(40) 후 리스트:", List)

# print("pop() 으로 출력 한 값:",List.pop())
# print("pop() 후 리스트:", List)

# List.sort()
# print("sort()후 리스트:", List)

# List.remove()
# print("remove() 후 리스트:",List)
# del(List[2])
# print("del() 후 리스트:",List)


# List =[30,10,44,26,15,20,10,45]
# print("현재 리스트:",List)

# print("10값의위치:", List.index(10))

# List.insert(2,200) #입력할 위치와 값을 같이 지정햐줘야함.
# print("insert(2,200) 후 리스트:",List)


# List.remove(10)
# print("remove(10) 후 리스트:",List)

# List.extend([555,666,555])

# print("extende([555,666,555]) 후 리스트:",List)

# print("555값의 개수:", List.count(555))



# =========================================

print("문제1. 리스트 2개를 만들어서 홀수번째의 값, 짝수번째의 값을 따로 넣고 짝수번째와 홀수 번쨰의 차를 또다른 리스트에 넣고 출력")
print("결과 :[5,13,-2,1,-13]")
print()
ls=[10,5,20,7,9,31,12,11,19,32]
ls_wkr=[]
ls_ghf=[]
for i in range(len(ls)):
    ls_wkr = ls[i]
    if ls[i]%2==0 :
        print("짝수:",ls[i]) 
        
    else:
        ls_ghf=ls[i]
        print("홀수:",ls[i])
# print("짝수:",ls_wkr)
# print("홀수:",ls_ghf) 


# print("문제2.ls 의 값 중 인덱스 홀수 번째와 짝수 번쨰의 합과 차를 구하시오.")
# print("짝수번쨰 [0,2,4,8]-[1,3,5,7,9]홀수번째/(결과:-16)")




# print("문제3 ls에 저장된 값을 invertLs에 거꾸로 저장하시오.")
# ls=[10,5,20,7,9,31,12,11,19,32]
# for i in range(len(ls)):
#     ls[i]=(ls[-1 -10])
# print(ls)

# print("ls의 값을 오름차순으로 sortLs에 저장하시오.")
# ls=[10,5,20,7,9,31,12,11,19,32]
# sortLs=[]
# for i in range(len(ls)-1):
#     for j in range(i+1,len(ls)):
#         if ls[i] > ls[j]:
#             if ls[i]>ls[j]:
#                 ls[i],ls[j]=ls[j],ls[i]
#                 sortLs=ls
# print("sortLs:",sortLs)


# print("ls의 값을 내림차순으로 reverseLs에 저장하시오.")
# ls=[10,5,20,7,9,31,12,11,19,32]
# reverseLs=[]
# for i in range(len(ls)-1):
#     for j in range(i+1,len(ls)):
#         if ls[j] > ls[i]:
#             if ls[j]>ls[i]:
#                 ls[j],ls[i]=ls[i],ls[j]
#                 reverseLs=ls
# print("reverseLs:",reverseLs)
