# Java 기본

### 변수란?
- 자료를 저장하기 위한 메모리 공간으로 `타입에 따라 크기가 달라짐`
- 메모리 공간에 값을 할당 후 사용

### 타입이란?
- 데이터 타입에 따른 데이터의 종류
- 기본형(primtive type): 미리 정해진 크기의 데이터 표현, 변수 자체에 값 저장
- 참조형(reference type): 크기가 미리 정해질 수 없는 데이터의 표현, 변수에는 실제 값을 참조할 수 있는 주소만 저장

### 기본형의 크기
![!\[Alt text\](image.png)](Java_01-1.png)

-> 기본형은 오버플로우에 유의하며 코드 작성 필수

### 실수형
```
실수의 연산은 정확하지 않음.
- 유효 자리수를 이용한 반올림 처리
```
- 실수에서 정확한 연산을 하려면?
```java
System.out.println(((int)(d1*100) - (int)(d2*100))/100.0); 
// 이렇게 정수로 변환해서 계산하거나

BigDecimal b1 = new BigDecimal("2.0");
BigDecimal b2 = new BigDecimal("1.1");
System.out.println(b1.subtract(b2));
// 이런식으로 BigDecimal 이용
```

### 형 변환이란?
- 변수의 형을 다른 형으로 변환하는 것
  - char  <-> int
- primitive는 primitive끼리, reference는 reference끼리 형 변환 가능
  - boolean은 다른 기본 형과 호환되지 안흠
  - 기본형과 참조형의 형 변환을 위해서 Wrapper 클래스 사용

- 형 변환 방법
  - 형 변환 연산자(괄호) 사용
    - 명시적 형 변환 (반드시 써야함)
    ```java
    int i = 300;
    byte b = (byte)i;
    ```
    - 묵시적 형 변환 (생략 가능)
    ```java
    byte b = 10;
    int i = (int)b;
    int i2 = b;
    ```

### 기본형의 형 변환 진행
- 값의 크기, 타입의 크기가 아닌 `타입의 표현 범위`가 커지는 방향으로 할당한 경우는 묵지석 형변환 발생
![!\[Alt text\](image.png)](java_01-2.png)
- **주의**   
  - `long(64비트) -> float(32비트)` -> long이 더 큰데 float은 실수형이므로 이 부분 주의
  - short와 char는 형변환 X, 호환 안됨.
- 명시적 형변화은 값 손실이 발생할 수 있으므로 프로그래머 책임하에 형변환 진행
- 묵시적 형변환은 자료의 손실 걱정이 없으므로 형변환 연산 생략

```java
public static void main(String[] args){
  int i1 = Integer.MAX_VALUE;
  int i2 = i1 + 1;
  System.out.println(i2);

  long l1 = i1 + 1;
  System.out.println(l1); //오버플로우

  long l2 = (long) (i1 + 1); //오버플로우
  System.out.println(l2);

  long l3 = (long) i1 + 1; //오버플로우X
  System.out.println(l3);

  int i3 = 1000000 * 1000000 / 100000; //오버플로우
  int i4 = 1000000 / 100000 * 100000; //오버플로우X
  System.out.println(i3 + " : " + i4)
}
```

```java
public static void main(String[] args){
  byte b1 = 10;
  byte b2 = 20;
  byte b3 = b1 + b2; // Type mismatch: cannot convert from int to byte -> 아마 덧셈 연산자가 int형부터 지원되는 듯?

  int i1 = 10;
  long l1 = 20;
  int i2 = i1 + l1; // Type mismatch: cannot convert from long to int


  float f1 = 10.0;
  float f2 = f1 + 20.0; // Type mismatch: cannot convert from double to float

}
```
- 산술 이항 연산자는 연산 전에 피 연산자의 타입을 일치시킨다.
- 피연산자의 크기가 4byte(int) 미만이면 int로 변경한 후 연산 진행
- 두 개의 피연산자 중 큰 타입으로 형 변환 후 연산 진행