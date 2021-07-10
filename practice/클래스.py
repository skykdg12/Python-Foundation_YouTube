# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다 공격력 {2}".format(name, location, damage))
    

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

class Unit: #클래스 생성
   def __init__(self, name, hp, damage): # 클래스 안에 항목들 입력
       self.name = name # 항목들 설정
       self.hp = hp
       self.damage = damage
       print("{0} 유닛이 생성 되었습니다".format(self.name))
       print("체력 {0}, 공격력{1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # Unit 클래스에 맞는 각자의 유닛들 생성 가능
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
