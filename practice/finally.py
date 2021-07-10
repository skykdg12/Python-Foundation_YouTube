class BigNumberError(Exception): # 에러를 정의해서 원하는 에러를 출력 가능함
    def __init__(self, msg): # msg 함수 생성
        self.msg = msg 
        
    def __str__(self): # str이라는 함수 생성해서 msg값을 리턴
        return self.msg
  
try: # 예외처리 
    print("한 자리 숫자 나누기 전용 계산기입니다")
    num1 = int(input("첫 번째 숫자를 입력하세요 :"))
    num2 = int(input("두 번째 숫자를 입력하세요 :"))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0} , {1}".format(num1, num2)) # 에러발생 시 입력한 값 출력
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다 한 자리 숫자만 입력하세요")  
except BigNumberError as err: # 에러로 처리
    print("에러가 발생하였습니다 한 자리 숫자만 입력하세요")
    print(err)
finally: # 에러가 발생하더라도 무조건 마지막 구문 출력 가능
    print("계산기를 이용해 주셔서 감사합니다")