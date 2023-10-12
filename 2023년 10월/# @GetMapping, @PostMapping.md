# @GetMapping, @PostMapping
    @RequestMapping 에서 GET, POST를 더 간단히 사용할 수 있는 매핑


### servlet-context.xml -> 스프링의 웹 관련 설정파일

## RequestMapping의 URL패턴 (이전의 WebServlet에서도 함, 거의 비슷)
?는 한 글자, *는 여러 글자, **는 하위 경로 포함. 배열로 여러 패턴 지정
|종류|URL pattern|매칭 URL|
|:--:|:--:|:--:|
|1. exact mapping|/login/hello.do|http://localhost/ch2/login/hello.do|
|2. path mapping|/login/*|http://localhost/ch2/login/ 으로 시작되는 모든 것|
|3. extension mapping|*.do|.do로 끝나는 모든 것|

## URL인코딩 - 퍼센트 인코딩
    URL에 포함된 non-ASCII 문자를 문자 코드(16진수) 문자열로 변환
    