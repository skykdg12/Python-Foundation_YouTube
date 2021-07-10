# 일반 유닛
class Unit: 
   def __init__(self, name, hp): 
       self.name = name 
       self.hp = hp
 
# 공격 유닛      
class AttackUnit(Unit): # Unit 클래스를 상속받음
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

# 비행 기능
class Flyable: # 비행 기능 클래스 생성
    def __init__(self, flying_speed): # 비행 속도
        self.flying_speed = flying_speed
    
    def fly(self, name, location): # 비행 함수 생성
        print("{0} : {1} 방향으로 날아갑니다 [속도 {2}]"\
            .format(name, location, self.flying_speed))
        
# 공중 공격 유닛
class flyableAttackUnit(AttackUnit, Flyable): # 공격유닛과 비행기능 클래스 다중 상속
    def __init__(self, name, hp, damage, flying_speed): # 공격유닛과 비행기능 클래스에 입력한 인스턴스들 입력
        AttackUnit.__init__(self, name, hp, damage) # 공격유닛 클래스에 들어가는 인스턴스 지정
        Flyable.__init__(self, flying_speed) # 비행기능 클래스에 들어가는 인스턴스 지정

valkyrie = flyableAttackUnit("발키리", 200, 6, 5) # 비행공격 유닛 생성
valkyrie.fly(valkyrie.name, "3시") # 비행 클래스에는 이름이 따로 없기때문에 직접 이름 설정