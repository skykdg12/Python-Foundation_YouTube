# 일반 유닛
class Unit: 
    def __init__(self, name, hp, speed): # 이동 속도 추가
       self.name = name 
       self.hp = hp
       self.speed = speed # 이동 속도
       
    def move(self, location): # 이동 함수 생성
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다 [속도 {2}]"\
            .format(self.name, location, self.speed)) # 이름, 방향, 속도
        
 
# 공격 유닛      
class AttackUnit(Unit): # Unit 클래스를 상속받음
    def __init__(self, name, hp, speed, damage): # 이동 속도 추가
        Unit.__init__(self, name, hp, speed) # Unit 클래스의 내용을 가져옴
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
class flyableAttackUnit(AttackUnit, Flyable): 
    def __init__(self, name, hp, damage, flying_speed): 
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed) 
    
    def move(self, location): # 지상과 공중 유닛 모두 move함수로 통일시키기 위해 move함수 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location) # 이름과 방향 
        
# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super을 통해서도 상속 가능 단, self를 빼고 뒤에 super뒤에 괄호가 있어야함 하지만
                                    # 다중 상속을 받을 경우 먼저 상속받는 내용만 출력하기 때문에 다중의 경우 모든 상속받을 내용들을 일일이 적어줘야함
        self.location = location