# print(123+123)
# print(542-242)
# print(2*123)
# print(120/3)
# print("120/3")

# print("덧셈 결과:",123+123)
# print("빼셈 결과:",54-242)
# print("곱셈 결과:",2*123)
# print("나눗셈 결과:",120/3)
'''
 print("12+54=",12+54,"입니다.")
 print("268-42=",268-42,"입니다." )
 print("2*23=",2*23,"입니다.")
 print("120/3=",120/3,"입니다.")
'''

"""
진범    범위    표현식  사용예
2진수   0,1     0b      0b0100 0001 #파이썬만 0b를 붙여서 표시 
8진수   0~7     0o      0o101
10진수  0~9             65
16진수  0~9,A~F 0x      0x41
"""

# print(0b01111011)
# print(0o173)
# print(0x7b)
# print(123)

# print("2진수:",bin(0b01111011))
# print("8진수:",oct(0b01111011))
# print("16진수",hex(0b01111011))
# print("10진수",0b0111011)

# print("%d"%123)
# # print("%d%d"%132)
# # print("%d"%(123,321))
# print("%d%d"%(123,321))
# print("%d+%d=%d"%(132,321,123+321))

# print("10진 정수:%d"%123)
# print("10진 정수:%d"%0o173)
# print("10진 정수:%d"%0x7b)

# print("8진정수:%o"%123)
# print("8진정수:%o"%0o173)
# print("8진정수:%o"%0x7b)

# print("16정수:%x"%123)
# print("16정수:%x"%0o173)
# print("16정수:%x"%0x7b)

# print("정수 표현:%d"%123)
# print("정수 표현:%d"%123.132)
# print("정수 표현:%d%d"%(123,456))

# print("\n 실수 표현:%f"%456)
# print("실수 표현:%f"%456.456)
# print("실수 표현:%f%f"%(456.456,123.123))


# print("문자 표현:%c%c"%("한","글")) #%C(c언어에서는 문자상수(아스키코드)로 호출해 사용됨)
# # print("문자 표현:%c%c"%(A,a)) #변수이기에 따움표 표시가 안되어있기에 변수로 작용
# print("문자 표현:%s%s"%('A','a'))
# print("문자 표현:%c%c"%(97,65))

# # 참거짓
# # print("문자 표현:%d%d"%(,))
# # print("문자 표현:%s%s"%(,))


# print("문자 표현:%c%c"%('표','현'))
# print("\n 문자열 표현 :%s"%"안녕")
# print("문자열 표현:%s\t%s"%("문자열",'표현방식'))


# # ******
# print("기본 값:%d"% 123)
# print("설정 값:%5d"% 123) #양숫자는 우측 정렬가능 , 칸확보를 무시함.(\t는 8칸확보)
# print("설정 값:%05d"% 123) #확보된 숫자공간에 0으로 채움
# print("설정 값:%5d%5d"% (123,123))
# print("설정 값:%-5d%-5d"% (123,123))#(-05d 는 존재하지 않음. 숫자 단위가 바뀜)


# print(" 기본 값:%f"%123.45678)
# print("설정 값:%10.3f"%123.45678)
# #실수 호출 소수점을 포함한 전체 칸 확보 
# print("설정 값:%2.1f"%123.45678)
# print("설정 값:%.2f"%123.45678) #앞 정수부분은 확보안하고 수소 몇자리확보


# print("12345678901234567890123456789012345678901234567890123456789012345678901234567890")
# print("%10s%10s"%("대한","민국")) #버그 존재 / 한글은 \t로 공간확보 추천 
# print("기본 값:%s"%"python test")
# print("설정 값:%20s"%"python test")

#========출력결과========
print("이름\t:%s"%"홍길동" )
 #print("이름\t:%c%C%C"%"홍","길","동" )
 # print("%-5s%-10s"%("이름",':홍길동'))  
print("나이\t:","20")
print("나이\t:%d"%20) 
print("나이\t:%s"%20)
print("tel\t :%03d%c%d%c%d"%(10,'-',1234,'-',1234))
print("키\t:%2.1F" %178.5) #문자열로 %s로 바꾸는 방법
 #print("키\t:%.1F" %178.5) 
print("몸무게\t:%d"%75)
print("혈액형\t:%d"%0)
        ### print("tel\t :%03d%c%d%c%d"%(10,'-',1234,'-',1234))
        #print("tel\t:%s"% "010-1234-1234")


#========출력결과========
print("이름\t:%s"%"홍길동" )
 #print("이름\t:%c%C%C"%"홍","길","동" )
 # print("%-5s%-10s"%("이름",':홍길동'))  
print("나이\t:","20")
print("나이\t:%d"%20) 
print("나이\t:%s"%20)
print("tel\t :%03d%c%d%c%d"%(10,'-',1234,'-',1234))
print("tel\t :0%s-%s-%s"%(10,1234,1234))
print("키\t:%2.1F" %178.5) #문자열로 %s로 바꾸는 방법
 #print("키\t:%.1F" %178.5) 
print("몸무게\t:%d"%75)
print("몸무게\t:%s"%75) 
print("혈액형\t:%d"%0)
print("혈액형\t:%s"%0)
        ### print("tel\t :%03d%c%d%c%d"%(10,'-',1234,'-',1234))
        #print("tel\t:%s"% "010-1234-1234")


