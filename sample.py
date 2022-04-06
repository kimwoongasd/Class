# 자동차 클래스
class Car:
    # class의 생성자 : 항상 함수 형태
    # 매개변수로 항상 self를 가지고 있는다.
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    # class의 메소드
    def show_info(self):
        print("이름" , self.name, "/ 색상", self.color)
        
# 인스턴스 생성
car_1 = Car("소나타", "검은색")
# 메소드 호출
car_1.show_info()

car_2 = Car("아반떼", "빨간색")
car_2.show_info()