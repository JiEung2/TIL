# Java_05

## 추상 클래스
- 아래 클래스들의 공통 분모를 뽑아서 상속 구조를 만들자.
```java
public class DieselSUV{
  private int curX, curY;

  public void reportPosition() {
    System.out.printf("현재 위치: (%d, %d%n)", curX, curY);
  }

  public void addFuel() {
    System.out.printf("주유소에서 급유");
  }
}

public class ElectricCar {
  private int curX, curY;

  public void reportPosition() {
    System.out.printf("현재 위치: (%d, %d)%n", curX, curY);
  }

  public void addFuel() {
    System.out.printf("급속 충전");
  }
}
```
-> 클래스 간 공통 모듈이 많음

- 상속 관계 정의를 통한 클래스 정비
```java
class Vehicle {
  private int curX, curY;

  public void reportPosition() {
    System.out.printf("현재 위치: (%d, $d)%n", curX, curY);
  }

  public void addFuel() {
    System.out.println("모든 운송 수단은 연료가 필요");
  }

  class DieselSUV extends Vehicle {
    @Override
    public void addFuel() {
      System.out.println("주유소에서 급유");
    }

    class ElectricCar extends Vehicle {
      @Override
      public void addFuel() {
        System.out.println("급속 충전");
      }
    }
  }
}
```
![!\[Alt text\](image.png)](Java_05-1.png)
-> 상속으로 코드의 재사용성이 좋아짐.  

코드를 이렇게 작성하면 어차피 Vehicle의 addFuel은 작동하지 않음. 그래서 addFuel을 없애버리면?  
-> if문을 사용해서 해당 클래스라면 클래스변수명.addFuel()을 사용해야함.

### 추상 클래스 정의
- DieselSUV, ElectricCar는 모두 연료가 필요하므로 addFuel은 공통 모듈
  - 조상 클래스인 Vehicle에 정리하고 각 자손 클래스에서 override 예정
  - Vehicle에서 힘들게 구현했지만, 아무도 Vehicle의 addFuel()에 신경쓰지 않음
    - addFuel()을 Vehicle에서 지우면?
  
  - 자손 클래스에서 반드시 재정의해서 사용되기 때문에 조상의 구현이 무의미한 메서드
    - 메서드의 선언부만 남기고 구현부는 세미콜론 `:` 으로 대체
    - 구현부가 없다는 의미로 abstract 키워드를 메서드 선언부에 추가
    - 객체를 생성할 수 없는 클래스라는 의미로 클래스 선언부에 abstract를 추가

    ```java
    abstract class Vehicle {
      private int curX, curY;

      public void reportPosition() {
        System.out.printf("현재 위치: (%d, %d)%n", curX, curY);
      }

      public abstract void addFuel();
    }

    ```
    이런 형태를 abstract method design pattern이라고 함

### 추상 클래스의 특징
  - abstract 클래스는 상속 전용의 클래스
    - 자식은 abstract method를 재정의할 책임
    - 클래스에 구현부가 없는 메서드가 있으므로 객체를 생성할 수 없음
    - 하지만 상위 클래스 타입으로써 자식을 참조는 가능
    ```java
    // Vehicle v = new Vehicle(); // abstract 클래스는 객체를 생성할 수 없음
    Vehicle V = new DieselSUV(); // 자식을 참조하는 것은 문제 없음
    ```
  
  - 조상 클래스에서 상속받은 abstract 메서드를 재정의 하지 않은 경우
    - 클래스 내부에 abstract 메서드가 있는 상황이므로 자식 클래스는 abstract 클래스로 선언되어야 함

### 추상 클래스를 사용하는 이유
- abstract 클래스는 `구현의 강제`를 통해 프로그램의 안정성 향상  
  ![!\[Alt text\](image.png)](Java_05-2.png)
- HorseCart에서 addFuel() 메서드를 필수로 오버라이드 하게 강제함
- interface에 있는 메서드 중 구현할 수 있는 메서드를 구현해 개발의 편의 지원

## Interface
### 인터페이스란?
- 서로 다른 두 시스템, 장치, 소프트웨어 따위를 서로 이어 주는 부분. 또는 그런 접속 장치.
- GUI - Graphic User Interface
  - 프로그램과 사용자 사이의 접점
- 인터페이스를 사이에 두고 한쪽은 사용에 관심, 한쪽은 구현에 관심

### 인터페이스 작성
- 최고 수준의 추상화 단계: 일반 메서드는 모두 abstract 형채
  - JDK 8에서 default method와 static method 추가
- 형태
  - 클래스와 유사하게 interface 선언
  - 멤버 구성
    - 모든 멤버변수는 public static final 이며 생략 가능
    - 모든 메서드는 public abstract이며 생략 가능
    ```java
    public interface MyInterface{
      public static final int MEMBER1 = 10;
      int MEMBER2 = 10;

      public abstract void method1(int param);
      void method2(int param);
    }
    ```
- 인터페이스는 object를 상속받지 않음. 따라서 클래스가 아님.

### 인터페이스 상속
- 클래스와 마찬가지로 인터페이스도 extends를 이용해 상속이 가능
- 클래스와 다른 점은 인터페이스는 다중 상속이 가능
  - 헷갈릴 메서드 구현 자체가 없음

  ```java
  interface Fightable{
    int fire();
  }

  interface Transformable{
    void changeShape(boolean isHeroMode);
  }

  public interface Heroable extends Fightable, Transformable{
    void upgrade();
  }
  ```
  ![!\[Alt text\](image.png)](Java_05-3.png)

### 인터페이스 구현과 객체 참조
- 클래스에서 implements 키워드를 사용해서 interface 구현
- implements 한 클래스는
  - 모든 abstract 메서드를 override해서 구현하건
  - 구현하지 않을 경우 abstract 클래스로 표시해야함
- 여러 개의 interface implements 가능
- 다형성은 조상 클래스 뿐 아니라 조상 인터페이스에도 적용
  ```java
  public class IronManTest{
    public static void main(String[] args){
      IronMan iman = new IronMan();
      Object obj = iman;
      Heroable hero = iman;
      Fightable fight = iman;
      Transformable trans = iman;
    }
  }
  ```
- interface와의 관계도 is a 관계이지만 좀 더 세부적으로 is able to 라고도 한다.
  - ~~ 할 수 있는 기능을 가지게 되는 관계
  - Serializable, Cloneable, Comparable...

### 인터페이스와 abstract 클래스와의 차이
- 인터페이스에서는 일반 메서드를 가질 수 없음
- 인터페이스는 다중 상속이 가능. 

### Interface 필요성
- 구현의 강제로 표준화 처리
  - abstract 메서드 사용
  - 손쉬운 모듈 교체 지원
  - printer에 대한 인터페이스를 구현해두면 프린터를 교체할 때마다 번거로운 작업을 할 필요가 없음
- 인터페이스를 통한 간접적인 클래스 사용으로 손쉬운 모듈 교체 지원
- 서로 상속의 관계가 없는 클래스들에게 인터페이스를 통한 관계 부여로 다형성 확장
- 모듈 간 독립적 프로그래밍 가능 -> 개발 기간 단축