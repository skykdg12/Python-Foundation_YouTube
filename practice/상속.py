# 일반 유닛
class Unit: 
   def __init__(self, name, hp): 
       self.name = name 
       self.hp = hp
 
# 공격 유닛      
class AttackUnit(Unit): # Unit 클래스를 받아옴
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # Unit 클래스의 내용을 가져옴
        self.damage = damage # Unit 클래스의 없는 내용 추가 

    def attack(self, location): 
        print("{0} : {1} 방향으로 적군을 공격 합니다 공격력 {2}"\
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage)) 
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp)) 
        if self.hp <=0: 
            print("{0} : 파괴되었습니다".format(self.name,))

firebat1 = AttackUnit("파이어뱃", 50, 16) 
firebat1.attack("5시") 

firebat1.damaged(25) 
firebat1.damaged(25)

