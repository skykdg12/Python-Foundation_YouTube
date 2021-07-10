class Unit: # Unit 생성 클래스
   def __init__(self, name, hp, damage): 
       self.name = name 
       self.hp = hp
       self.damage = damage
       print("{0} 유닛이 생성 되었습니다".format(self.name))
       print("체력 {0}, 공격력{1}".format(self.hp, self.damage))
       
class AttackUnit: # 공격 유닛 생성 클래스
    def __init__(self, name, hp, damage): 
        self.name = name 
        self.hp = hp
        self.damage = damage

    def attack(self, location): # 메소드 앞에서는 항상 self를 작성해야한다
        print("{0} : {1} 방향으로 적군을 공격 합니다 공격력 {2}"\
              .format(self.name, location, self.damage))
        
    def damaged(self, damage): # 공격받는 함수 생성
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage)) # 받은 데미지 표시
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp)) # 남은 체력 표시
        if self.hp <=0: # 체력이 0이하면 파괴
            print("{0} : 파괴되었습니다".format(self.name,))

firebat1 = AttackUnit("파이어뱃", 50, 16) # 공격 유닛 생성
firebat1.attack("5시") # 생성한 공격 유닛을 5시 방향으로 공격

firebat1.damaged(25) # 공격 받은 유닛
firebat1.damaged(25)

