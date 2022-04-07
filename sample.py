# 자동차 클래스
class Car:
    # class의 생성자 : 항상 함수 형태
    # 매개변수로 항상 self를 가지고 있는다.
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    # 클래스 소멸자 : 인스턴스가 소멸되었을 떄 처리해주는 함수
    def __del__(self):
        print("인스턴스를 소멸시킵니다.")
    
    # class의 메소드
    def show_info(self):
        print("이름" , self.name, "/ 색상", self.color)
        
    # Settet 메서드 : 특정한 값을 변경할 때 사용
    def set_name(self, name):
        self.name = name
        
# # 인스턴스 생성
# car_1 = Car("소나타", "검은색")
# # 메소드 호출
# car_1.show_info()

# car_2 = Car("아반떼", "빨간색")
# car_2.show_info()

# # car_1의 대한 name 속성 접근
# print(car_1.name)

# # settet 함수로 이름 바꾸기
# car_1.set_name("트럭")
# print(car_1.name)
# del car_1
# car_1.show_info()

# 상속 : 다른 클래스의 내용(속성과 메서드)을 물려받아 사용하는 기법


# # 공격력 없는 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

#     def move(self):
#         print(f"{self.name}이 이동")
        

# # 공격력 있는 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         # Unit클래스를 상속받아 속성을 사용 가능하다.
#         Unit.__init__(self, name, hp)
#         self.damage = damage
        
#     def attack_move(self):
#         print(f"{self.name} 공격력 {self.damage}로 공격합니다.")
        
# class Flyable:
#     def __init__(self, speed):
#         self.speed = speed
        
#     def fly(self, name, location):
#         print(f"{self.name}이 {location}으로 날아갑니다 [속도 {self.speed}]")
        

# class AttackFly(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, speed)
        
#     def move(self, location):
#         self.fly(self.name, location)
        
# m_1 = Unit("메딕", "80")
# m_2 = Unit("메딕", "80")
# t_1 = AttackUnit("탱크", "80", "50")
# t_1.move()
# t_1.attack_move()

# r_1 = AttackFly("레이스", "150", "20", "20")
# r_1.move("5시")

# supper
class Unit:
    def __init__(self):
        print('유닛 클래스')
        
class Fly:
    def __init__(self):
        print('Fly 클래스')
        
class Flyunit(Unit, Fly):
    def __init__(self):
        super().__init__()
        print("다중상속")
        
a = Flyunit()