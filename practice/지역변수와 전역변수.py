gun = 10 #전역변수

def checkpoint(soldiers):
    global gun #전역 공간에 있는 변수 사용
    # gun = 20 #지역변수
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers #gun을 그냥 쓰면 값이 없지만 밑에서 입력 후 값을 받아옴
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun #결과를 리턴

    
print("전체 총 : {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2) #전역변수 값에 체크포인트 함수 값을 입력
print("남은 총 : {0}".format(gun))