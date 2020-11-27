#   지역 변수

# def func2(a,b):
#     a+=5; b*=10
#     print("func2:a={},b={}".format(a,b))
# def func1():
#     a=5; b=10
#     func2(a,b)
#     print("func1:a={},b={}".format(a,b))
# func1()

# def func2(a,b): #func1지역에서의 연산된 func2를 대입하여 연산
#     a+=5; b*=10
#     print ("func2: a={},b={}".format(a,b))#12~14까지 func2의지역
# def func1(): # 첫실행후 이 지역 함수 실행
#     a=5; b=10 #func2에 대입
#     func2(a,b) #대입후 위로 가서 대입
#     print("func1: a={},b={}".format(a,b)) #마지막 대입 실행
# func1() 첫 실행 
#C언어는 메모리 주소로 할당되어 메모리 관리 용의
# =======================================================================

# def aa(a): #던져주는 인수값 1 
#     if a == 1: #a가 1이면 
#         print('1입력')
#     print('다음문장 실행')
# a=aa(1) #함수 호출
# print("리턴값 :",a) # 함수를 호출하기만하고 되돌려 받는 값이 없음none
# print("프로그램 종료")

# def aa(a):
#     if a == 1:
#         return # return만 쓰면 함수의 종료를 의미함
#return함수가 호출한 곳으로 되돌아감.
#         print('1입력')
#     print('다음문장 실행')
# a=aa(1)
# print("리턴값 :",a)
# print("프로그램 종료")

# def aa(a):
#     if a == 1:
#         return 'end' #a는 대입되고 소멸/ 문자열(end), 불영(True)도 가능
#         print('1입력')
#     print('다음문장 실행')
# a=aa(1) #return a은 a에 되돌려주고 소멸
# print("리턴값 :",a) #위 a를 받아서 출력
# print("프로그램 종료")

# ========================================================

# def move():
#     print('이동')
# def attack():
#     print('공격')
# def defense():
#     print('방어')
# move()
# attack()
# defense()

# ============================================
# 협업중 앞의 코드가 필요할경우 그 하위버젼을 코드 할때 앞부분은 비워두는 방법
# def move():
#     pass
# def attack():
#     pass
# def defense():
#     pass
# move()
# attack()
# defense()

# ===========================================

# def a(a):
#     if a==1:# 참일때 조건이 정해지지 않았을 경우 pass로 비워두고 진행함.
#         pass
#     else: #거짓을때의 조건은 명확히 명시되어있음
#         print('1이 아니에요.')
# a(1)

# =============================================================================================================
#문제 1. 짝,홀를 구분하는 함수 만드시오.

# def su_co(su) :
#     if su %2==0 :
#         print("짝수입니다.")
#     else:
#         print("홀수입니다.")
#     print()
# su=int(input("수 입력:"))
# su_co(su)


## 문제1번 풀이 1=============================================
# num1=int(input("정수 입력:"))
# if su1 %2==0 :
#         print("%d 짝수입니다."%num1)
#     else:
#         print("%d홀수입니다."%num1)
# -----------------------------------------
# def input_func(): 
#     num1=int(input("정수 입력:")) #입력받기
#     hol_jjak(num1) #홀짝수 판단, #호출할려면 입력 받은 num1 호출 인수넣기
# def hol_jjak(num1):
#     if (num1%2==0): #호출된 인수가 0과 같으면 참 
#         output_Data(1) #참값이면 상수 1, 거짓이면 상수 0을 가져감
# # 함수를 호출하여 참,거짓 구분
#     else :
#         output_Data(0)
# def output_Data(a): #참이면1, 거짓이면 0 값이 가지고 대입
#     if(a):#if는 함수연산식분만 아니라 일반 연산식, 변수, 상수 다 가능
#         print("짝수")
#     else:
#         print("홀수")    
# input_func() #원하는 값
# # 문제1번 풀이 2============================================
# def hol_jjak(num1):#retur값을 받음
#     if num1%2: #1이 나오면 참값
#         return " 홀수입니다"
#     else:
#         return " 짝수입니다"
# num1=int(input("정수 입력:"))
# ret=hol_jjak(num1) #def에서 연산된 값을 변수에 대입함.
# print("%d는 %s이다"% (num1, ret))


# #문제2. 3의 배수를 판별하는 함수를 만드시오.=======================================================

# def mul3(su):
#     if su %3 == 0 : 
#         print("3의 배수입니다.")
#     else:
#         print("3의 배수가 아닙니다.")
#     print()
# su=int(input("수 입력:"))
# mul3(su)

# 문제2번 풀이 1=============================================
# num1=int(input("정수 입력:"))
# if num1 %3 == 0 :
#      print("%d의 3의 배수입니다."%num1)
# else:
#      print("%d의 3의 배수가 아닙니다."%num1)
# # ------------------------------------------------------------
# def three_func(num1): #함수 정의하기 
#     if num1 %3  : #3으로 안떨어짐.
#         return "3의 배수가 아니다."
#     else: #3으로 떨어짐
#         return "3의 배수이다."
# num1=int(input("정수 입력:")) #입력 받기 
# ret= three_func(num1) #대입 시켜 함수 호출,인수전달
# print("%d의 %s"%(num1,ret))
# -------------------------------
# def three_func(num1):
#     if num1 %3 ==0 :
#         return 1
#     else:
#         return 0
# num1=int(input("정수 입력:"))
# ret= three_func(num1)
# if (ret):
#     print ("%d의 3의 배수 입니다."%num1)
# else :
#     print ("%d의 3의 배수가 아닙니다."%num1)

# # 문제3. 이전 예제 계산기를 입력, 출력, 연산기능으로 나눠서 실행되게 만드시오.=======================================================

# def su():
#     su1=int(input("숫자 :"))
#     op=input("부호:")
#     su2=int(input("숫자:"))

# def calc(su1,op,su,result):
#     result =0
#     if op == '+': result = su1+su2
#     elif op == '-': result = su1-su2
#     elif op == '*': result = su1*su2
#     elif op == '/': result = su1/su2
#     print("%d%s%d=%.2f"% (su1,op,su,result))


# def su_print(calc):
#     print("%d%s%d=%.2f"% (su1,op,su,result))

# su()
# calc(su)
# su_print(calc)

# 문제3번 풀이 1==(시작부터 함수로 시작)==========================
# def input_data(): #입력함수 정의 
#     num1,op,num2=int(input("숫자 :")),input("부호:"),int(input("숫자:"))
#     calc_func(num1,op,num2) #연산기능으로 넘기기위한 함수
# def calc_func(num1,op,num2): #입력받아 연산기능 함수 정의하기
#     if op == '+': result = num1+num2 #if po가 +와 같다면 ret은 mun1 +num2와 같다.
#     elif op == '-': result = num1-num2 
#     elif op == '*': result = num1*num2
#     elif op == '/': result = num1/num2
#     output_data(num1,op,num2,result) #연산 수행 값을 함수 인수에 넣어주기
# def output_data(num1,op,num2,result):#4의 인수를 다 받아오기    
#     print("%d%s%d=%.2f"% (num1,op,num2,result))# 대입
# input_data()#입력함수

# # 문제4. 이전 거꾸로 수를 반환하는 함수를 만드시오.=======================================================

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

# 문제4번 풀이 1=============================================
# num1 = int(input("정수 입력 : "))
# ret=0
# while(True): 
#     tmp=num1%10  #나머지값을 집어넣음
#     ret=ret*10  
#     ret=ret+tmp
#     num1=num1//10 #몫값만 저장되어야함. 
#     if num1==0:
#         break
# print(ret)
# -------------------------------------
# def revers_code(num1):
#     ret=0
#     while(True):
#         tmp=num1%10 
#         ret=ret*10
#         ret=ret+tmp
#         num1=num1//10 
#         if num1==0:
#             return ret

# num1 = int(input("정수 입력 : "))
# ret=revers_code(num1)
# print("입력된 수:%d -> 거꾸로 수: %d"% (num1,ret))

# =======================변수 스코필 룰 ==========================================================
# 변수 [스코필 룰]
# 지역변수는 한정된 지역에서만 사용되는 변수,
#  전역변수는 프로그램 전체에서 사용되는변수

# def func1():
#     a=100
#     print("func1의 a:%d" %a)
#     print(id(a))
# def func2():
#     a=200 # func2 지역의 a인수 대입
#     print("func2의 a:%d" %a)
#     print(id(a))
# func1()
# func2() #func1과 funt2 는 다른 객체(주소확인) 
# -----------------------------

# def func1():
#     print("func1의 a:%d" %a)

# def func2():
#     print("func2의 a:%d" %a)

# a=200 #전역 변수

# func1()
# func2()
# ---------------------------------
# def func1(): # 전역 변수보다 지역 변수 먼저 적용
#     a=123 #지역 변수
#     print("func1의 a:%d" %a)

# def func2():
#     print("func2의 a:%d" %a)#전역 변수로 대입
# a=200 #전역 변수
# func1()
# func2()
# print(a)
# ---------------------------------

# def func1():
#     global a #지역변수를 전역 변수로 사용하겠다는 함수 
#     a=1222
#     print("func1의 a:%d" %a)
# def func2():
#     print("func2의 a:%d" %a)
# a=200 #전역 변수 => func1dml giobal로 인해 global a 전역변수로 넣어짐
# func1()
# func2()

#지역변수로 사용하면 데이터가 망가질 일이 없음. 
#전역변수는 프로그램이 종료되지 않는 이상 계속 남아있어 메모리에 남아 비효율적
#c언어엑서는 스택틱이라는 정적변수 가 있음.
# -----------------------------------------------
# for i in range(11):
#     a=10 #int a=10 (계속 10으로 인식), 10을 계속 할당하고 출력함.
#     print(a) 
#     a+=1

# a=10 
# for i in range(11):
#     print(a)
#     a+=1

# -----------------------------------


num=10
sum=0
def display():
    sumFunc() 
    print("10까지의 합 :", sum)
def sumFunc():
    # global sum
    sum=0 
    for i in range(num+1):
        sum+=i 
display()

# def display():
#     num=10
#     print("10까지의 합 :",sumFunc(num))
# def sumFunc(num):
#     # global sum
#     sum=0 
#     for i in range(num+1):
#         sum+=i 
#     return sum
# display()




