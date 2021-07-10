class ThailandPackage:
    def detail(self):
        print("태국 패키지 3박 5일 방콕, 파타야 여행")
        
if __name__ == "__main__": # 모듈 내부에서 실행하는건지 외부에서 실행하는건지 구별 가능
    print("Thailand 모듈을 직접 실행")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")