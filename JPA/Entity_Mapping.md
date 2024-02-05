# 엔티티 매핑

## 엔티티 매핑 소개
- 객체와 테이블 매핑: @Entity, @Table
- 필드와 컬럼 매핑: @Column
- 기본 키 매핑: @Id
- 연관관계 매핑: @ManyToOne, @JoinColumn

## 객체와 테이블 매핑
### @Entity
- @Entity가 붙은 클래스는 JPA가 관리, 엔티티라 한다.
- JPA를 사용해서 테이블과 매핑할 클래스는 @Entity 필수
- 주의
  - `기본 생성자 필수`(파라미터가 없는 public 또는 Protected 생성자)
  - final 클래스, enum, interface, inner 클래스 사용X
  - 저장할 필드에 final 사용X
- @Table(name = " ") 애노테이션으로 테이블 명을 지정할 수 있음.

## 데이터베이스 스키마 자동 생성
- DDL을 애플리케이션 실행 시점에 자동 생성
- 테이블 중심 -> 객체 중심
- 데이터베이스 방언을 활용해서 데이터베이스에 맞는 적절한 DDL 생성
- 이렇게 생성된 DDL은 개발 장비에서만 사용
- 생성된 DDL은 운영서버에서는 사용하지 않거나, 적절히 다듬은 후 사용

### 데이터베이스 스키마 자동 생성 - 속성
**hibernate.hbm2ddl.auto**
|옵션|설명|
|:---:|:---:|
|create|기존테이블 삭제 후 다시 생성(DROP + CREATE)|
|create-drop|create와 같으나 종료시점에 테이블 DROP|
|update|변경분만 반영(운영DB에는 사용하면 안됨)|
|validate|엔티티와 테이블이 정상 매핑되었는지만 확인|
|none|사용하지 않음|

### 데이터베이스 스키마 자동 생성 - 주의
- `운영 장비에는 절대 create, create-drop, update 사용하면 안됨`
- 개발 초기 단계는 create 또는 update
- 테스트 서버는 update 또는 validate
- 스테이징과 운영 서버는 validate 또는 none

### 매핑 어노테이션 정리
|어노테이션|설명|
|:---:|:---:|
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
