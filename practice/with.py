# import pickle

# with open("profile.pickle", "rb") as profile_file: # 프로필에 있는 내용을 프로필 파일로 입력
#     print(pickle.load(profile_file)) # 입력된 프로필 파일 프린트

# with open("study.txt", "w", encoding="utf8") as study_file: # 스터디에 있는 내용을 스터디 파일로 입력
#     study_file.write("파이썬을 열심히 공부하고 있어요") # 스터디파일에 내용 입력

with open("study.txt", "r", encoding="utf8") as study_file: # 스터디 파일에 입력된 내용 읽기
    print(study_file.read())