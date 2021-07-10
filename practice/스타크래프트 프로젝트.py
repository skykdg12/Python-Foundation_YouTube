from random import * # 피해값을 랜덤으로 가져오기 위함

# 일반 유닛
class Unit: 
    def __init__(self, name, hp, speed): # 이동 속도 추가
       self.name = name 
       self.hp = hp
       self.speed = speed # 이동 속도
       print("{0} 유닛이 생성되었습니다".format(name))
       
    def move(self, location): # 이동 함수 생성
        print("{0} : {1} 방향으로 이동합니다 [속도 {2}]"\
            .format(self.name, location, self.speed)) # 이름, 방향, 속도
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage)) 
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp)) 
        if self.hp <=0: 
            print("{0} : 파괴되었습니다".format(self.name,))

 
# 공격 유닛      
class AttackUnit(Unit): # Unit 클래스를 상속받음
    def __init__(self, name, hp, speed, damage): # 이동 속도 추가
        Unit.__init__(self, name, hp, speed) # Unit 클래스의 내용을 가져옴
        self.damage = damage # Unit 클래스의 없는 내용 추가 

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다 공격력 {2}"\
              .format(self.name, location, self.damage))

# 마린       
class Marine(AttackUnit): # 마린 클래스 생성
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5) #어택유닛 상속받음
    def stimpack(self): # 스팀팩 함수 생성
        if self.hp > 10: # 조건 설정
            self.hp -=10
            print("{0} : 스팀팩을 사용합니다 (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

# 탱크            
class Tank(AttackUnit): # 탱크 클래스 생성
    # seize_developed = False # 시즈모드 개발 여부
    
    def __init__(self): # 어택유닛 상속 받음
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False # 시즈모드 여부
        
    def set_seize_mode(self): # 시즈모드 전환 함수 생성
        # if Tank.seize_developed == False: # 시즈모드가 개발 안되어있다면 빠져나옴
        #     return
        
        # 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False: # 시즈모드가 아니라면
            print("{0} : 시즈모드로 전환합니다".format(self.name))
            self.damage *= 2 # 데미지 2배
            self.seize_mode = True
            
        # 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다".format(self.name))
            self.damage /= 2
            self.seize_mode = False         
            
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
        self.fly(self.name, location) # 이름과 방향 
        
# 레이스
class Wraith(flyableAttackUnit): # 레이스 클래스 생성
    def __init__(self):
        flyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 플라이어블어택유닛 상속
        self.clocked = False #클로킹 모드
        
    def clocking(self): # 클로킹 함수 생성
        if self.clocked == True: # 조건
            print("{0} : 클로킹 모드 해제합니다".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정합니다".format(self.name))
            self.clocked = True
            
def game_start():
    print("새로운 게임을 시작합니다")
    
def game_over():
    print("player : gg")
    print("[player] 님이 게임을 나갔습니다")
    

# 실제 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units: # unit에 어택 유닛 설정
    unit.move("1시") # 모든 유닛 이동

# 탱크 시즈모드 개발
# Tank.set_seize_mode = True
# print("탱크 시즈 모드 개발이 완료되었습니다")

# 공격 모드 준비
for unit in attack_units: # 유닛에 어택 유닛 입력
    if isinstance(unit, Marine): # 유닛이 마린이라면 스팀팩 사용
        unit.stimpack()
    elif isinstance(unit, Tank): # 유닛이 탱크라면 시즈모드 사용
        unit.set_seize_mode()
    elif isinstance(unit, Wraith): # 유닛이 레이스라면 클로킹 사용
        unit.clocking()
        
        
# 전군 공격
for unit in attack_units: 
    unit.attack("1시")
    
# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음
    
# 게임 종료
game_over()
    
