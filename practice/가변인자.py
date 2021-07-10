# def Profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)

def Profile(name, age, *lang):# *표를 이용해서 lang 갯수와 상관없이 출력가능
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
    for i in lang:
        print(i,end=" ")
    print()

    
Profile("유재석", 20, "python", "java", "c", "c#", "c++", "javs")
Profile("김태호", 25, "kotlin", "swift", "", "", "")