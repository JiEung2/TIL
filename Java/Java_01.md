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

## 배열
### 배열이란?
- 동일한 타입의 데이터 0개 이상을 하나의 연속된 메모리 공간에서 관리하는 것

### Array 만들기 #1
- 타입[] 변수명; 또는 타입 변수명 []
- 변수의 타입과 저장하는 데이터의 타입

### 배열의 생성과 초기화
- 생성
  - new keyword와 함께 저장하려는 데이터 타입 및 길이 지정: new data_type[length]
    - new int[3]; int타입의 자료 3개를 저장할 수 있는 배열을 메모리에 생성
    - points = new int[3]: 생성된 배열을 points라는 변수에 할당
    - points는 메모리에 배열을 가리키는 reference 타입 변수

- 배열 요소의 초기화
  - 배열의 생성과 동시에 저장 대상 자료형에 대한 기본값으로 default 초기화 진행

  |자료형|기본값|비고|
  |:---:|:---:|:---:|
  |boolean|false||
  |char|'\u0000'|공백문자|
  |byte, short, int|0||
  |long|0L||
  |float|0.0f||
  |double|0.0||
  |`참조형 변수`|`null`|`아무것도 참조하지 않음`|

### 배열의 사용
- 배열은 index 번호를 가지고 각 요소에 접근 가능
  - index 번호는 0부터 시작
  - 배열의 길이: 배열이름.length로 배열의 크기 조회 가능
- for문을 통한 출력 대신 Arrays.toString() 사용 가능

### Array 만들기 #2
- 생성과 동시에 할당한 값으로 초기화
  - int[] b = new int[]{1,3,5,6,8};
  - int[] c = {1,3,5,6,8};
- 선언과 생성을 따로 처리할 경우 초기화 주의
  - int[] points;
    points = {1,3,4,6,8}; // 컴파일 오류
  - int[] points;
    points = new int[]{1,3,5,6,8}; // 선언할 때는 배열의 크기를 알 수 없을 때

### for-each with Array
- 가독성이 개선된 반복문으로, 배열 및 Collections에서 사용
- index 대신 직접 요소(element)에 접근하는 변수를 제공
  - naturally read only(copied value)
  - index를 사용하지 않을 수 있지만, 사용하지 못함. -> 용도에 따라 사용

### Array is Immutable
- 배열은 최초 메모리 할당 이후, 변경할 수 없음.
- 개별 요소는 다른 값으로 변경이 가능하나, 요소를 추가하거나 삭제할 수는 없음.

### 2차원 Array 만들기 #1
- int Type 기준으로 4x3 배열 만들기
- 선언
  - int [][] intArray;
  - int intArray [][];
  - int [] intArray [];

### 2차원 Array 만들기 #2
- 선언, 생성, 할당 동시에
  - int [][] intArray = {{},{},{}};

### 2차원 Array 만들기 #3
- int Type 기준으로 4x? 배열 만들기
  - int[][] intArray = new int[4][];
- 1차 Array만 생성 후, 필요에 따라 2차 배열을 생성함
  - intArray[0] = new int[3];
  - int Array[1] = new int[2];
  - intArray[2] = new int[]{1,2,3};