# score_file = open("score.txt", "w", encoding="utf8") # w는 쓰기전용
# print("수학 : 0", file=score_file) # 수학 점수 작성
# print("영어 : 50", file=score_file) # 영어 점수 작성
# score_file.close() # 파일 닫기

# score_file = open("score.txt", "a", encoding="utf8") # a는 내용 추가
# score_file.write("과학 : 80") # 과학 점수 추가
# score_file.write("\n코딩 : 100") # 코딩 점수 추가, 일반적인 프린트와 달리 엔터가 없기 때문에 코딩 앞에 \n추가
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # r은 읽기전용
# print(score_file.read()) # 스코어 파일 읽기
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # 파일이 총 몇줄인지 모를때 사용가능
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8") #리스트 형태로 만들어서 출력
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()