# result1=0
# def add1(n):
#     global result1
#     result1 +=n
# def sub1(n):
#     global result1
#     result1 -=n
# result2=0
# def add2(n):
#     global result2
#     result2 +=n
# def sub2(n):
#     global result2
#     result2 -=n
# add1(8)
# add1(19)
# sub2(15)
# print("1번 계산기 계산결과 : %d"% result1)
# print("2번 계산기 계산결과 : %d"% result2)

# class Calculator: #클래스는 함수랑 구분을 위해 대문자로 해주고 :으로 종속시켜주기
#     result =0
#     def add(self,n): #함수 - (매개변수)
#         self.result+=n
#     def sub(self,n):
#         self.result-=n
# cal1=Calculator() 
# cal2=Calculator() 
# cal3=Calculator() 
# cal1.add(19)
# cal1.sub(5)
# cal3.add(56)
# cal3.sub(27)
# print("1번 계산기 계산결과 : %d"% cal1.result)
# print("2번 계산기 계산결과 : %d"% cal2.result)
# print("3번 계산기 계산결과 : %d"% cal3.result)


# class Calculator: 
#     result =0
#     def add(self,n):
#         self.result+=n
#     def sub(self,n):
#         self.result-=n
# cal1=Calculator() 
# cal2=Calculator() 
# cal3=Calculator() 
# cal1.add(19)
# cal1.sub(5)
# cal3.add(56)
# cal3.sub(27)
# print("1번 계산기 계산결과 : %d"% cal1.result)
# print("2번 계산기 계산결과 : %d"% cal2.result)
# print("3번 계산기 계산결과 : %d"% cal3.result)
# print(type(cal1)); print(type(cal2)); print(type(cal3))

# class Person:
#     name= 'Hong Kil Dong'
#     gender = 'male'
#     address = 'sroul'

#     def set_name(self,name):
#         self.name = name
#     def print(self):
#         print('my nsme is{0}'.format*(self.name))

# p1=Person()
# p2=Person()
# p3=Person()
# p3.gender='female'
# p1.name= "hong kildong"
# print("p1's name is",p1.name)
# print("p2's name is",p2.name)
# print("p2's name is",p3.gender)
# print(p1,print())
# print(p2,print())

# class Calculator:
#     def setting(self,color,n1,n2):
#             self.color= color
#             self.n1 =n1
#             self.n2= n2
#     def add(self):
#         result=self.n1+self.n2
#         return result
# red_calc= Calculator()
# blue_calc= Calculator()
# red_calc.setting('빨강색',15.5)
# blue_calc.setting('파랑색',20.15)
# print("파랑계산기 색깔 (self.color):",blue_calc.color)
# print("빨강계산기 색깔 (self.color):",red_calc.color)
# print("파랑계산기 덧셈결과(self.color):",blue_calc.add())
# print("빨강계산기 덧셈결과(self.color):",red_calc.add())

# 생성자 ======================================================

# class Account:
#     def __init__ (self,bank):
#         self.balance=0
#         self.bank=bank        
#     def gat_balance(salf):
#         return self.balance
#     def deposit(self,money):
#         self.balance += money 
#     def withdraw(self,money):
#         self.balance -= money 

# if __name__ == '__main__':
#     woori = Account('우리은행')
#     woori.deposit(15000)
#     print ('%s 잔액: %d원'% (woori.bank,woori.gat_balance()))

# 상속===================================================

# class player :
#     def __inif__ (self, user_id): #생성자  , 모두 초기화 
#         self.user_id=user_id
#         self.level=1
#         self.hp=50
#         self.atk=3
#         self.exp=0
#     def info(self):
#         print('\n========캐릭터 정보 ========')
#         print('아이디', self.user_id)
#         print('레벨', self.level)
#         print('공격력',self.atk)
#         print('경험치',self.exp)
#         print('체력',self.hp)
#         print('============================')
# if __name__ == '__main__':

#     class Healer(player):
#         def heal(self):
#             pass
#     class Tanker(player):
#         def tank(self):
#             pass
#     P1=Healer('아처')
#     P2=Tanker('워리어')
#     P1.info()
#     P2.info()
# else:
#     class Healer(player):
#         def heal(self):
#             pass
#     class Tanker(player):
#         def tank(self):
#             pass
#     P1= Healer('archer')
#     P2= Tanker('warrior')
#     P1.info()
#     P2.info()

# 예외처리==========================================================================================

# n1=10
# n2=0
# try :
#     result=n1/n2
#     print("%d/%d=%d "% (n1,n2,result))
# except:
#     print("0으로 나눌 수 없습니다.")
# print("프로그램 정상 종료!!")

# n1=10
# n2=0
# result=n1/n2
# print("%d/%d=%d "% (n1,n2,result))
# print("0으로 나눌 수 없습니다.")
# print("프로그램 정상 종료!!")
# #ZeroDivisionError =0으로 나눌수 없기에 나는 에러 

# while True:
#     try :
#         n1=int(input('정수1:'))
#         n2=int(input('정수2:'))
#         break
#     except:
#         print('숫자로만 입력하세요~') #예외 처리 
#     # print("%d/%d=%d "% (n1,n2,result))
# try: 
#     result=n1/n2
#     print("%d/%d=%d "% (n1,n2,result))
# except:
#     print("0으로 나눌 수 없습니다.")
# print("프로그램 정상 종료!!")

# s=input('정수:')
# try:
#     point = int (s)
#     print(150/point)
# except ValueError:
#     print('숫자로만 입력하세요')
# except ZeroDivisionError:
#     print('0으로 나눌수 없습니다.')
# except:
#     print('알수 없는 오류 발생.점검 후 조치하겠습니다.')
# print("프로그램 정상 종료!!")
# ==========================

# pet=['거북이','타란튤란', '전갈']
# for i in range(4):
#     try:
#         print(pet[i],"키울래용!")
#     except:
#         print("애완동물의 정보가 없습니다.")
#     finally:#예외처리 (에러)와 상관없이 꼭 실행되야 하는경우
#         print('IT수업은 상준샘과 함께~~~')
# print("프로그램 정상 종료!!")

'''
웹 크롤링
'''


















