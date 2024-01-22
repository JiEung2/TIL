# Java_04
## OOP
## 데이터 은닉과 보호(Encapsulation, OOP Is A PI`E`)
- 누군가 당신의 정보를 마음대로 바꾼다면?
- 소중한 정보가 보호되지 못하는 이유는?
- 정보를 보호하기 위한 대책은?
  - 변수는 private 접근으로 막기
  - 곡개되는 메서드를 통한 접근 통로 마련: setter / getter
    - 메서드에 정보 보호 로직 작성

### 객체의 생성 제어와 Singleton 디자인 패턴
- 객체의 생성을 제한해야 한다면?
  - 여러 개의 객체가 필요 없는 경우
    - 객체를 구별할 필요가 없는 경우 = 수정 가능한 멤버 변수가 없고 기능만 있는 경우
    - 이런 객체를 stateless한 객체라고 한다.
  - 객체를 계속 생성/삭제 하는데 많은 비용이 들어서 재사용이 유리한 경우

- Singleton 디자인 패턴
  - 외부에서 생성자에 접근 금지 -> 생성자의 접근 제한자를 private으로 설정
  - 내부에서는 private에 접근 가능하므로 직접 객체 생성 -> 멤버 변수이므로 private 설정
  - 외부에서 private member에 접근 가능한 getter 생성 -> setter는 불필요
  - 객체 없이 외부에서 접근할 수 있도록 getter와 변수에 static 추가

  - 외부에서는 언제나 getter를 통해서 객체를 참조하므로 하나의 객체 재사용

```java
//주석처리 되어있는 것. 기본적으로 선언되어있지만 숨겨져 있는 것들
//import java.lang.*;

class SingletonClass {//extends Object
    // public SingletonClass(){
    //   super();
    // }
    private static SingletonClass instance = new SingletonClass();

    public static SingletonClass getInstance(){
        return instance;
    }

    public void sayHello() {
        System.out.println("Hello");
    }
}

public class SingletonTest {
    public static void main(String[] args){
        SingletonClass sc = new SingletonClass();
        sc.sayHello();

        SingletonClass sc2 = new SingletonClass();
        sc2.sayHello();

        System.out.println(sc == sc2);
    }

}
```

## 다형성(Polymoriphism: OOP Is A `P`IE)
- 하나의 객체가 많은 형(타입)을 가질 수 있는 성질

- 상속 관계에 있을 때 `조상 클래스의 타입으로 자식 클래스 객체를 레퍼런스` 할 수 있다.
  ![!\[Alt text\](image.png)](Java_04-01.png)

```java
SpiderMan onlyOne = new SpiderMan();
```
- onlyOne은 SpiderMan 타입인가?
  - SpiderMan 타입으로 onlyOne을 참조할 수 있는가?
- onlyOne은 Person 타입인가?
  - Person 타입으로 onlyOne을 참조할 수 있는가?
- onlyOne은 Object 타입인가?
  - Object 타입으로 onlyOne을 참조할 수 있는가?
- onlyOne은 Venom 타입인가?
  - Venom 타입으로 onlyOne을 참조할 수 있는가?

### 다형성의 활용 예1 - 다른 타입의 객체를 다루는 배열
- 배열의 특징 - 같은 타입의 데이터를 묶음으로 다룬다.
- 다형성으로 다른 타입의 데이터 (Person, SpiderMan)를 하나의 배열로 관리

```java
void beforePoly() {
    Person[] persons = new Person[10];
    persons[0] = new Person();
    SpiderMan[] spiderMans = new SpiderMan[10];
    spiderMans[0] = new SpiderMan();
}

void afterPoly() {
    Person[] persons = new Person[10];
    persons[0] = new Person();
    persons[1] = new SpiderMan();
}
```
- Object는 모든 클래스의 조상!!
  - Object의 배열은 어떤 타입의 객체라도 다 저장할 수 있음
- 자바의 자료 구조를 간단하게 처리할 수 있음
  - 이와 같은 특성을 이용하여 Collection API가 등장하게 됨
    ```java
    public ArrayList(int initialCapacity) {
        if(initialCapacity > 0){
            this.elementData = new Object[initialCapacity];
        } else if(initialCapacity == 0){
          this.elementData = EMPTY_ELEMENTDATA;
        } else {
          throw new IllegalArgumentException("Illegal Capacity: " + initialCapacity);
        }
    }
    ```
  - 기본형은 담을 수 있을까? -> 기본형은 Object가 아니라서 못담음.
  - 만약에 3을 넣으면 Integer Wrapper 클래스로 감싸서 들어감 -> 이런 것을 auto boxing이라고 부름.

### 다형성의 활용 예2 - 매개변수의 다형성
- 무언가를 출력하고 싶다!!
  - 메서드가 호출되기 위해서는 메서드 이름과 파라미터가 맞아야 하는데...
- 사실 println은
  ```java
  public void println(Object x){
      String s = String.valueOf(x);
      synchronized(this){
        print(s);
        newLine();
      }
  }
  ```
  - 조상을 파라미터로 처리한다면 객체의 타입에 따라 메서드를 만들 필요가 없어진다.
- API에서 파라미터로 Object를 받는다는 것은 모든 객체를 처리한다는 말이다.

## 객체의 형 변환
### 다형성과 참조형 객체의 형 변환
- 메모리에 있는 것과 사용할 수 있는 것의 차이
  - 메모리에 있더라도 참조하는 변수의 타입에 따라 접근할 수 있는 내용이 제한됨
  ```java
  Person person = new SpiderMan();
  // -> person은 SpiderMan의 기능을 모름
  ```

### 참조형 객체의 형 변환
- 하위 타입을 상위 타입으로 형 변환 -> 묵시적 캐스팅
  ```java
  Phone phone = new Phone();
  Object obj = phone;
  ```
  - 자손 타입의 객체를 조상 타입으로 참조: 형 변환 생략 가능
    - 왜냐면 조상의 모든 내용이 자식에 있기 때문에 걱정할 필요가 없다.
- 상위 타입을 하위 타입으로 형 변환 -> 명시적 캐스팅
  ```java
  Phone phone = new SmartPhone();
  SmartPhone sPhone= (SmartPhone)phone;
  ```
  - 조상 타입을 자손 타입으로 참조: 형 변환 생략 불가

- 무늬만 SpiderMan인 Person
  ```java
  Person person = new Person();
  SpiderMan sman = (SpiderMan) person;
  sman.fireWeb();
  ```
  - 메모리의 객체는 fireWeb이 없음
  - 런타입 오류 발생.

- 조상을 무작정 자손으로 바꿀 수는 없다.
  - instanceof 연산자
    - 실제 메모리에 있는 객체가 특정 클래스 타입인지 boolean으로 리턴
    ```javas
    Person person = new Person();

    if(person instanceof SpiderMan){
        SpiderMan sman = (SpiderMan) person;
    }
    ```

### 참조 변수의 레벨에 따른 객체의 멤버 연결 ⭐⭐⭐⭐
![!\[Alt text\](image.png)](Java_04-02.png)
```java
public class MemberBindingTest{
    public static void main(String[] args){
        SubClass subClass = new SubClass();
        System.out.println(subClass.x); //얘는 당연히 sub가 나옴
        subClass.method();

        SuperClass superClass = subClass;
        System.out.println(superClass.x);
        superClass.method();
        //얘는 원래는 super가 나오는게 맞는데 그림 왼쪽에서 method()가 자식클래스에서 오버라이딩 되어 있다면, 자식 클래스의 method를 실행
    }
}
```

- 정적 바인딩(static binding)
  - 컴파일 단계에서 참조 변수의 타입에 따라 연결이 달라짐
  - 상속 관계에서 객체의 멤버 변수(static/instance)가 중복될 때 또는 static method

- 동적 바인딩(dynamic binding)
  - 다형성을 이용해서 메서드 호출이 발생할 때 runtime에 메모리의 실제 객체의 타입으로 결정
  - 상속 관계에서 객체의 instance method가 재정의 되었을 때 마지막에 재정의 된 자식 클래스의 메서드가 호출됨
    - 최대한 메모리에 생성된 실제 객체의 최적화 된 메서드가 동작한다.

||정적 바인딩|동적 바인딩|
|:---:|:---:|:---:|
|수행 속도|상대적으로 빠름|상대적으로 느림|
|메모리 공간 활용 효율|상대적으로 높음|상대적으로 낮음|
|객체 지향적||다형성으로 효율적인 코드 재사용 가능|