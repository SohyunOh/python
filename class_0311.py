
# ls=[10,5,20,7,9,31,12,11,19,32]
# hol_ls=[]
# jjak_ls=[]
# sub_ls=[0,0,0,0,0]
# for i in range(len(ls)): 
#     if i %2 == 0 :
#         jjak_ls.append(ls[i])
#     else:
#         hol_ls .append (ls[i])

# for i in range(len(jjak_ls)):
#     sub_ls[i]=jjak_ls[i]-hol_ls[i]
#     sub_ls.append(jjak_ls[i]-hol_ls[i])
# print(sub_ls)

# print("문제2.ls 의 값 중 인덱스 홀수 번째와 짝수 번쨰의 합과 차를 구하시오.")
# print("짝수번쨰 [0,2,4,8]-[1,3,5,7,9]홀수번째/(결과:-16)")
# jjak_sum=0
# hol_sum=0
# ls=[10,5,20,7,9,31,12,11,19,32]
# for i in range(len(ls)):
#     if i%2==0:
#         jjak_sum +=ls[i]
#     else:
#         hol_sum +=ls[i]
# print(jjak_sum-hol_sum)

# print("문제3 ls에 저장된 값을 invertLs에 거꾸로 저장하시오.")

#  ls=[10,5,20,7,9,31,12,11,19,32]
# for i in range(len(ls)):
#     ls[i]=(ls[-1 -10])
# print(ls)

# ls=[10,5,20,7,9,31,12,11,19,32]
# inverls=[]
# for i in range(1,11):
#     inverls.append(ls[-1])
# print(ls)

# ls=[10,5,20,7,9,31,12,11,19,32]
# j=10
# inverLs=[0,0,0,0,0,0,0,0,0,0]
# for i in range(0,10,1):
#     j-=1
#     inverLs[i]=ls[j]
# print("ls:",ls)
# print("inverls:\n",inverLs)


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

# ls=[10,5,20,7,9,31,12,11,19,32]
# sortLs=ls[:]
# for i in range(len(ls)-1):
#     for j in range(i+1,len(ls)):
#         if sortLs[i] > sortLs[j]:
#             sortLs[i], sortLs[j]= sortLs[j], sortLs[i]
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



# aa=[[1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]]

# print('[0][0]',aa[0][0])
# print('[0][1]',aa[0][1])
# print('[0][2]',aa[0][2])
# print('[0][3]',aa[0][3])
# print('[1][0]',aa[1][0])
# print('[1][1]',aa[1][1])

# for i in aa:
#     for j in i:
#         print(j,end='\t')
#     print()
# print()

# for i in range (len(aa)):
#     for j in range(len(aa[0])):
#         print(aa[i][j],end='\t')
#     print () 

# # [얕은 복사] ; 동기화
# aa=[[1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]]

# a=aa[0]
# a[1]=20000

# print('[0]',aa[0])
# print(a)
# print(aa)


# # [깊은복사]
# aa=[[1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]]

# a=aa[0][:] # 0번 인덱스 지정[1,2,3,4] 를 지정해서 a에 넣겠다
# a[1]=20000 # 0(1),1(2)번쨰 인덱스에 2000을 넣음

# print('[0]',aa[0])
# print(a)
# print(aa)



# # 변수:
# ls_1=[] ; ls_2=[];value=1  #(반복문이용)
# for i in range (3):
#     for i in range(4):
#         ls_1.append (value)
#         value+=1
#     ls_2.append (ls_1) 
#     ls_1=[]
# # print(ls_2)
# for i in ls_2:
#     for j in i :
#         print(j,end='\t')
#     print () 

# map 함수
# be = ['2019','12','31']
# print(be)

# af =list(map(int,be))
# print(af)

# ******
# be=[
#     ['100'],
#     ['200'],
#     ['300'],
# ]
# print('수정:', be )
# for i in range(len(be)):
#     be[i]=list(map(int,be[i]))
# print(be)

# for i in range(len(be)):
#     be[i][0] = str(be [i][0]*100)
# print('수정 후:',be)

# *****tuple
# tp=(10,20,30) 
# print("tp:",tp)
# print("tp type :",type(tp))
# print("tp len:" ,len(tp))

# tp1=10,20,30
# print("tp1:",tp1)
# print("tp1 type :",type(tp1))

# print("tp1[0] type:", type(tp1[0]))

# tp1[0]=100 # 에러발생

# tpType ="문자열",100,1.111

# print("tpType :", tpType)
# print("tpType :", type(tpType))
# print("tpType[0]type ;", type(tpType[0]))
# print("tpType[1]type ;", type(tpType[1]))
# print("tpType[2]type ;", type(tpType[2]))

# tplnt=(10)
# print("tplnt:", type(tplnt)); #<class 'int'>

# tpT1 =(10,)
# print("tpT1:",type(tpT1)); #<class 'tuple'>

# tpT2 =10,
# print("tpT2:",type(tpT2)); #<class 'tuple'>

# tt1 =(10,20,30,40)
# tt2 =tt1[0]+tt1[1]+tt1[2]+tt1[3]
# print("튜플 힙: %d"% tt2)

# print("tt1[1:3]:",tt1[1:3])
# print("tt1[1:]:",tt1[1:])
# print("tt1[:3]:",tt1[:3])

# a=1,2,3
# b=4,5,6
# c=a+b

# print("a:",a)
# print("b:",b)
# print("c:",c)

# *******중요******* 함수에서 쓸 예정
# 포장 - 포장 벗기기
# pack=1,2,"패킹"
# print("packing\npack:", pack)

# a,b,c= pack
# print("unpacking\na:",a,"b:",b,"c:",c)



# # 튜플함수
# tp = 100,200,"함수", 100, '개수'

# print("tp안의 200의 위치:",tp.index(200),"번째 인덱스") #0,2
# # print("tp안의 200의 위치:",tp.index(200) +1,"번째 인덱스") 사람기준2번쨰
# print("tp안의 100의 위치:",tp.count(100),"개")


tp = ("회사정보", "제품명", "가격정보", "출시일")
ls = ["삼성전자", "겔럭시", "100원", "미정"]
tpp=[]
ltt=[]
i=0
for i in range(len(ls)):
    print("%5s\t"%tp[i],":",ls[i])


for i in range(4):
    tpp.append(input("튜플데이터: "))
    lss.append(input("리스트데이터: "))
tpp=tuple(tpp)
for i in range(len(ls)):
    print("%5s\t"%tpp[i],":",lss[i])








