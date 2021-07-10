def profile(name, age, main_lang):
    print(name,age, main_lang)
    
profile(name="유재석", main_lang="파이썬", age = 20)#순서가 달라도 함수에 정해진 순서대로 출력됨
profile(main_lang = "자바", age=25, name="김태호")