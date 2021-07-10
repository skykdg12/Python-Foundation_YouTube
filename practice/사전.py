cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5]) # 오류나고 다음 값 안나옴
# print(cabinet.get(5)) # get을 사용하면 none 출력후 다음 값 나옴
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# print(3 in cabinet)


cabinet = {"A=3":"유재석", "B-100":"김태호"}
print(cabinet["A=3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A=3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A=3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())


# 목욕탕 페점
cabinet.clear()
print(cabinet)