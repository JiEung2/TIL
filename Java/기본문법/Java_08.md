# Java_08
## IO & Stream

## 노드 스트림
### I/O와 Stream
- I/O? 데이터의 입력(input)과 출력(output)
- 데이터는 한쪽에서 주고 한쪽에서 받는 구조로 되어있음
    - 이 때 입력과 출력의 끝단: 노드(Node)
    - 두 노드를 연결하고 데이터를 전송할 수 있는 개념: 스트림(Stream)
        - 물의 흐름이나 전기의 흐름과 같은 개념
    - 스트림은 단방향으로만 통신이 가능하며 하나의 스트림으로 입력과 출력을 같이 처리할 수 없음
    - 입력 스트림: InputStrema, Reader
    - 출력 스트림: OutputStream, Writer
- Node stream: node에 연결되는 스트림  
![!\[Alt text\](image.png)](Java_08-1.png)

### InputStream의 주요 메서드
![!\[Alt text\](image.png)](Java_08-2.png)

### Reader의 주요 메서드
![!\[Alt text\](image.png)](Java_08-3.png)

### OutputStream
![!\[Alt text\](image.png)](Java_08-4.png)

### Writer
![!\[Alt text\](image.png)](Java_08-5.png)

### File
- 가장 기본적인 입출력 장치 중 하나로 파일과 디렉터리를 다루는 클래스  
![!\[Alt text\](image.png)](Java_08-6.png)  
![!\[Alt text\](image.png)](Java_08-7.png)

- 상대경로의 기준은 java program을 실행하는 위치(소스와 무관)
- 그래서 내가 어디에서 실행하느냐에 따라 다름


## 보조 스트림

### 보조 스트림: Filter Stream, Processing Stream
- 다른 스트림에 부가적인 기능을 제공하는 스트림
    - 문자 set 변환
    - Buffering
    - 기본 데이터 형의 전송
    - 객체 입출력
- 스트림 체이닝(Stream Chaining)
    - 필요에 따라 여러 보조 스트림을 연결해서 사용 가능

### 보조 스트림의 종류
|기능|byte 기반|char 기반|
|:---:|:---:|:---:|
|기능|byte 기반|char 기반|
|byte 스트림을 char 스트림으로 변환|InputStreamReader, OutputStreamWriter||
|버퍼링을 통한 속도 향상|BufferedInputStream, BufferedOutputStream|BufferedReader, BufferedWriter|
|객체 전송|ObjectInputStream, ObjectOutputStream||

- 생성 - 이전 스트림을 생성자의 파라미터에 연결
```java
new BufferedInputStream(System.in);

new ObjectInputStream(new BufferedInputStream(new FileInputStream()));
```

- 종료
    - 보조 스트림의 close()를 호출하면 노드 스트림의 close() 까지 호출 됨

### 사용할 스트림의 결정 과정
- 노드가 무엇인가 -> 타입은 문자열인가? 바이트인가? -> 방향이 무엇인가? (여기까진 노드 스트림 구성) -> 추가 기능이 필요한가? (보조 스트림 구성)
- 영화 파일을 빠른 속도로 이동시키고 싶다면?
    - File -> byte -> read, write -> FileInputStream, FIleOuntputStream -> BufferedInputStream, BufferedOutputStream
- 키보드에서 유니코드 문자를 안전하고 빠르게 읽고 싶다면?
    - Keyboard -> byte -> 읽기 -> InputStream System.in -> InputStreamReader -> BufferedReader (그래서 알고리즘 문제 풀 때 이 세 개 체이닝해서 사용)
- 메모리의 객체를 파일로 저장하고 싶다면?
    - File -> byte -> 쓰기 -> FileOutputStream -> OutputStream

### InputStreamReader & OuputStreamWriter
- 바이트 기반 스트림 char 기반으로 변경해주는 스트림
    - 문자열을 관리하기 위해서는 byte 단위보다 char 단위가 유리
    - 키보드에서 입력(byte stream) 받은 데이터를 처리할 경우 등
- 변환 시 encoding 지정 가능

### Buffered 계열
- 버퍼의 역할
- 스트림의 입/출력 효율을 높이기 위해 버퍼를 사용하는 스트림
- BufferedReader & BufferedWriter
    - BufferedReader: readLine() -> 줄 단위로 데이터를 읽어 들임

### 객체 직렬화(serialization)
- 객체를 파일 등에 저장하거나 네트워크로 전송하기 위해 연속적인 데이터로 변환하는 것
- 반대의 경우는 역 직렬화(deserialization)
    ![!\[Alt text\](image.png)](Java_08-8.png)
- 직렬화 되기 위한 조건
    - Serializable 인터페이스를 구현할 것
    - 클래스의 모든 멤버가 Serializable 인터페이스를 구현해야 함
    - 직렬화에서 제외하려는 멤버는 transient 선언

    ```java
    class Person implements Serializable { // -> 직렬화 필수 조건
        private String name;
        private int age;

        private transient String ssn; // -> 직렬화 제외
        private LoginInfo lInfo; // -> 직렬화 필요
    }
    ``` 

- serialVersionUID
    - 클래스의 변경 여부를 파악하기 위한 유일 키
    - 직렬화 할 때의 UID와 역 직렬화 할 때의 UID가 다를 경우 예외 발생
    - 직렬화되는 객체에 UID가 설정되지 않았을 경우 컴파일러가 자동 생성
        - 멤버 변경으로 인한 컴파일 시마다 변경 -> InvalidClassException

### Scanner와 BufferedReader
- char 형태의 데이터를 읽기위한 클래스들
- Scanner - 자동 형변환을 지원하는 등 사용이 간편하지만 속도가 느림
- BufferedReader - 직접 스트림을 구성해야 하는 등 번거롭지만 속도가 빠름

