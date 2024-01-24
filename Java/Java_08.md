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