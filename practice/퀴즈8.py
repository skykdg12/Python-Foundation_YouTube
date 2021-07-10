# 주어진 코드를 활용하여 부동산 프로그램을 작성하시오

# (출력예제)
# 총 3대의 매물이 있습니다
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년


class House: # House 클래스 생성
    def __init__(self, location, house_type, deal_type, price, completion_year): # 각 인스턴스에 값 입력
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        
    def show_detail(self): # House 값을 출력하는 함수 생성
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = [] # 리스트 생성해서 각 정보들을 입력
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1) # 입력한 정보들을 리스트에 추가
houses.append(house2)
houses.append(house3)

print("총 {0} 대의 매물이 있습니다".format(len(houses))) # houses의 길이를 구해서 갯수 계산
for house in houses: # house 안에 houses의 리스트 추가
    house.show_detail() # 값 출력
