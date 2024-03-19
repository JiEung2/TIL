## RDBMS
### RDBMS
- 관계형(Relational) 데이터베이스 시스템
- 테이블 기반(Table based)의 DBMS
    - 데이터를 테이블 단위로 관리  
        -> 하나의 테이블은 여러 개의 컬럼으로 구성
    - 중복 데이터를 최소화 시킴  
        -> 같은 데이터가 여러 컬럼 또는 테이블에 존재했을 경우, 데이터를 수정 시 문제가 발생할 가능성이 높아짐 - 정규화  
    - 여러 테이블에 분산되어 있는 데이터를 검색 시 테이블 간의 관계(join)를 이용하여 필요한 데이터를 검색
    
## SQL(Structured Query Language)
### SQL
- Database에 있는 정보를 사용할 수 있도록 지원하는 언어
- 모든 DBMS에서 사용 가능
- Query의 대소문자는 구분하지 않음(단, 데이터의 대소문자는 구분)
    - MySQL은 데이터도 대소문자 구분하지 않음(default 설정):: binary함수 이용
    
- SQL 구문은 DCL, DDL, DML로 구분함

### 구문 종류
- DML(Data Manipulation Language)
    - 개별적으로 Database 테이블에서 새로운 행을 입력하고, 기존의 행을 변경하고 제거
    - INSERT
    - UPDATE
    - DELETE
    - SELECT - Database로 부터 Data를 검색. SELECT 역시 DML로 분류
- DDL(Data Definition Language)
    - 테이블로부터 데이터 구조를 생성, 변경, 제거
    - CREATE
    - ALTER
    - DROP
    - RENAME
- TCL(Transaction Control Language)
    - DML 명령문으로 수행한 변경을 관리
    - COMMIT
    - ROLLBACK
- DCL(Data Control Language)
    - Database와 그 구조에 대한 접근권한을 제공하거나 제거
    - GRANT
    - REVOKE
    
### DDL
- 데이터베이스 생성  
    ```sql
    > create database 데이터베이스명;
    > create database 데이터베이스명
      default character set 값
      collate 값;
    ```
    - 다국어 처리(utf8mb3): dbtest생성  
        ```sql
        create database dbtest
        default character set utf8mb3 collate utf8mb3_general_ci;  
        ```
    - 이모지 문자까지 처리  
        ```sql
        create database dbtest
        default character set utf8mb4 collate utf8mb3_general_ci;  
        ```
      
    - Character set은 각 문자가 컴퓨터에 저장될 때 어떠한 코드로 저장될지에 대한 규칙의 집합을 의미
    - Collation은 특정 문자 셋에 의해 데이터베이스에 저장된 값들을 비교 검색하거나 정렬 등의 작업을 위해 문자들을 서로 비교할 때 사용하는 규칙들의 집합을 의미

- 데이터베이스 변경  
    ```sql
    > alter database 데이터베이스명
      default character set 값 collate 값;
    ```
    - dbtest의 character set, collate 변경
        ```sql
        > alter database dbtest
        default character set utf8mb4 collate utf8mb4_general_ci;
        ```
      
- 데이터베이스 삭제  
    - 데이터베이스 삭제
        ```sql
        > drop database 데이터베이스명;
        ```
        - 이름이 'dbtest'인 데이터베이스 삭제  
            ```sql
            drop database dbtest;
            ```
          
    - 데이터베이스 사용  
        ```sql
        > use 데이터베이스명;
        ```
            
        - 이름이 ssafydb인 데이터베이스 사용  
            ```sql
            use ssafydb;
            ```
    