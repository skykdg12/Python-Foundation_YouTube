def open(): #새로운 함수를 생성
    print("새로운 계좌가 생성되었습니다")
    
open() #함수를 작성해야 실행시 프린트 명령어 작동

def deposit(balance, money): #입금 함수 생성
    print("입금이 완료되었습니다. 잔액은 {0}원입니다".format(balance + money))
    return balance + money #기본금액 + 입금한 금액

def withdraw(balance, money): #출금 함수 생성
    if balance >= money: # 잔액이 출금액보다 크면
        print("출금이 완료되었습니다 잔액은{0}원입니다".format(balance - money))
        return balance - money #기본금액 - 출금액하고 남은 금액
    else: # 잔액이 출금액보다 작으면
        print("출금이 완료되지 않았습니다 잔액은 {0}원입니다".format(balance))
        return balance #남은 금액
    
def withdraw_night(balance, money):#야간 출금 함수 생성
    commision = 100 #수수료
    return commision, balance - money - commision #수수료, 잔고 - 출금액 - 수수료

balance = 0
balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
commision, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다".format(commision,balance))

