abs = [2, 5]
nob = [7]
for stu in range(1, 11):
    if stu in abs:
        continue #결석한 학생들이 있더라도 건너뛰어서 다음 학생까지 진행
    elif stu in nob:
        print("오늘 수업 여기까지 {0}는 교무실로 따라와".format(stu))
        break #책이없는 학생이 발생시 이후 남은 학생이 있어도 진행하지 않음
    print("{0}, 책을 읽어봐".format(stu))