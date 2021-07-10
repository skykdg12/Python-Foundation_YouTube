def profile(name, age, main_lang):
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}".format(name,age,main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

#같은 학교 학년 반 수업

def profile(name, age = 17, main_lang = "파이썬"):#기본 값을 입력하면 기본값이 없는 name만 입력해도 나머지 자동 출력
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}".format(name,age,main_lang))

profile("유재석")