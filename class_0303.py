
# print("입력한 데이터가 3의 배수인 경우 출력")
# num1=int(input("데이터 입력:"))
# if num1 %3 == 0: 
#     print(num1,"은 3의 배수이다")

# num1=int(input("임의의 정수 입력:"))
# if num1 %3 == 0: 
#     print("%d은 3의 배수이다"%num)
# if not(num%3): 
#     print("%d은 3의 배수이다"%num)



# print("절대값을 구하는 프로그램 작성")
# num2=int(input("데이터 입력:"))
# if num2 >= 0 : print(num2)
# if num2 < 0 : print(-num2)

# num=int(input("임의의 정수 입력:"))
# if num <0:
#     num=num*-1
# print("%d"%num) #print(num)



# print("수를 입력받아 짝,홀수를 구분하여 출력하시오")
# num3=int(input("수 입력:"))
# if num3 %2 == 0: 
#     print("%d는 짝수"%num)
# if num3 %2 == 1: 
#     print("%d는홀수"%num)



# print("두 수를 입력받아 큰수를 출력하시오")
# su1 =int(input("1수 입력:"))
# su2 =int(input("2수 입력:"))
# if su1 > su2 : print(su1) 
# if su1 < su2 : print(su2)

# print("두 수를 입력받아 큰수를 출력하시오")
# su1 =int(input("임의의 정수 입력:"))
# su2 =int(input("임의의 정수 입력:"))
# if su1 > su2 : print("%d가 큰수"%su1) 
# if su1 < su2 : print("%d가 큰수"%su2)


# su1 =int(input("임의의 정수 입력:"))
# su2 =int(input("임의의 정수 입력:"))
# if su1 < su2 :
#     su1=su2
# print(su1)



# print("세 수를 입력받아 큰수 출력")
# su1=int(input("입력"))
# su2=int(input("입력"))
# su3=int(input("입력")) 
# if su1<su2:
#     if su2<su3:
#       print(su3)
# if su1<su3:
#     if su3<su2:
#          print(su2)
# if su2<su1:
#     if su1<su3:
#       print(su3)
# if su2<su3:
#     if su3<su1:
#       print(su1)
# if su3<su2:
#     if su2<su1:
#       print(su1)
# if su3<su1:
#     if su1<su2: 
#       print(su2)

# print("세 수를 입력받아 큰수 출력")
# num1=int(input("임의의 정수 입력:"))
# num2=int(input("임의의 정수 입력:"))
# num3=int(input("임의의 정수 입력:")) 
# if num1>num2 and num1>num3 :
#     print("%d가 가장 큰수"%num1)
# if num2>num1 and num2>num3 :
#     print("%d가 가장 큰수"%num2)
# if num3>num1 and num3>num2 :
#     print("%d가 가장 큰수"%num3)

# print("세 수를 입력받아 큰수 출력")
# num1=int(input("임의의 정수 입력:"))
# num2=int(input("임의의 정수 입력:"))
# num3=int(input("임의의 정수 입력:")) 
# if num1<num2 :
#     num1=num2
# if num1<num3 :
#     num1=num3
# print(num1)



# print("두수를 입력받아 큰수가 짝수이면 출력")
# su1 = int(input("입력:"))
# su2 = int(input("입력:"))
# if su1 > su2 :
#      if su1 %2 == 0:
#       print(su1)
# if su1 < su2 :
#     if su2 %2 == 0:
#       print(su2)

# print("두수를 입력받아 큰수가 짝수이면 출력")
# su1 = int(input("입력:"))
# su2 = int(input("입력:"))
# if su1 > su2 and su1 %2 == 0: print("%d는 큰수이면서 짝수이다."%su1)
# if su2 > su1 and su2 %2 == 0: print("%d는 큰수이면서 짝수이다."%su2)


# print("두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력")
# su1 = int(input("1.입력:"))
# su2 = int(input("2.입력:"))
# if (su1+su2) %2 == 0 :
#     if (su1+su2) %3 == 0 :
#         print((su1+su2),"는 짝수이며 3의 배수이다")


# print("두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력")
# su1 = int(input("임의의 정수 입력:"))
# su2 = int(input("임의의 정수 입력:"))
# sum_=su1+su2
# if sum_ %2 == 0 : and sum_ %3 == 0 :
#         print("두수의 합은 %d이고 짝수이며 3의 배수이다"%sum_)


# num=int(input("수 입력 :"))
# if num == 1:
#     print("1입력")
# else:
#     print("1이 아닌 값 입력")


# arr = [1,2,3,4,5,]
# na = int(input("찾는 숫자 입력:"))
# if na in arr:
#     print("arr:",arr."찾는 숫자가 존재 합니다.:", na)
# else:
#     print("arr:",arr."안에는 찾고자하는 숫자가 없습니다.:", na)
# print('결과:',na in arr)


# st = "Hello Python Fun"
# na = input("찾고자 하는 문자열 입력:")
# if na in st :
#     print("st:",st,"찾는 문자열:",na,"존재한다.")
# else:
#     print("st 안에는 ",na,"존재하지 않습니다.")

# old_id = input("저장할 ID 입력 :")
# print("인증프로그램 입니다")
# print("ID와 PW를 입력하세요")
# new_id = input("ID 입력 :")
# if old_id == new_id :
#     print("인증을 통과 했습니다")
# else:
#     print("인증실패")

# num=int(input("수 입력:"))
# if num %3 ==0:
#     if num %2 ==0:
#         print("num은 3의 배수면서 짝수 입니다.")
# print("다음문장 실행")


# num=int(input("수 입력:"))
# if num %3 ==0: and num %2 ==0:
#  print("%d은 3의 배수면서 짝수 입니다."%d)
# print("다음문장 실행")

# num =int(input("수 입력:"))
# if num > 0:
#     if num %2 == 0:
#         print("num은 양의 짝수입니다")
#     else:
#         print("num은 양의 홀수입니다")
# else:
#     print("num은 음수입니다")
# print("다음문장 실행")



# *다시 하기
# gb=int(input("Gbyte 입력:"))
# sel = int(input("1.byte 2.Kbyte 3.Mbyta \n>>>"))
# if sel ==1 :
#     print(gd,"Gbyte:",gb*1024*1024*1024, "byte" )
# if sel ==2 :
#     print(gd,"Gbyte:",gb*1024*1024*, "Kbyte" )
# if sel ==3 :
#     print(gd,"Gbyte:",gb*1024, "Mbyte")



# old_id = input("저장할 ID 입력 :")
# new_id = input("ID 입력 :")
# old_pw = input("저장할 PW 입력:")
# new_pw = input("PW 입력:")

# if old_id == new_id and old_pw == new_pw :
#     print("인증을 통과 했습니다")
#     if old_id == new_id:
#         print("인증 통과")
#     else :
#         print("등록되지 않은 아이디 입니다.")
#     if old_pw == new_pw :
#         print("비밀번호가 일치합니다.")
#     else :
#         print("비밀번호가 틀립니다.")

# else:
#     print("인증을 실패했습니다.")



# old_id = input("저장할 ID 입력 :")
# old_pw = input("저장할 PW 입력:")
# print("인증할 id 와 pw를 입력하세요.")
# new_id = input("ID 입력 :")
# new_pw = input("PW 입력:")
# if old_id == new_id :
#     if  old_pw == new_pw :
#         print("인증 통과")
#     else : 
#         print("인증번호가 틀렸습니다.")
# else :
#     print("인증번호가 ")

# old_id = input("저장할 ID 입력 :")
# old_pw = input("저장할 PW 입력:")
# print("인증할 id 와 pw를 입력하세요.")
# new_id = input("ID 입력 :")
# if old_id == new_id :
#     new_pw = input("PW 입력:")
#     if  old_pw == new_pw :
#         print("인증 통과")
#     else : 
#         print("인증번호가 틀렸습니다.")
# else :
#     print("인증번호가 틀렸습니다. ")

# num = int(input("수 입력:"))
# if num > 100:
#     print("100보다 큰수 입력")
# elif num > 50:
#     print("50보다 큰수 입력")
# elif num > 0:
#     print("0보다 큰수 입력")
# else:
#     print("그 외의 값 입력")

# name = input("이름:")
# num = input("학번:")
# su1 = int(input("과목1:"))
# su2 = int(input("과목2:"))
# su3 = int(input("과목3:"))
# sum_= su1+su2+su3
# avg= sum_/3
# if avg >= 90:
#     print("A")
# elif avg >= 80:
#     print("B")
# elif avg >= 70:
#     print("C")
# elif avg >=60:
#     print("D") 
# else:
#     print(f)   

cof=int(input())
cof1= cof*2000
cof2= cof1 - (cof-10)*500
if cof > 9 :
    print ("%d원"% cof2)


     