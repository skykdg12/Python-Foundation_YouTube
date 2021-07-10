# 동네에 항상 대기 손님이 있는 치킨집이 있습니다
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#         출력 메세지 : "잘못된 값을 입력하였습니다"
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생 시키고 프로그램 종료
#         출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다"
        
# [코드]
chicken = 10
waiting = 1
class SoldOutError(Exception): # 조건 2를 위해 에러 클래스 생성
    pass # 굳이 인스턴스 추가 안하고 에러 발생 시 메세지만 출력하기 위함

while(True): # 재료가 소진할 때까지 반복
    try: # 에러 처리 
        print("[남은 치킨 : {0}".format(chicken)) # 남은 치킨에 포맷을 이용해 자동으로 채움
        order = int(input("치킨 몇 마리 주문하시겠습니까?")) # 인트를 씌웟기 때문에 조건1의 숫자가 아닐시 조건 만족
        if order > chicken: # 조건
            print("재료가 부족합니다")
        elif order <= 0: # 조건 1을 위해 작성
            raise ValueError # order가 0이하 일때 ValueError 발생하라는 명령
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다"\
                .format(waiting, order))
            waiting += 1 # 대기번호를 자동으로 1씩 추가
            chicken -= order # 치킨 재료에 오더를 자동으로 빼서 남은 재고 확인
            
        if chicken == 0: # 조건 2를 위해 if를 한번 더 사용
            raise SoldOutError # 치킨 재료가 0일 때 SoldOutError 발생하라는 명령
    except ValueError: # 예외 처리를 통해서 에러 발생시 문구 출력
        print("잘못된 값을 입력하였습니다")
    except SoldOutError: # 예외 처리를 통해 에러 발생시 문구 출력
        print("재고가 소진되어 더 이상 주문을 받지 않습니다")
        break # 재고가 0이 될 시 자동으로 프로그램을 나가는 명령