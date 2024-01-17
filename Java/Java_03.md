## 생성자
- 객체를 생성할 때 호출하는 메서드 비슷한 것
    - new 키워드와 함께 호출하는 것
    - 일반 멤버 변수의 초기화나 객체 생성 시 실행돼야 하는 작업 정리
- 작성 규칙
    - 메서드와 비슷하나 리턴 타입이 없고 이름은 클래스 이름과 동일
- 기본 생성자(default constructor)
    - 기본 생성자의 형태는 파라미터가 없고 구현부가 비어있는 형태
    - 생성자 코드가 없으면 컴파일러가 기본 생성자 제공
- 파라미터가 있는 생성자
    - 생성자의 목적이 일반 멤버 변수의 초기화 -> 생성자 호출 시 값을 넘겨줘서 초기화
    - 주의! `파라미터가 있는 생성자를 만들면 기본 생성자는 추가되지 않음`

## this의 용법
### this
- 참조 변수로써 객체 자신을 가리킴
    - 참조변수를 통해 객체의 멤버에 접근했던 것처럼 this를 이용해 자신의 멤버에 접근 가능
- 용도
    - 로컬 변수와 멤버 변수의 이름이 동일할 경우 멤버 변수임을 명시적으로 나타냄
    - 명시적으로 멤버임을 나타낼 경우 사용
- this는 객체에 대한 참조
    - 따라서 static 영역에서 this 사용 불가

### this()
- 메서드와 마찬가지로 생성자도 오버로딩 가능
    - 객체 생성 시 필요한 멤버변수만 초기화 진행 -> 생성자 별 코드의 중복 발생
    - 한 생성자에서 다른 생성자를 호출할 때 사용
- `반드시 첫 줄에서만 호출이 가능`

```java
public class OverloadConstructorPerson {
    String name = "아무개";
    int age = 0;

    OverloadConstructorPerson(String name, int age){
        this.name = name;
        this.age = age;
    }

    OverloadConstructorPerson(String name){
        this(name, 0); //이런식으로 this.name = name으로 겹치니까 그냥 this()를 사용. 여기도 첫 번째 라인에서만 사용 가능
    }
    OverloadConstructorPerson() {
        // 첫 번째 라인에서만 사용 가능
        this("홍길동", 100);
    }
}

```

## OOP-2
### 객체지향 언어의 특징
- OOP is A P.I.E
- 까먹지말고 항상 마음에 새기자.

|특성|내용|
|---|---|
|Abstraction(추상화)|현실의 객체를 추상화해서 클래스를 구성한다.|
|Polymorphism(다형성)|하나의 객체를 여러가지 타입(형)으로 참조할 수 있다.|
|Inheritance(상속)|부모 클래스의 자산을 물려받아 자식을 정의함으로 코드의 재사용이 가능하다.|
|Encapsulation(데이터 은닉과 보호)|데이터를 외부에 직접 노출시키지 않고 메서드를 이용해 보호할 수 있다.|

### 상속(Inheritance: OOP Is A P`I`E
- 기존(상위) 클래스의 자산(멤버)을 자식(하위) 클래스에서 재사용하기 위한 것
    - 상위 클래스의 생성자와 초기화 블록은 상속하지 않는다.
- 상위 클래스의 멤버를 물려 받기 때문에 코드의 절감
    - 상위 클래스의 코드를 변경하면 모든 하위 클래스들에게도 적용 -> 유지 보수성 향상
- 상속의 적용
    - extends 키워드 사용

- 클래스 다이어그램(이름, 멤버 변수, 멤버 메서드로 구성)
![!\[Alt text\](image.png)](Java_03-01.png)
-> 바뀌어 있음 Person이 조상, SpiderMan이 자식

### Object 클래스
- 모든 클래스의 조상 클래스
    - 별도의 extends 선언이 없는 클래스들은 extends Object가 생략됨
    - 따라서 모든 클래스에는 Object 클래스에 정의된 메서드가 있음
    - hashCode(), equals(), toString() 메서드는 꼭 알아두기!

### 다양한 상속 관계
![!\[Alt text\](image.png)](Java_03-02.png)
- 상속의 관계는 `is a` (kind of) 관계라고 함
    - Person is a Object, SpiderMan is a Person
- Person과 Employee의 관계? 상속
- Object와 Employee의 관계? 상속
- Employee와 SpiderMan의 관계? 아무관계도 아님

### 단일 상속(Single Inheritance)
- 다중 상속의 경우 여러 클래스의 기능을 물려받을 수 있으나 관계가 매우 복잡해짐
    - 동일한 이름의 메서드가 두 상위 클래스에게 모두 있다면 하위 클래스는 어떤 메서드를 쓸 것인가?
- `자바는 단일 상속만 지원`
    - 대신 interface와 포함 관계(`has a`)(->코드 재사용)로 단점 극복

### 포함 관계
- 상속 이외에 클래스를 재활용 하는 방법
    - 2개 이상의 클래스에서 특성을 가져올 때 하나는 상속, 나머지는 멤버 변수로 처리
![!\[Alt text\](image.png)](Java_03-03.png)
- 둘이 같은 표현
- 포함 관계의 UML 표현: 실선 화살표
- Spider의 코드를 수정하면 SpiderMan에도 반영되므로 유지 보수성 확보
- 상속이냐 포함이냐 그것이 문제로다.
- 어떤 클래스를 상속 받고 어떤 클래스를 포함해야 하는가?
    - 문법적인 문제는 아니며 프로젝트의 관점 문제
    - 상속: is a 관계가 성립하는가? -> SpiderMan is a Person.
    - 포함: has a 관계가 성립하는가? -> SpiderMan has a Spider.

## 메서드 재정의
### 메서드 오버라이딩(overriding)
- 조상 클래스에 정의된 메서드를 자식 클래스에서 적합하게 수정하는 것(overWrite)
```java
public class Person{
    void jump(){
        System.out.println("두 다리로 힘껏 점프");
    }
}

public class Spider{
    void jump(){
        System.out.println("키 * 1000만큼 엄청난 점프");
    }
}
    //스파이더맨은 더 많이 뛸 수 있어. 그래서 jump를 다시 정의해보자.

public class SpiderMan2 extends{
    Spider spider - new Spider();
    boolean isSpider;

    void fireWeb() {...}
    void jump() {
        if(isSpider){
            spider.jump();
        }else{
            System.out.println("두 다리로 힘껏 점프");
        }
    }
}
```
- 오버라이딩의 조건
    - 메서드 이름이 같아야 한다.
    - 매개 변수의 개수, 타입, 순서가 같아야 한다.
    - 리턴 타입이 같아야 한다.
    - 접근 제한자는 부모보다 범위가 넓거나 같아야 한다.
    - 조상보다 더 큰 예외를 던질 수 없다.

### super 키워드
- this통해 멤버에 접근했듯이 super를 통해 조상 클래스 멤버 접근
    - super.을 이용해 조상의 메서드 호출로 조상의 코드 재사용
- 변수의 scope
    - 사용된 위치에서 점점 확장해가며 처음 만난 선언부에 연결됨
    - method 내부 -> 해당 클래스 멤버 변수 -> 조상 클래스 멤버 변수
- this()가 해당 클래스의 다른 생성자를 호출하듯 super()는 조상 클래스의 생성자 호출
    - 조상 클래스에 선언된 멤버들은 조상 클래스의 생성자에서 초기화가 이뤄지므로 이를 재활용
    - 자식 클래스에 선언된 멤버들만 자식 클래스 생성자에서 초기화
- super()는 자식 클래스 생성자의 맨 첫 줄에서만 호출 가능
    - 즉 생성자의 첫 줄에만 this() 또는 super()가 올 수 있다.
- 명시적으로 this() 또는 super()를 호출하지 않는 경우 컴파일러가 super() 삽입
    - 결론적으로 맨 상위의 Object까지 객체가 다 만들어지는 구조

### Annotation
- 사전적 의미: 주석
- 컴파일러, JVM, 프레임워크 등이 보는 주석
- 소스코드에 메타 데이터를 삽입하는 형태
    - 소스 코드에 붙여 놓은 라벨
    - 코드에 대한 정보 추가 -> 소스 코드의 구조 변경, 환경 설정 정보 추가 등의 작업 진행

- 기본 annotation의 예
    - @Deprecated
        - 컴파일러에게 해당 메서드가 deprecated(없어질 수도 있다) 되었다고 알려줌
    - @Override
        - 컴파일러에게 해당 메서드는 override한 메서드 임을 알려줌
        - @Override가 선언된 경우 반드시 super class에 선언 되어있는 메서드여야 함
    - @SuppressWarnings
        - 컴파일러에게 사소한 warning의 경우 신경 쓰지 말라고 알려줌

## package와 import
### Package
- PC의 많은 파일 관리 -> 폴더 이용
    - 유사한 목적의 파일을 기준으로 작성
    - 이름은 의미 있는 이름으로, 계층적 접근
- 프로그램의 많은 클래스 -> 패키지 이용
    - 패키지의 이름은 의미 있는 이름으로 만들고 `.`를 통해 계층적 접근
    - 물리적으로 패키지는 클래스 파일을 담고 있는 디렉터리
    - package name _ class name으로 클래스 구분 -> fully qualified name
- package의 선언
    - package package_name;
    - 주석, 공백을 제외한 첫 번째 문장에 하나의 패키지만 선언
    - 모든 클래스는 반드시 하나의 패키지에 속한다.
        - 생략 시 default package에 속하는데 default package는 가급적 사용하지 않는다.

- 일반적인 package naming 룰
    - 소속.프로젝트.용도
    - com.ssafy.hrm.common, com.ssafy.hrm.service,...
    - com.ssafy -> 회사의 identity
    - hrm -> project
    - common -> 용도

### import
- 다른 패키지에 선언된 클래스를 사용하기 위해 키워드
    - 패키지와 클래스 선언 사이에 위치
    - 패키지와 달리 여러 번 선언 가능
- 선언 방법
    - import 패키지명.클래스명;
    - import 패키지명.*;
        - 하위 패키지까지 import 하지는 않는다.
- import 한 package의 클래스 이름이 동일하여 명확히 구분해야 할 때
    - 클래스 이름 앞에 전체 패키지 명을 입력
- default import package
    - java.lang.*;
- import 단축키 -> `ctrl + space` or `ctrl + shift + o`

### 제한자(modifier)
- 클래스, 변수, 메서드 선언부에 함께 사용되어 부가적인 의미 부여
- 종류
    - 접근 제한자: public, protected, (default=package), private
    - 그 외 제한자
        - static: 클래스 레벨의 요소 설정
        - final: 요소를 더 이상 수정할 수 없게 함
        - abstract: 추상 메서드 및 추상 클래스 작성
        - synchronized: 멀티스레드에서의 동기화 처리
- 하나의 대상에 여러 제한자를 조합 가능하나 접근 제한자는 하나만 사용 가능
- 순서는 무관
    - 일반적으로 접근 제한자를 맨 앞으로

### final
- 마지막, 더 이상 바뀔 수 없음
- final class - 더 이상 확장할 수 없음 : 상속 금지 -> 오버라이드 방지
    - 대표적인 final class: String, Math, ...
- final method - 더 이상 재정의할 수 없음 : overriding 금지
- 확장을 못하게 한다기 보다는 실수를 하지 않게 도와주는 느낌
- final variable - 더 이상 값을 바꿀 수 없음(상수)
    - Blank final - 값이 할당되지 않은 멤버 변수
        - final 멤버 변수에 초기 값이 할당되어버리면 모든 객체는 같은 값을 사용해야 함
        - 객체가 생성되면 값을 변경할 기회가 없기 때문에 반드시 `생성자에서 1회 초기화` 가능
    - static final
        - 단지 final만 있으면 객체마다 갖는 값으로 공용성이 없음
        - 진정한 상수는 객체와 무관하게 모두가 공용하는 값(Math.PI, Math.e,...)

### 접근 제한자(Acceess modifier)
- 멤버 등에 사용되며 해당 요소를 외부에서 사용할 수 있는지 설정
![!\[Alt text\](image.png)](Java_03-04.png)