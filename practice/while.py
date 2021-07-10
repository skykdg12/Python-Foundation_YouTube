# cus = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(cus,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다")

# cus = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(cus,index))
#     index += 1

customer = "토르"
person = "Unknown"

while person!= customer : #c와 p가 같지 않을경우
    print("{0}, 커피가 준비되었습니다".format(customer)) #c 호출
    person = input("이름이 어떻게 되세요?") # p에 인풋 값을 물어보고 c와 같은 p가 나올때 까지 반복