import theater_module
theater_module.price(3) # 3명이 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이 조조 할인
theater_module.price_soldier(5) # 5명 군인

import theater_module as mv # mv로 단축해서 사용가능
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import * # *을 통해 모든걸 가져왔기 때문에 바로 모듈명으로 사용가능
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning # 원하는것들만 사용가능
price(3)
price_morning(4)

from theater_module import price_soldier as price # 1개만 가져오기 때문에 모듈명 단축해서 사용 가능
price(5)
