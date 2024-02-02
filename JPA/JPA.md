### JPA란

- Java persistence API
- 자바 진영의 ORM 기술 표준

### ORM란

- Object-relational mapping(객체 관계 매핑(
- 객체는 객체대로 설계
- 관계형 데이터베이스는 관계형 데이터베이스대로 설계
- ORM 프레임워크가 중간에서 매핑
- 대중적인 언어에는 대부분 ORM 기술이 존재

### JPA는 애플리케이션과 JDBC 사이에서 동작

- JPA 동작 - 저장

![Alt text](<스크린샷 2024-01-14 오후 9.54.00.png>)

- JPA 동작 - 조회

![Alt text](<스크린샷 2024-01-14 오후 9.54.47.png>)

### JPA는 표준 명세

- JPA는 인터페이스의 모음
- JPA 2.1 표준 명세를 구현한 3가지 구현체
- 하이버네이트, EclipseLink, DataNucleus

→ 우리는 그냥 JPA의 하이버네이트를 쓴다라고 생각하면 됨.

### JPA를 왜 사용해야 하는가?

- SQL 중심적인 개발에서 객체 중심으로 개발
- 생산성
- 유지보수
- 패러다임의 불일치 해결
- 성능
- 데이터 접근 추상화와 벤더 독립성
- 표준

### 생산성 - JPA와 CRUD

- 저장: **jpa.persist**(member)
- 조회: Member member = **jpa.find**(memberId)
- 수정: **member.setName**(”변경할 이름”)
- 삭제: **jpa.remove**(member)

### 유지보수

- 기존: 필드 변경시 모든 SQL 수정

![Alt text](<스크린샷 2024-01-14 오후 10.04.41.png>)

- JPA: 필드만 추가하면 됨, SQL은 JPA가 처리

![Alt text](<스크린샷 2024-01-14 오후 10.05.15.png>)

### JPA와 패러다임의 불일치 해결

1. JPA와 상속
2. JPA와 연관관계
3. JPA와 객체 그래프 탐색
4. JPA와 비교하기

### JPA와 비교하기

![Alt text](<스크린샷 2024-01-14 오후 10.08.29.png>)

### JPA의 성능 최적화 기능

1. 1차 캐시와 동일성(identity) 보장
2. 트랜잭션을 지원하는 쓰기 지연(transactional write-behind)
3. 지연 로딩(Lazy Loading)

- **1차 캐시와 동일성 보장**
    1. 같은 트랜잭션 안에서는 같은 엔티티를 반환 - 약간의 조회 성능 향상
    2. DB Isolation Level이 Read Commit이어도 애플리케이션에서 Repeatable Read 보장
- **트랜잭션을 지원하는 쓰기 지연 - INSERT**
    1. 트랜잭션을 커밋할 때까지 INSERT SQL을 모음
    2. JDBC BATCH SQL 기능을 사용해서 한번에 SQL 전송
    
    ![Alt text](<스크린샷 2024-01-14 오후 10.12.04.png>)
    
- **트랜잭션을 지원하는 쓰기 지연 - UPDATE**
    1. UPDATE, DELETE로 인한 로우(ROW)락 시간 최소화
    2. 트랜잭션 커밋 시 UPDATE, DELETE SQL 실행하고, 바로 커밋
- **지연 로딩과 즉시 로딩**
    - 지연 로딩: 객체가 실제 사용될 때 로딩
    - 즉시 로딩: JOIN SQL로 한번에 연관된 객체까지 미리 조회
    
    ![Alt text](<스크린샷 2024-01-14 오후 10.14.03.png>)

### 매핑 어노테이션 정리
|어노테이션|설명|
|:---:|:---:|:---:|
|@Column|컬럼 매핑|
|@Temporal|날짜 타입 매핑|
|@Enumerated|enum 타입 매핑|
|@Lob|BLOB, CLOB 매핑|
|@Transient|특정 필드를 컬럼에 추가하지 않고 메모리에서만 사용, 임시 데이터|

### Column
|속성|설명|기본값|
|:---:|:---:|:---:|
|name|필드와 매핑할 테이블의 컬럼 이름|객체의 필드 이름|
|insertable, updatable|등록, 변경 가능 여부|TRUE|
|nullable|null 값의 허용 여부를 설정한다. false로 설정하면 DDL 생성 시에 not null 제약 조건이 붙는다.||
|unique|@Table의 uniqueConstraints와 같지만 한 컬럼에 간단히 유니크 제약조건을 걸 때 사용한다.||
|columnDefinition|데이터베이스 컬럼 정보를 직접 줄 수 있다. ex) varchar(100) default 'EMPTY'|필드의 자바 타입과 방언 정보를 사용해|
|length(DDL)|문자 길이 제약조건, String 타입에만 사용한다.|255|
|precision, scale(DDL)|BigDecimal 타입에서 사용한다.(BigInteger도 사용 가능). precision은 소수점을 포함한 전체 자릿수를 scale은 소수의 자릿수다. 참고로 double, float 타입에는 적용되지 않는다. (덜 작성)|precision=19,|

### @Enumerated
enum 타입을 매핑할 때 사용
