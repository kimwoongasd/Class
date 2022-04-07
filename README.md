# class 정리
## 클래스 개요
- 클래스는 객체의 구조와 행동을 정의합니다.
- 객체의 클래스는 초기화를 통해 제어합니다.
- 래스는 복잡한 문제를 다루기 쉽도록 만듭니다.
  
## class 란?
반복되는 불필요한 소스코드를 최소화 하면서 프로그래밍 상에서 쉽게 표현할 수 있도록 해주는 프로그래밍 기술

## 인스턴스
class로 정의된 객체를 프로그램 상에서 이용할 수 있게 만든 변수

### 클래스를 이루는 2가지 요소
- class의 맴버 : class 내부에 포함되는 변수
- class의 메서드 : class 내부에 포함되는 함수


```python
# 자동차 클래스
class Car:
    # class의 생성자 : 항상 함수 형태
    # 매개변수로 항상 self를 가지고 있는다.
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    # class의 메서드
    def show_info(self):
        print("이름" , self.name, "/ 색상", self.color)
        
# 인스턴스 생성
car_1 = Car("소나타", "검은색")
# 메서드 호출
car_1.show_info()
```

### self의 의미
self는 인스턴스 자기 자신을 의미한다.  
클래스에서 모든 메서드는 self라는 첫번쨰 매개변수로 삼는다.

- Car 라는 클래스를 생성하고 속성으로 name과 color를 주었다.
    
- Car으로 변수 car_1를 만들었는데 이 car_1이 Car의 인스턴스(instance)입니다. 클래스는 특정 개념을 표현만 할뿐 사용을 하려면 인스턴스를 생성해야 합니다.

- 메소드는 class가 아니라 인스턴스를 통해 호출한다. 인스턴스.메서드()와 같이 점을 붙이고 메소드를 호출한다.
- 이렇게 인스턴스를 통해 호출하는 메서드를 인스턴스 메서드라고 부른다.

### 인스턴스 속성

```python
# car_1의 대한 name 속성 접근
print(car_1.name)

# car_2의 대한 name 속성 접근
print(car_2.name)
```
이렇게 인스턴스를 통해 접근하는 속성을 인스턴스 속성이라고 부른다.


#### Settet 함수
Settet 메서드 : 특정한 값을 변경할 때 사용
```python
class Car:
    # class의 생성자 : 항상 함수 형태
    # 매개변수로 항상 self를 가지고 있는다.
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    # class의 메소드
    def show_info(self):
        print("이름" , self.name, "/ 색상", self.color)
        
    # Settet 메서드 : 특정한 값을 변경할 때 사용
    def set_name(self, name):
        self.name = name

# 인스턴스 생성
car_1 = Car("소나타", "검은색")

# settet 함수로 이름 바꾸기
car_1.set_name("트럭")
print(car_1.name)
```

실행을 하면 소나타였던 이름이 트럭으로 바뀌는 것을 확인할 수 있다.

### 클래스 소멸자
인스턴스가 소멸되었을 떄 처리해주는 함수  

```python
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

# 인스턴스 생성
car_1 = Car("소나타", "검은색")

# settet 함수로 이름 바꾸기
car_1.set_name("트럭")
print(car_1.name)
# 인스턴스 삭제
del car_1

# 인스턴스 삭제되어 오류
car_1.show_info()
```

- 파이썬 같은 경우 하나의 변수(객체)를 만든다고 하면 내부적으로 메모리상의 
해당 변수가 필요한 공간만큼 동적으로 메모리공간을 할당해서 이용한다.  
한번 사용하고 사용하지 않을 변수(객체)는 메모리상에서 할당을 해제할 수 있다.

## 상속
### 상속이란?
- 클래스에서 상속이란, 물려주는 클래스(부모 클래스)의 내용(속성과 메소드)을 물려받는 클래스(자식 클래스)가 가지게 되는 것입니다.
- 예를 들면 국가라는 클래스가 있고, 그것을 상속받은 한국, 일본, 중국, 미국 등의 클래스를 만들 수 있으며, 국가라는 클래스의 기본적인 속성으로 인구라는 속성을 만들었다면, 상속 받은 한국, 일본, 중국 등등의 클래스에서 부모 클래스의 속성과 메소드를 사용할 수 있음을 말합니다.
- 기본적인 사용방법은 아래와 같습니다.
- 자식클래스를 선언할때 소괄호로 부모클래스를 포함시킵니다.

```python
class 부모클래스:
    ...내용...

class 자식클래스(부모클래스):
    ...내용...
```

### 상속 예제
```python
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def move(self):
        print(f"{self.name}이 이동")
        

# 공격력 있는 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        # Unit클래스를 상속받아 속성을 사용 가능하다.
        Unit.__init__(self, name, hp)
        self.damage = damage
        
    def attack_move(self):
        print(f"{self.name} 공격력 {self.damage}로 공격합니다.")
        
m_1 = Unit("메딕", "80")
m_2 = Unit("메딕", "80")
t_1 = AttackUnit("탱크", "80", "50")
t_1.move()
t_1.attack_move()
```

- Unit 이라는 클래스의 내용을 상속받아서 AttackUnit을 만들었다.
- AttackUnit은 Unit의 자식클래스
- Unit은 AttackUnit의 부모클래스가 된다.
- 상속받은 AttackUnit은 부모클래스의 메서드 사용가능하다.

## 다중상속
한 클래스에 여러 클래스가 상속하는 것이다.

간당하게 사용해 보자
```python
# 공격력 없는 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self):
        print(f"{self.name}이 이동")
        

# 공격력 있는 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        # Unit클래스를 상속받아 속성을 사용 가능하다.
        Unit.__init__(self, name, hp)
        self.damage = damage
        
    def attack_move(self):
        print(f"{self.name} 공격력 {self.damage}로 공격합니다.")

# 공중유닛      
class Flyable:
    def __init__(self, speed):
        self.speed = speed
        
    def fly(self, name, location):
        print(f"{self.name}이 {location}으로 날아갑니다 [속도 {self.speed}]")
        
# 공격가능 공중 유닛
class AttackFly(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, speed)
        
r_1 = AttackFly("레이스", "150", "20", "20")
r_1.fly(r_1.name, "5시")
```

- 이렇게 상속을 여러개 받아서 사용이 가능하다.
  

## 메소드 오버라이딩
- 메소드 오버라이딩은 부모 클래스의 메소드를 자식 클래스에서 재정의 하는 것이다.
  
```python
# 공격력 없는 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def move(self):
        print(f"{self.name}이 이동")
        

# 공격력 있는 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        # Unit클래스를 상속받아 속성을 사용 가능하다.
        Unit.__init__(self, name, hp)
        self.damage = damage
        
    def attack(self):
        print(f"{self.name} 공격력 {self.damage}로 공격합니다.")
        
class Flyable:
    def __init__(self, speed):
        self.speed = speed
        
    def fly(self, name, location):
        print(f"{self.name}이 {location}으로 날아갑니다 [속도 {self.speed}]")
        

class AttackFly(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, speed)
        
m_1 = Unit("메딕", "80")
m_2 = Unit("메딕", "80")
t_1 = AttackUnit("탱크", "80", "50")
t_1.attack()

r_1 = AttackFly("레이스", "150", "20", "20")
t_1.move()
r_1.fly(r_1.name, "5시")
```

- 위 코드를 보면 지상유닛과 공중유닛 이동할 떄 마다 move 메서드와 fly메서드를 구분해서 써야하는 번거로움이 있다.
- 이것을 해결하기 위해서 아래의 코드로 바꾸어 보자

```python
class AttackFly(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, speed)
    
    # 재정의
    def move(self, location):
        self.fly(self.name, location)

t_1 = AttackUnit("탱크", "80", "50")
t_1.attack()

r_1 = AttackFly("레이스", "150", "20", "20")
t_1.move()
r_1.move( "5시")
```

- 같은 함수가 2개이지만 부모클래스의 메서드가 아닌 자식 클래스에서 재정의한 메서드가 실행된다.

### super
- 부모클래스의 메소드도 수행하고, 자식클래스의 메소드의 내용도 함께 출력하기를 원할 수 있다.
- 그럴때는 super() 라는 키워드를 사용하면 자식클래스 내에서 코드에서도 부모클래스를 호출할 수 있다.

```python
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
```

- super를 쓸떄는 sunper() 괄호가 있어야하고 self는 없어야한다.
- 실행하면 유닛 클래스의 출력문과 Flyunit의 출력문이 같이 나오는 것을 확인할 수 있다.

```python
class Unit:
    def __init__(self):
        print('유닛 클래스')
        
class Fly:
    def __init__(self):
        print('Fly 클래스')
        
class Flyunit(Fly, Unit):
    def __init__(self):
        super().__init__()
        print("다중상속")
        
a = Flyunit()
```

- 상속 순서를 바꾸면 Fly클라스 출력문이 나온다.
- 다중 상속일 떄는 맨 앞 상속자가 호출된다.
- 다중 상속일 때는 따로 명시적으로 쓰는 것이 좋다.