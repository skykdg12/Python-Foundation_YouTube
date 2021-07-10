# import travel.태국 
# # import travel.태국.ThailandPackage() # import 에서는 클래스를 바로 사용 못함
# trip_to = travel.태국.ThailandPackage()
# trip_to.detail()

# from travel.태국 import ThailandPackage # from에서는 클래스를 바로 사용가능
# trip_to = ThailandPackage()
# trip_to.detail()

from travel import 태국 # 모듈부터 불러오는 방식도 가능
trip_to = 태국.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(태국))