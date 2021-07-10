class Unit: 
   def __init__(self, name, hp, damage): # init은 생산자의 역할, 셀프 빼고 init함수에 포함된 갯수만큼 정보를 입력해줘야함
       self.name = name 
       self.hp = hp
       self.damage = damage
       print("{0} 유닛이 생성 되었습니다".format(self.name))
       print("체력 {0}, 공격력{1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # 클래스로 부터 만들어지는 것을 객체라 표현
marine2 = Unit("마린", 40, 5) # 이런것들을 유닛클래스의 인스턴스라고 함
tank = Unit("탱크", 150, 35)
# marine3 = Unit("마린", 40) # 이런식으로 하면 오류가 뜸