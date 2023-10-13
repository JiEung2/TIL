# 라이브러리에 대해 알아보자

## 스프링 부트 라이브러리
- spring-boot-starter-web
    - spring-boot-starter-tomcat: 톰캣(웹서버)
    - spring-webmvc: 스프링 웹 MVC
- spring-boot-thymeleaf: 타임리프 템플릿 엔진(View)
- spring-boot-starter(rhdxhd): 스프링 부트 + 스프링 코어 + 로깅
    - spring-boot
        - spring-core
    - spring-boot-starter-logging
        - logback, slf4j
        - logback과 slf4j에 관해서는 검색 한번 하자! 실무에서는 sout으로 출력하면 안되고, 로그에 남겨야함 그래서 이 라이브러리들을 사용

## 테스트 라이브러리
- spring-boot-starter-test
    - junit: 테스트 프레임워크
    - mockito: 목 라이브러리
    - assertj: 테스트 코드를 좀 더 편하게 작성하게 도와주는 라이브러리
    - spring-test: 스프링 통합 테스트 지원