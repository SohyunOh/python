# st = 'Have a nice day'
# print("st[0]:",st[0])
# print("st[1]:",st[1])
# print("st[2]:",st[2])
# print("st[3]:",st[3])
# print()
# print("문자열의 총 길이: ", len(st))
# print("st:",st)

# for i in range(st):
#     print(i,end="")


# st = 'Have a nice day'
# print("st:",st)

# print("find: 'day'위치 :", st.find('day'))
# print("index: 'day'위치 :", st.index('day'))
# print("find: 'day'위치 :", st.find('kkk')) # 찾지 못했을 경우 : -1
# print("index: 'day'위치 :",st.index('kkk'))# : 벨유 에러


# st = 'Have a nice day'
# print("st:",st)

# print("find: 'day'위치 :", st.find('a')) #제일 첫번쨰 값만 찾음
# print("find: 'day'위치 :", st.find('a',2)) #2번(인덱스) 부터 찾아줘
# print("find: 'day'위치 :", st.find('a',6)) 
# print("find: 'day'위치 :", st.find('a',14)) 


st = 'Have a nice day Have a nice day Have a nice day'

# for i in range(len(st)) :
#     print(st.find ('a',i))

# Sum=0
# i=0
# while i < len(st):
#     st(i)=st.find('a',i)
#     Sum+=i
#     i+=1
#     print(i,end="")

# loc=0
# ls=[]
# while True :
#     loc=st.find ('a',loc)
#     if loc != -1:
#         ls.append(loc)
#         loc+=1
#     else:
#         break
# print("a문자의 개수 : %d" % st.count('a'))
# print("a문자의 위치 :",ls)

# loc=0
# ls=[]
# while True:
#     loc = st.find ('a',loc) #상수 x, 변수 로 적용 
#     if loc != -1 :
#         ls.append (loc)
#         loc+=1
#     else:
#         break
# print(st.count('a'))
# print(ls)


# 문자열 변경 함수 
# strip : 양쪽 제거  Str.strip() or Str.st.strip('문자열')


# st='    파 이 썬    '
# print('st\t\t:{}{}{}'.format('*',st,'*'))    
# print('')
# print('st.strip()\t:{}{}{}'.format('*',st.strip(),'*'))

# st='파이썬파'

# print('st\t\t:',st)
# print()
# print('Str.srtip("파")\t:', st.strip('파'))
# print("==========================================")

# st='파이썬'
# print('st\t\t:',st)
# print()
# print('Str.srtip("파")\t:', st.strip('파'))

# st='파이썬파파파파파'
# print('st\t\t:',st)
# print()
# print('Str.srtip("파")\t:', st.strip('파'))
# #지정된 문자가 연속적이면 다 날림


# st='---파---이---썬---'

# print('st\t\t:',st)
# print('st.srtip("-")\t:', st.strip('-'))

# print('st.rsrtip("-")\t:', st.rstrip('-'))

# print('st.lsrtip("-")\t:', st.lstrip('-'))


# st='2015/04/02'

# print('st\t\t:',st)
# print('replace()\t:',st.replace('/','.'))
# print('replace([0:4])\t:',st.replace(st[0:4],'2017')) #슬라이씽 활용  ,

# print(st.replace('2015/','15/')


# st="""
# 오늘 하루도 즐겁게
# 오늘 하루도 행복하게
# 오늘 하루도 최선을
# """
# print(st)

# # 여러줄을 묶어서 문자열 표현할때는 """ 로 표현 ,"는 한줄만 해당





st="""
김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월 14일
"""
# -를:로 변경 / 년도를 모두 1999년 변경

# print(st.replace('-',':'))
# print(st.replace('2017','1999'),st.replace('2015','1999'),st.replace('2018','1999'))
# print(st.replace(st[6:10],'1999'))
# print(st.replace(st[27:31],'1999'))
# print(st.replace(st[47:51],'1999'))

# st=st.replace('-',':')
# # print(st)
# loc=0
# while True:
#     loc=st.find('년',loc)
#     if loc != -1:
#         st.replace(st[loc-4:loc] ,'1999')
#         loc+=1
#     else:
#         break
# print(st)


# for i in range(st.count(':')):
#     loc=st.find(':',loc+1)
#     # print(loc)
#     st=st.replace(st[loc:loc+5],'1999')
#     print(st)

# for i in range(st.count(':')):
#     loc=st.find(':',loc)
#     # print(loc)
#     st=st.replace(st[loc+1:loc+5],'1999')
#     print(st)

# 문자열 변경
# Str.split() or Str.split('문자')
# Str.splitlines()
# Str.join('문자')

# st= 'Never ever give up'
# print('st\t\t:',st)
# print('st.split()\t:', st.split())
# 공백단위로 분리, 단어만 추출


# st='하나:둘:셋'

# print('st\t\t:',st)
# print('st.split(:)\t:', st.split(':'))

# st='일,이,삼'
# print('st\t\t:',st)
# print('st.split(,)\t:', st.split())
# sprit 함수는 기본적으로 공백을 기준으로 리스트를 만듬
# ()특전 문자나 기호를 지정하면 그 특정문자를 기분으로 분리한다.
# 특정문자를 지정하지 않은 상태에서 문자열에 공백이 존재하지 않은 경우
# 리스트 하나의 구성요소로 리스트가 만들어진다.

# st= 'Never ever give up'
# print('st:',st)
# print('st.splitlines():',st.splitlines())
# st=''' Never ever give up
# Never ever give up
# '''

# print('st.splitlines():',st.splitlines())
# st="\n하나\n둘"
# print('st.splitlines():',st.splitlines())


Str='123'
print('"%".join(132)\t:.','%'.join (Str))
print('123.join ("%a")\t:', Str.join('%a'))

li=['','132','456']
print('"공백".join([123,456])\t:',"".join(li))
li= ['','안녕하세요','만나서반가습니다','행복하세요.']
print('"엔터".join(li)\t', "\n\n".join(li))

# a.join (b) => b의 구성요소사이에 a를 삽입 
# [b는 구성요소를 갖는 성격의 데이터 예>이스트,튜플,딕셔너리,문자열]


# # 문자열 정렬
# Srt.center(정수) or Srt.center(정수, 값)
# ljust(정수)
# rjust(정수)


Str='python'
print('Str\t\t:',st)
print('Str.center(10)\t:',Str.center(10))
print('Str.center(10,"-")\t:',Str.center(10,'-'))

print('Str.ljust(10)\t:',Str.ljust(10),Str.ljust(10))
print('Str.rjust(10)\t:',Str.rjust(10),Str.rjust(10))
print('Str.zfill(10)\t:',Str.zfill(10))




