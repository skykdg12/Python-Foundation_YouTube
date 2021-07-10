class Unit: 
   def __init__(self, name, hp, damage): 
       self.name = name # 클래스 내에서 정의된 변수를 멤버변수라고 한다
       self.hp = hp
       self.damage = damage
       print("{0} 유닛이 생성 되었습니다".format(self.name))
       print("체력 {0}, 공격력{1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5) 
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # Unit 클래스를 사용후에 클래스 외부에서 내용을 추가 할 수도 있음

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name))