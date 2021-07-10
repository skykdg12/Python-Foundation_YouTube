import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":40, "취미":["축구" ,"골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # 프로필에 있는 정보를 파일에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file 에 있는 정보를 프로필에 불러오기
print(profile)
profile_file.close()