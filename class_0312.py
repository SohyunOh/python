# 딕션너리


# student= {'학번':1234, '이름':'홍길동' ,'학과':'it학과'}
# print(student)

# mobile={ '품명': '갤럭시', '가격' :100, '크기':10}
# print(mobile)

# impo = {}
# impo['파이썬'] = 'www.python.org'
# impo['네이버'] = 'www.naver.com'
# impo['구글'] = 'www.google.com'

# print("파이썬:",impo['파이썬'])
# print("네이버:", impo['네이버'])
# print("구글:",impo['구글'])
# print(impo)


# impo={}
# name = input('키값 입력:')
# val=input('값 입력:')
# impo[name]=val


# impo={}
# for i in range(1,6,1):
#     name =input('이름(key) 입력:')
#     val=input('값(value) 입력:')
#     impo[name]=val
# print(name,":",impo[name])
# print(impo)


# overwatch={}
# for i in range(5):
#     name=input('이름(key) 입력:')
#     skil=input('기술명(skil) 입력:')
#     overwatch[name]=val
# print(name,":",overwatch[skil])
# print(impo)



# import collections
# #순서잇는 사전
# overwatch= collections.OrderedDict()
# i=0;name="";val=""
# for i in range(5):
#     name=input('이름(key) 입력:')
#     skil=input('기술명(skil) 입력:')
#     overwatch[name]=val
# print(overwatch)

# num={1:"일", 2:'이',3:'삼', 4:"사"}

# print('keys()키:', num.keys())
# print()
# print('values() rqkt:', num.values())

# **** 
# num={1:"일", 2:'이',3:'삼', 4:"사"}
# print("num.keys():",num.keys())
# print("list(num):",list(num))
# print('list(num.keys()):',list(num.keys()))
# print()
# print("num.values():",num.values())
# print("list(num.values()):", list(num.values()))


# singer ={}
# singer['이름'] =input("가수 이름 입력:")
# singer['구성원'] =input("인원 수 입력:")
# singer['대표곡'] =input("대표곡 입력:")

# for i in singer.keys():
#     print('%s:%s'% (i,singer[i]))

# menu={}; bl=True; num=0
# while bl:
#     print("1.메뉴등록"); print("2.메뉴별 가격 보기"); print("3.가격 수정"); print("4.종료")
#     num = int(input(">>>"))
#     if num ==1:
#         name =input("메뉴 입력:");menu[name] = input("가격 입력:")
#     elif num ==2:
#         for i in menu.keys():
#             print(i,":",menu[i])
#     elif num ==3:
#         for i in menu.keys():
#             name=input("수정할 목록 입력:"); menu[name] = input("수정 가격:")
#     elif num ==4:
#         print("프로그램 종료합니다.")
#         lb = False

# num={1:"일", 2:'이',3:'삼', 4:"사"}


# print(num)
# print("num.get(3):" ,num.get(3))
# print("num.get(9):" ,num.get(9))
# print("num.get(0):" ,num.get(0,'없음'))

# su= int(input("찾고자 하는 키 입력:"))
# if num.get(su) ==None:
#     print("값이 없습니다.")
# else:
#     print(num.get(su))

#======================================================================
# singer ={}
# singer['이름'] =input("가수 이름 입력:")
# singer['구성원'] =input("인원 수 입력:")
# singer['대표곡'] =input("대표곡 입력:")

# for i in singer.keys():
#     print('%s:%s'% (i,singer[i]))

# menu={}; bl=True; num=0
# while bl:
#     print("1.메뉴등록"); print("2.메뉴별 가격 보기"); print("3.가격 수정"); print("4.종료")
#     num = int(input(">>>"))
#     if num ==1:
#         name =input("메뉴 입력:")
#         if menu.get(name) != None:
#             print("이미 등록된 메뉴 입니다.")
#         else:
#             menu[name]= input("가격입력")
#     elif num ==2:
#         for i in menu.keys():
#             print(i,":",menu[i])
#     elif num ==3:
#         name=input("수정할 목록 입력:")
#         if menu.get(name) == None:
#             print("등록되지 않은 메뉴입니다.")
#         else:
#              menu[name] = input("수정 가격:")           
#     elif num ==4:
#         print("프로그램 종료합니다.")
#         lb = False

# =====================================
# 네비게이션 만들기
# 1.등록
# 2.목적지 수정
# 3.검색
# 4.종료

# menu={}; bl=True; num=0
# while bl :
#     print("1.등록"); print("2.목적지 수정"); print("3.검색"); print("4.종료")
#     num =int(input("선택:"))
#     if num ==1:
#         ad =input("등록:")
#         if menu.get(ad) != None:
#             print("이미 등록된 주소입니다.")
#         else:
#             menu[ad]= input("주소 등록:")
#     elif num == 2:
#         ad=input("수정 할 목적지 입력:")
#         if menu.get(ad) == None:
#             print("등록되지 않은 주소입니다.")
#         else:
#             menu[ad] = input(" 목적지 수정 : ")
#     elif num ==3:
#         for i in menu.keys():
#          print(i,":",menu[i])
#     elif num ==4:
#         print("종료")
#         bl = False


# =========================================================
# 풀이 답
# menu={}; bl=True; num=0
# while bl :
#     print("1.등록"); print("2.목적지 수정"); print("3.검색"); print("4.종료")
#     num =int(input(">>>"))
#     if num ==1:
#         ad =input("위치 등록:")
#         if menu.get(ad) != None:
#             print("이미 등록된 위치입니다.")
#         else:
#             menu[ad]= input("위치 등록:")
#     elif num == 2:
#         ad=input("수정 할 위치 입력:")
#         if menu.get(ad) == None:
#             print("등록되지 않은 위치입니다.")
#         else:
#             menu[ad] = input(" 수정 주소 입력: ")
#     elif num ==3:
#         ad=input("위치 검색:")
#         if menu.get(ad) == None:
#             print("등록되지 않은 목적지 입니다.")
#         else :
#             print("검색된 주소",menu.get(ad))
#     elif num ==4:
#         print("종료")
#         bl = False


# #/
# studeut = {'학번 ': 1234, '이름': '홍길동', '학과' : 'it학과'}

# print(studeut['학번'])
# print(studeut['이름'])
# print(studeut['학과'])
# print()
# print(studeut.items())
# print()
# print(studeut)    

name={'이순신': '거북선', '세종대왕':'훈민정음', '파이썬':'프로그래민 언어'}
for key,value in name.items(): #언패킹 활용
    print(key,":",value)

print("삭제:", name.clear())
print("삭제 후:", name)







