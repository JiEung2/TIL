# 영속성 컨텍스트
- JPA를 이해하는데 가장 중요한 용어
- "엔티티를 영구 저장하는 환경"이라는 뜻
- `EntityManager.persis(entity);` -> 엔티티를 DB가 아니라 영속성 컨텍스트에 저장하겠다는 것

- 영속성 컨텍스트는 논리적인 개념
- 눈에 보이지 않음
- 엔티티 매니저를 통해서 영속성 컨텍스트에 접근

### J2SE 환경
- 엔티티 매니저와 영속성 컨텍스트가 1:1
  ![!\[Alt text\](image.png)](Persistence_Context-01.png)

## 엔티티의 생명주기
- 비영속(new/transient)
  영속성 컨텍스와 전혀 관계가 없는 새로운 상태
- 영속(managed)
  영속성 컨텍스트에 관리되는 상태
- 준영속(detached)
  영속성 컨텍스트에 저장되었다가 분리된 상태
- 삭제(removed)
  삭제된 상태

### 비영속
```java
//객체를 생성한 상태(비영속)
Member member = new Member();
member.setId("member1");
member.setUsername("회원1");
```

### 영속
```java
Member member = new Member();
member.setId("member1");
member.setUsername("회원1");

EntityManager em = emf.createEntityManager();
em.getTransaction().begin();

//객체를 저장한 상태(영속)
em.persist(member);
```

### 준영속, 삭제
```java
//회원 엔티티를 영속성 컨텍스트에서 분리, 준영속 상태
em.detach(member);

//객체를 삭제한 상태(삭제)
em.remove(member);
```

### 영속성 컨텍스트의 이점
- 1차 캐시
- 동일성(identity) 보장
- 트랜잭션을 지원하는 쓰기 지연(transactional write-behind)
- 변경 감지(Dirty Checking)
- 지연 로딩(Lazy Loading)

### 엔티티 조회, 1차 캐시

### 1차 캐시에서 조회
```java
Member member = new Member();
member.setId("member1");
member.setUsername("회원1");

//1차 캐시에 저장됨
em.persist(member);

//1차 캐시에서 조회
Member findMember = em.find(Member.class, "member1");
```
- persist를 하게되면 영속 컨텍스트(entity Manager)에 1차 캐시라는 것이 생기고, member1이라는 키와 member 객체 자체가 값으로 들어가게 됨
- 영속 컨텍스트와 엔티티 매니저를 지금은 같다고 생각해도 괜찮, 하지만 미묘하게 다름
- 위의 findMember를 하게되면, 1차 캐시에서 조회한다는 이점이 있음
- 1차 캐시에서 조회하면 당연히 DB에 SELECT 쿼리문이 안나감

### 데이터베이스에서 조회
```java
Member findMember2 = em.gind(Member.class, "member2");
```
- 조회를 할 때 1차캐시에 없으면 DB에서 조회함
- 조회한 후 1차 캐시에 값을 저장하고, 그 다음 반환
- 1차 캐시는 정말 데이터베이스 한 트랜잭션 안에서만 효과가 있기 때문에 사실 막 그렇게 성능의 이점을 크게 얻을 수 있는 장점은 없음
- 그래도 비즈니스 로직이 굉장히 복잡한 경우에는 도움이 될 때가 있음

### 영속 엔티티의 동일성 보장
```java
Member a = em.find(Member.class, "member1");
Member b = em.find(Member.class, "member1");

System.out.println(a == b); //동일성 비교 true
```
- 1차 캐시로 반복 가능한 읽기(REPEATABLE READ) 등급의 트랜잭션 격리 수준을 데이터베이스가 아닌 애플리케이션 차원에서 제공

### 엔티티 등록 - 트랜잭션을 지원하는 쓰기 지연
```java
EntityManager em = emf.createEntityManager();
EntityTransaction transaction = em.getTransaction();
//엔티티 매니저는 데이터 변경 시 트랜잭션을 시작해야함.
transaction.begin(); //트랜잭션 시작

em.persist(memberA);
em.persist(memberB);
//여기까지 INSERT SQL을 데이터베이스에 보내지 않는다.
//영속성 컨텍스트에 차곡차곡 쌓아두기만함.

//커밋하는 순간 데이터베이스에 INSERT SQL을 보낸다.
transaction.commit(); //트랜잭션 커밋
```

### 엔티티 수정 - 변경 감지(Dirty Checking)
수정하고 persist를 할 필요가 없음.  
0. 값을 가져와서 수정
1. flush()
2. 엔티티와 스냅샷을 비교함
3. UPDATE SQL을 생성해서 쓰기 지연 SQL 저장소에 만들어둠.
4. flush() -> 업데이트 쿼리를 데이터베이스에 반영을하고
5. commit()

## flush(플러시)
영속성 컨텍스트의 변경내용을 데이터베이스에 반영

### 플러시 발생
데이터베이스 트랜지션이 커밋되면 플러시가 자동으로 발생한다고 보면 됨

- 변경 감지
- 수정된 엔티티 쓰기 지연 SQL 저장소에 등록
- 쓰기 지연 SQL 저장소의 쿼리를 데이터베이스에 전송(등록, 수정, 삭제 쿼리)

### 영속성 컨텍스트를 플러시하는 방법
쓸 일은 테스트 말고 거의 쓸 일이 없음. 이 데이터를 미리 데이터베이스에 반영을 하고 싶거나 미리 보고 싶을 때 em.flush()를 직접 호출하여 사용
- em.flush() - 직접 호출
- 트랜잭션 커밋 - 플러시 자동 호출
- JPQL 쿼리 실행 - 플러시 자동 호출

### JPQL 쿼리 실행시 플러시가 자동으로 호출되는 이유

```java
em.persist(memberA);
em.persist(memberB);
em.persist(memberC);

//중간에 JPQL 실행
query = em.createQuery("select m from Member m", Member.class);
List<Member> members = query.getResultList();
```
위와 같은 코드에서 jpql 쿼리가 날아가면 현재 memberA,B,C는 데이터베이스에 반영되지 않은 상태이기 때문에 쿼리문에서 오류가 날 수 있음. 그렇기 때문에 그러한 에러를 방지하기 위해 자동으로 플러시를 호출해줌.

### 플러시는!
- 영속성 컨텍스트를 비우지 않음
- 영속성 컨텍스트의 변경내용을 데이터베이스에 동기화
- 트랜잭션이라는 작업 단위가 중요 -> 커밋 직전에만 동기화 하며 됨

## 준영속 상태
- 영속 -> 준영속
- 영속 상태의 엔티티가 영속성 컨텍스트에서 분리(detached)
- 영속성 컨텍스트가 제공하는 기능을 사용 못함

### 준영속 상태로 만드는 방법
- em.detach(entity)
  - 특정 엔티티만 준영속 상태로 전환
- em.claer()
  - 영속성 컨텍스트를 완전히 초기화
- em.close()
  - 영속성 컨텍스트를 종료