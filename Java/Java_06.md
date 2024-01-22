# Java_06

## 예외 처리
### 에러와 예외
- 어떤 원인에 의해 오동작 하거나 비정상적으로 종료되는 경우
- 심각도에 따른 분류
||Error|Exception|
|:---:|:---:|:---:|
|상황|프로그램을 잘못 작성한 경우|프로그램을 잘못 작성한 경우, 프로그램의 작성 의도와 달리 사용되는 경우|
|대처|디버깅으로 코드 개선|디버깅으로 코드 개선, 예외 처리 코드로 상황 수습|
|예|메모리 부족, Stack Overflow등|null인 객체의 사용, 1/0, 읽으려는 파일이 없음|
- exception handling(예외 처리)란
    - 예외 발생 시 프로그램의 비 정상 종료를 막고 정상적인 실행 상태를 유지하는 것
        - 예외의 감지 및 예외 발생 시 동작할 코드 작성 필요

### 예외 클래스의 계층
![!\[Alt text\](image.png)](Java_06-1.png)
- Error 계열
- Checked exception 계열
    - 예외에 대한 대처 코드가 없으면 컴파일이 진행되지 않음
- Unchecked exception 계열
    - 예외에 대한 대처 코드가 없더라도 컴파일은 진행됨

## 예외 처리 기법
### try ~ catch 구문
```java
try{
    //예외가 발생할 수 있는 코드
}catch(XXException e){ //던진 예외를 받음
    //예외가 발생했을 때 처리할 코드
}
```

### Exception 객체의 정보 활용
- Throwable의 주요 메서드
    - public String getMessage(): 발생된 예외에 대한 구체적인 메시지를 반환
    - public Throwable getCause(): 예외의 원인이 되는 Throwable 객체 또는 null을 반환
    - *public void printStackTrace(): 예외가 발생된 메서드가 호출되기까지의 메서드 호출 스택을 출력. 디버깅의 수단으로 주로 사용됨

### try-catch 문에서의 흐름
- try 블록에서 예외가 발생하면
    - JVM이 해당 Exception 클래스의 객체 생성 후 던짐(throw)
        - throw new XXException()
    - 던져진 exception을 처리할 수 있는 catch 블록에서 받은 후 처리
        - 적당한 catch 블록을 만나지 못하면 예외처리는 실패
    - 정상적으로 처리되면 try-catch 블록을 벗어나 다음 문장 진행
- try 블록에서 어떠한 예외도 발생하지 않은 경우
    - catch문을 거치지 않고 try-catch 블록의 다음 흐름 문장을 실행

```java
try{
    문제 발생 가능 코드
    일반코드
} catch (XXException e){
    예외 처리 코드
}
일반 코드
```
- 예외 발생이 없을 때: 문제 발생 가능 코드 -> 일반 코드 -> 일반 코드
- 예외가 발생할 때: 문제 발생 가능 코드 -> throw new XXException() -> catch(XXException e) -> 예외 처리 코드 -> 일반 코드

### Checked Exception 처리
- 처리하지 않으면 컴파일 불가

### 다중 exception handling
- try 블록에서 여러 종류의 예외가 발생할 경우
    - 하나의 try 블록에 여러 개의 catch 블록 추가 가능
        - 예외 종류별로 catch 블록 구성
        ```java
        try{
            // exception이 발생할 만한 코드
        } catch (XXException e){
            // XXException 발생 시 처리 코드
        }catch (YYException e){
            // YYException 발생 시 처리 코드
        } catch (Exception e){
            // Exception 발생 시 처리 코드
        }
        ```
        - 여기에서도 다형성 적용 가능 exception이 다른 예외 포용 가능
        - 밑의 코드에선 전부 Exception에서 걸림
        ```java
        try{
            // exception이 발생할 만한 코드
        } catch (Exception e){
            // Exception 발생 시 처리 코드
        }catch (XXException e){
            // XXException 발생 시 처리 코드
        }catch (YYException e){
            // YYException 발생 시 처리 코드
        } 
        ```
- 다중 catch 문장 작성 순서 유의 사항
    - JVM이 던진 예외는 catch문장을 찾을 때는 다형성이 적용됨
    - 상위 타입의 예외가 먼저 선언되는 경우 뒤에 등장하는 catch 블록은 동작할 기회가 없음
        - Unreachable catch block for Exception
    - 상속 관계가 없는 경우는 무관
    - 상속 관계에서는 작은 범위(자식)에서 큰 범위(조상)순으로 정의

### 다중 예외 처리를 이용한 Checked Exception 처리
![!\[Alt text\](image.png)](Java_06-2.png)
- 발생하는 예외들을 하나로 처리하기
    ```java
    try{
        //다중 예외 발생 코드
    } catch(Exception e){
        System.out.printf("예외 발생: %s%n", e.getMessage());
    }
    ```
    - 예외 상황 별 처리가 쉽지 않음
    - 가급적 예외 상황 별로 처리하는 것을 권장
- 심각하지 않은 예외를 굳이 세분화 해서 처리하는 것도 낭비
    - `|`를 이용해 하나의 catch 구문에서 상속관계가 없는 여러 개의 exception 처리
    ```java
    public void exceptionHandling() {
        try{
            Class.forName("abc.Def");
            new FileInputStream("Hello.java");
            DriverManager.getConnection("Hello");
        } catch (ClassNotFoundException | FileNotFoundException e){
            System.out.printf("자원을 찾을 수 없습니다.: %s%n", e.getMEssage());
        } catch (SQLException e){
            System.out.printf("DB 접속 실패: %s%n", e.getMessage());
        }
        System.out.println("프로그램 정상 종료");
    }
    ```

### 다중 exception handling를 이용한 Checked Exception 처리
![!\[Alt text\](image.png)](Java_06-3.png)