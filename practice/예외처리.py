try: # 예외처리 하기 위함
    print("나누기 전용 계산기입니다")
    nums = [] # nums라는 리스트 만듬
    nums.append(int(input("첫 번째 숫자를 입력하세요 : "))) # 리스트에 추가
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1])) # 이 부분을 누락 시켯을 시
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError: # 위에 식들을 잘못 시행할 시 에러가 발생하는 예외 적용
    print("에러! 잘못된 값을 입력하였습니다")
except ZeroDivisionError as err: # 0으로 나눌 때의 에러 정의
    print(err)
except Exception as err: # 이렇게 정의하게 되면 오류만 나는게 아니라 정확한 이유가 보임
    print("알 수 없는 에러가 발생하였습니다")
    print(err)