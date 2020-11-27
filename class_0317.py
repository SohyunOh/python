# accountBook ="shose 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"
# #공백과 콤마 로 구분되어있고 품목과 날짜,가격으로 나열
# replaceAB = accountBook.split(',')# ',' 기준으로 리스트 로 저장

# k=0
# for i in replaceAB:
#     replaceAB[k] = i.lstrip(',')#각 문자열의 왼쪽 공백 삭제 후 저장(_coffee,_food,_dress)
#     k+=1
# kk='$ ' #' $' 뒤로 표시 
# print('item'.ljust(10),end="")
# print('date'.ljust(10),end="")
# print('$(price)'.ljust(10))
# for i in range(len(replaceAB)):
#     z= replaceAB[i].split() #공백을 기분으로 리스트로 저장
#     for k in range(len(z)):
#         if k ==0:
#             print(z[k].ljust(10), end="")#10칸 확보 후 왼쪽 출력
#         elif k ==1:
#             print(z[k].ljust(10), end="")#10칸 확보 후 왼쪽 출력
#         elif k ==2:
#             print("{:,}".format(int(z[k])).join(kk).ljust(10))



#===========================================================================================
# ======판단만 하는 함수 = True ot False 판단 ====

# Str = 'python te12st 1324'

# print("Str .isdigit(): ", Str.isdigit()) #숫자로만 구성
# print("Str[9:11] .isdigit(): ", Str[9:11].isdigit())# 숫자로만 구성

# print("Str .isalpha(): ", Str.isalpha())#글자
# print("Str[:6] .isalpha(): ", Str[:6].isalpha())#글자

# print("Str .isalnum(): ", Str.isalnum())#글자+숫자
# print("Str[7:13].isalnum():",Str[7:13].isalnum()) #글자+숫자

# print("Str.islower():",Str.islower())#소문자
# print("Str.isupper():",Str.isupper())#대문자
# print("Str.isspace():",Str.isspace())#공백


# =========================================================================================
# # 문자구성요소 파악 함수, 리플레이스, 하이픈을 기준으로 왼쪽 오른쪽 검사할수있도록 파인드
# info = """
# jo 9abc08-302023
# cho 900402-1011232
# test 1234567-1234567
# lee 980908-3a2c0c3
# kim 900514-2022023
# """
# print(info)
# k=0
# for i in range(info.count('-')):
#     k=info.find('-',k+1)
#     if info [k+1:k+8].isdigit() and not info[k-7:k].isdigit and info[k-6:k].isdigit():
#         info =info.replace()

# <풀이>============================================================================
# info = """
# jo 9abc08-302023
# cho 900402-1011232
# test 1234567-1234567
# lee 980908-3a2c0c3
# kim 900514-2022023
# """
# print(info)
# k=0
# for i in range(info.count('-')): #'-'로 반복문 횟수 결정
#     k=info.find ('-',k+1) #find로 팢고 찾은 다음 K+1로 다음 걸 또 찾는다.
##여러 행의  문자열이지만 인덱스 값은 계속 연속적이기 때문.
#     if info [k+1:k+8].isdigit() and not info[k-7:k].isdigit() and info[k-6:k].isdigit():
## '-'을 기준으로 뒷 7자리가 숫자로만 되어있는지, 7자리(6자리도 있음)가 숫자로만 이루어지 말아야함.
##다시 6자리만 숫자로 이루어져있는지.
#         info =info.replace(info[k+1:k+8],'*******') #6가지 조건을 만족하는 값만 '-'을 기준으로 7자리 *로 출력
# print(info)

# =================================================================================================
# 함수 - 어떤 이름을 가진 코드가 구체적으로 어떻게 동작하는지 구체적으로 기술하는 것
# 파이선에서는 함수나 메소드를 정의할때 definition를 두인 키워드인 'def'를 사용_사용자 정의 함수
# 내장 함수 (컴파일에 내용 포함),외장함수 (사용자 모듈함수로 사용할때 마다 불러오기 예)decopy 활용) 

# result,temp = 0,0
# result = int (input("수 입력 : "))
# while True:
#     temp = int(result%10) #임시변수에 나머지 값 
#     result= int (result/10) #나머지에 몫값만 
#     print(temp,end="")
#     if not result: break; 
#     #result 0이 되면 부정을 시키면 참가 , 남아 있지 않으면 거짓 -거짓이여서 break실핼하지 않고 반복
# print("\n 프로그램 종료")


# 여러(5)개 입력할경우 
# result,temp = 0,0
# for i in range (5):
#     result = int (input("수 입력 : "))
#     while True:
#         temp = int(result%10)
#         result= int (result/10)
#         print(temp,end="")
#         if not result: break;
#     print("\n 프로그램 종료")

# ===========================================================================
# 꺼구로 함수 정의함

# def  reverseCode():
#     result,temp = 0,0
#     result = int (input("수 입력 : "))
#     while True:
#         temp = int(result%10)
#         result= int (result/10)
#         print(temp,end="")
#         if not result: break;
#     print()
# print("프로그램시작")
# reverseCode()
# print("\n 프로그램 종료")

# ================================================================================
# #***
# def sel_machine():#변수와 규칙이 같음, 숫자가 앞으로 올수없음. 앞에'_',한글 사용가능 /공백,특수문자안됨 
#     sel =0
#     sel =int (input("음료 선택\n1.골라\n2.핫6\n3.포카리\n입력:"))
#     if sel ==1 : print('콜라등장')
#     if sel ==2 : print('핫6등장')
#     if sel ==3 : print('포카리등장')
#     else : print('만들어 드세요^^')

#     if sel >= 1 and sel<=3:
#         print("맛있게 드세요^^")
# sel_machine()

# ========================================================================
# 예제
# def calc():
#     result =0
#     su1,op,su2 = int(input("숫자 :")),input("부호:"),int(input("숫자:"))
#     result = su1+su2
#     print(su1,'+',su2,'=',result)
# calc()    

# +,-,*,/연산식 만들기
# def calc():
#     result =0
#     su1,op,su2 = int(input("숫자 :")),input("부호:"),int(input("숫자:"))
#     if op == '+': result = su1+su2
#     elif op == '-': result = su1-su2
#     elif op == '*': result = su1*su2
#     elif op == '/': result = su1/su2
#     print("%d%s%d=%.2f"% (su1,op,su2,result))
# calc()

# ===============================================================================
# def calc(su1,op,su2 ):#매개변수에서 인수 전달받음 / 지역변수 (종속된곳에서 사용되고 소멸)
#     result =0 #초기화 연산이 이루어질걸 알수있음
#     result = su1+su2 #연산자 부호는 활용이 안됨.
#     print('calc 실행')
#     return result # 되돌려 받는 값 상수를 지정하면 매번 상수지정되어 출력 됨. 

# su1,op,su2 = int(input("숫자 :")),input("부호:"),int(input("숫자:"))
# result =calc(su1,op,su2)
# print(su1,'+',su2,'=',result) #전역변수  프로그램시작할때 부터 메모리 할당된 변수가 그대로 보존됨.

# print("다음문장")

# # =================================================================================
# def showAvrg(a,b,c):
#     print("{}와{}의 평균".format(a,b))
#     print("값은{}입니다.".format(round(c,1))) #반올림 함수에 소수 첫째 자리 짤라씀
# def avrg(j,k):
#     total= j+k;
#     f= total/2
#     return f;
# i=2; j=3;
# f=avrg(i,j)
# showAvrg(i,j,f)
# print()

