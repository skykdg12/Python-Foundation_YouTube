# import sys
# print("python", "java", file=sys.stdout) #로그에 표준으로 출력
# print("python", "java", file=sys.stderr) #로그에 에러로 출력

# #시험 성적
# scores = {"수학":0, "영어":50, "코딩":100} #딕셔너리 구성
# for subject, score in scores.items(): #키와 밸류에 스코어의 키밸류 값들 입력
#     # print(subject, score)
#     print(subject.ljust(4), str(score).rjust(4), sep=":") #문자 왼쪽 오른쪽에 숫자 만큼의 공간 확보, sep은 빈공간에 들어갈 문자, end는 마지막에 들어갈 문자

#은행 대기순번표
#001, 002, 003, ...
# for num in range(1, 21): #num에 숫자 범위 설정
#     print("대기번호 : " + str(num).zfill(3)) #num이 숫자이기 때문에 str을 써서 문자로 변환, zfill의 숫자만큼 자릿수를 출력하고 빈값은 0으로 출력

answer = input("아무값이나 입력하세요 : ")#input으로 입력된 값은 항상 str으로 인식됨
print("입력하신 값은 " + answer + "입니다")