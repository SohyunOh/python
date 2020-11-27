# num={1:"일",2:"이" ,3:"삼", 4:"사", 5:"오"}

# print("변경전 값:",num)
# print()
# print("num.setdefault(9):",num.setdefault(9,"구~우"))
# print()
# print("변경 후:",num)
# print()
# print("num.get(9번쨰)value:",num.get(9))


# setdefault =통계같은 중요자료에 없으면 추가할수 있음.


# num={1:"일",2:"이" ,3:"삼", 4:"사", 5:"오"}
# aaa={6:"육",7:"칠", 8:"팔"}

# print("updatew 전 num:",num)
# num.update(aaa)

# print("update 후 num:" ,num)



# dic = {}
# ls=[]

# ls.append(input("등록할 키값 입력:"))
# ls.append(input("등록할 키값 입력:"))
# ls.append(input("등록할 키값 입력:"))

# dic =dic.fromkeys(ls)
# print("dic 키 설정:",dic)

# dic =dic.fromkeys(ls,0)
# print("dic 키&값 설정:",dic)



# num={1:"일",2:"이" ,3:"삼", 4:"사", 5:"오"}


# print("pop 전  num:", num)
# print("\npop(3) 실행  num:" , num.pop(3))
# print("\npop 실행 후 num:" , num)

# # pop 키값을 찾아서 벨류값을 지움
# pop() 키값을 비워두면 결과 안나옴. 딕션러리는 순서가 없기에 마지막 값을 찾지 모삼



# info= {}; pe=[]; bl=True ; num=0
# while bl:
#     print("1.인적사항등록"); print("2.검색"); print("3.종료")
#     num= int(input(">>>"))
#     if num==1:
#         pe.append(input("이름 입력:")); pe.append(input("점수 입력:"))
#         inpo[pe[0]]= pe[1]
#     elif num ==2:
#         name= input("찾고자하는 학생 이름 입력:")
#         if info.get(name)==Noen: print("찾고자 하는 학생이 없습니다..")
#         else:
#             print(name,"님의 점수:", inpo.get(name))
#     elif num==3 :
#         print("프로그램 종료합니다.")
#         bl= False



# info= {}; pe=[]; bl=True ; num=0
# while bl:
#     print("1.인적사항등록"); print("2.검색"); print("3.종료")
#     num= int(input(">>>"))
#     if num==1:
#         pe.append(input("이름 입력:")); pe.append(input("점수 입력:"))
#         info[pe[0]]= pe[1]
#         print(pe)
#         print(info)  #리스트는 늘어나지만 딕셔너리는 늘어나지 않음.
#     elif num ==2:
#         name= input("찾고자하는 학생 이름 입력:")
#         if info.get(name)==None: print("찾고자 하는 학생이 없습니다..")
#         else:
#             print(name,"님의 점수:", info.get(name))
#     elif num==3 :
#         print("프로그램 종료합니다.")
#         bl= False
#     pe=[] #pe.clear()




#*Set(집합) : 중복허용 안함, 구성요소 모두를 포함함.


# names = {'허준', '신사임당', '권율', '홍길동','허준'}

# print(type(names))
# print(len(names))
# print(names)


# # 내장함수
# s=set({}) #s={} 초기화는 s=set({}) 
# print(type(s))

# print(set('programming'))
# print(set([12,15,17,11,15]))

# dic = {'a':1,'b':2,'c':3} #키값만 잡음(키값은 중복허용x)
# print(set(dic))

# for x in {'가','나','다','라'}:
#     print(x #수집 목적용 함수 

# asia ={'korea','china', 'japan'}
# print()

# asia.add('thailand')
# print(asia)
# asia.add('china')
# print(asia)
# asia.remove('japan')
 
# print(asia)

# asia ={'korea','china', 'japan'}
# print(asia)
# asia2= {'iraq','singapore', 'korea'}
# asia.update(asia2)
# print(asia)

# print('-'*40)

# asia={'korea','china', 'japan'}
# asia2= {'iraq','singapore', 'korea'}
# asia3=asia+asia2
# print(asia3)

'''
*집합의 연산
1.합집합(|): 두 집합의 전체 요소들의 모음.
2 교집합(&) : 두집합의 공통요소들의 모음
3.차집합(-) : 왼쪽 집합의 요소에서 오른쪽 집합의 요소를 제거
4.베타적 차집합(^) : 합집합-교집합
5.부분집합(<=): 왼쪽 집합이 오른쪽 집합의 부분집합인지의 여부 확인
6.진성집합 (<):부분 집합이면서 추가로 요소가 저 존재하는 확인

부분집합, 진성집합은 - True(해당), False(해당x)

부분집합과 진성집합의 차이는
부분집합일 경우 좌, 우 집합이 같아도 부분집합이다.
진성집합인 경우 좌, 우 집합이 모주 같은 경유 성립되지 않는다.
'''

# two = {2,4,6,8,10,12}
# three = {3,6,9,12,15}
# print('교집합',two % three)
# print('합집합',two | three)
# print('차집합',two -three)
# print('베타적 차집합',two^three)


# animal ={'호랑이','사자', '강아지', '치타','햄스터','고양이'}
# pet={'강아지','고양이', '햄스터'}

# print(pet <= animal)
# print(pet <= pet)

# print(pet < animal)
# print(pet < pet)




# #문자열
# Str = 'Have a nice day'

# print("Str[0] : ",Str [0])
# print("Str[1] : ",Str [1])
# print("Str[2] : ",Str [2])
# print("Str[3] : ",Str [3])
# print()
# print("문자열의 총 길이 : ",len(Str))
# print("Str: ",Str)

# for i in Str:
#     print(i, end='')
# print()
# # 인덱스를 이용한 반복문
# for i in range(len(Str)):
#     print(str[i],end='')
# print()


# Str = 'Have a nice day'
# arr = Str[7:11]
# print("Str:",Str)
# print("arr:",arr);
# print(Str[7:])
# print(Str[:6])

# Str = "즐거운 파이썬"
# # 한글바이트 지만, 인덱스는 1로 인식
# print("Str\t:",Str)
# print("Str[0]\t:",Str[0])
# print("Str[1:3]:",Str[1:3])
# print("Str[3:]:",Str[3:])
# print("Str[:3]:",Str[:3])

# Str ='Have a'
# print("변경 전 Str:", Str)

# Str += 'nice day'

# print("변경 후 Str:",Str)
# print("="*27)
# print("Str*3:",Str*3)

'''
문자열 함수
upper()         소문자를 대문자로 변경                     str.upper()
lower()         대문자 소문자 변경                         str.lower()
swapcase()      문자 상호 변경                             str.swapcase()
tltle()         각 단어의 제일 앞 글자만 대문자로 변경      str.title()
'''


# Str= 'Pythone is Easy , 그리고 grogrmming 할만하다^^'
# print("Str:", Str)
# print()
# print('Str.upper():', Str.upper())#소문자를 대문자로 변경  
# print()
# print('Str.lower():',Str.lower())#대문자 소문자 변경  
# print()
# print('Str.swapcase():' ,Str.swapcase())#문자 상호 변경   
# print()
# print('Str.title():', Str.title())#각 단어의 제일 앞 글자만 대문자로 변경

# st ='NerEr -eVer 110giVe up'
# st =st.title()
# print(st)

# #문자열찾기
# Str.count('문자열') 찾는 문자열의 개수
# Str.find('문자열') 찾는 문자열의 위치가 없으면-1
# Str.rfind('문자열') 맨 끝쪽부터찾는다 없으면-1
# Str.index('문자열') find() 동일용도, 없으면 error

st = 'Have a nice day'
print("st:",st)
print()
print("st안에 'a'문자열 개수:", st.count('a'))
print("st안에 'day'문자열 개수:", st.count('day'))
print("st안에 'dak'문자열 개수:", st.count('dak'))
print(st.count('')) #16개 널문자포함









