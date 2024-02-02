# Java_07
## Collection Framework
### 자료구조
- 자료구조는 컴퓨터 과학에서 효율적인 접근 및 수정을 가능하게 하는 자료의 조직, 관리, 저장을 의미한다. 
더 정확히 말해, 자료구조는 데이터 값의 모임, 또 데이터 간의 관계, 그리고 데이터에 적용할 수 있는 함수나 명령을 의미한다.

### 배열
- 가장 기본적인 자료 구조
- homogeneous collection: 동일한 데이터 타입만 관리 가능
    - 타입이 다른 객체를 관리하기 위해서는 매번 다른 배열 필요
- Polymorphism
    - Object를 이용하면 모든 객체 참조 가능 -> Collection Framework
    - 담을 때는 편리하지만 빼낼 때는 Object로만 가져올 수 있음
    - 런타임에 실제 객체의 타입 확인 후 사용해야 하는 번거러움
- Generic을 이용한 타입 한정
    - 컴파일 타임에 저장하려는 타입 제한 -> 형변환의 번거로움 제거

### Collection Framework
- java.util 패키지
    - 다수의 데이터를 쉽게 처리하는 방법 제공 -> DB처럼 CRUD 기능 중요
- collection framework 핵심 interface  
|interface|특징|
|:---:|:---:|
|List|입력 순서가 있는 데이터의 집합. 순서가 있으니까 데이터의 중복을 허락, ex) 일렬로 줄 서기, ArrayList, LinkedList|
|Set|입력 순서를 유지하지 않는 데이터의 집합. 순서가 없어서 같은 데이터를 구별할 수 없음 -> 중복 허락하지 않음, HashSet, TreeSet...|
|Map|key와 value의 쌍으로 데이터를 관리하는 집합. 순서는 없고 keydml wndqhr qnfrk, value는 중복 자능, HashMap, TreeMap|

### Collection interface
CRUD
|분류|Collection|
|:---:|:---:|
|추가|add(E e), addAll(Collection<? extends E> c)|
|조회|contains(Object o), containsAll(Collection<?> c), equals(), isEmpty(), iterator(), size(), clear(), remove(Object o), removeAll(Collection<?> c)|
|삭제||
|수정||
|기타|toArray()|

## List
### 특징
- 입력 순서가 있는 데이터의 집합
- 입력 순서가 있으므로 데이터의 중복을 허락
- 관련 클래스 관계도  
    ![!\[Alt text\](image.png)](Java_07-1.png)

### 주요 메서드
- 추가: add(int index, E element), addAll(int index, Collection<? extends E> c)
- 조회: get(int index), indexOf(Object o), lastIndexOf(Object o), listIterator()
- 삭제: remove(int index)
- 수정: set(int index, E element)
- 기타: subList(int fromIndex, int toIndex)

### 배열과 ArrayList
- 배열의 장점
    - 가장 기본적인 형태의 자료 구조로 간단하며 사용이 쉬움
    - 접근 속도가 빠름
- 배열의 단점
    - 크기를 변경할 수 없어 추가 데이터를 위해 새로운 배열을 만들고 복사해야 함
    - 비 순차적 데이터의 추가, 삭제에 많은 시간이 걸림
- 배열을 사용하는 ArrayList도 태생적으로 배열의 장단점을 그대로 가져감

### LinkedList
- 각 요소를 Node로 정의하고 Node는 다음 요소의 참조 값과 데이터로 구성됨
    - 각 요소가 다음 요소의 링크 정보를 가지며 연속적으로 구성될 필요가 없다.  
    ![!\[Alt text\](image.png)](Java_07-3.png)
- 데이터 삭제 및 추가  
    ![!\[Alt text\](image.png)](Java_07-2.png)

### LinkedList와 ArrayList의 용도
|구분|순차 추가/수정/삭제|비 순차 추가/수정/삭제|조회|
|:---:|:---:|:---:|:---:|
|ArrayList|빠름|느림|빠름|
|LinkedList|느림|빠름|느림|

- 결론
    - 특정 클래스가 좋고 나쁨이 아니라 용도에 적합하게 사용해야 함
    - 소량의 데이터를 가지고 사용할 경우는 큰 차이가 없음
    - 정적인 데이터 활용, 단순한 데이터 조회용: ArrayList
    - 동적인 데이터 추가, 삭제가 많은 작업: LinkedList

## Set
### Set interface
- 특징
    - 입력 순서를 관리하지 않고 주머니에 구슬(데이터)를 넣는 형태
    - 데이터를 구별할 순서(index)가 없어 중복이 허용되지 않는다.
        - 효율적인 중복 데이터 제거 수단
    - 관련 클래스 관계도  
    ![!\[Alt text\](image.png)](Java_07-4.png)

- set에서는 같은 데이터의 중복을 허용하지 않는데 만약 같은 클래스의 같은 값을 가지는 객체를 두 개 생성해서 set에 삽입 시 둘 다 들어가게됨.
- ex) Phone p1 = new SmartPhone("010");, Phone p2 = new SmartPhone("010");
- 이런식으로 p1, p2를 set에 넣으면 둘 다 들어감.
- 해시코드가 다르기 때문에 객체가 서로 다른 객체로 인식됨.
- 그래서 일단 해당 클래스에서 equals 메서드를 오버라이딩 해서 번호가 같으면 같은 객체로 인식하도록 하고
- 해시 코드도 오버라이딩 해서 같다고 해줘야 함.
- `동일한 데이터의 기준은 객체의 equals()가 true를 리턴하고 hashCode() 값이 같을 것`

## Map 계열
### Map interface
- 특징
    - Key와 Value를 하나의 Entry로 묶어서 데이터 관리
        - Key: Object 형태로 데이터 중복을 허락하지 않음
        - Value: Object 형태로 데이터 중복이 허락 됨
    - 관련 클래스 관계도  
    ![!\[Alt text\](image.png)](Java_07-5.png)

### Map interface의 주요 메서드
- 추가: put(K key, V value), putAll(Map<? extends K, ? extends V> m)
- 조회: containsKey(Object key), containsValue(Object value), entrySet(), keySet(), get(Object key), values(), size(), isEmpty()
- 삭제: clear(), remove(Object key)
- 수정: put(K key, V value), putAll(Map<? extends K, ? extends V> m)

### 정렬
- 요소를 특정 기준에 대한 내림차순 또는 오름차순으로 배치 하는 것
- 순서를 가지는 Collection들만 정렬 가능
    - List 계열
    - Set에서는 SortedSet의 자식 객체
    - Map에서는 SortedMap의 자식 객체(key 기준)

- Collections의 sort()를 이용한 정렬
    - sort(List<T> list)
        - 객체가 Comparable을 구현하고 있는 경우 내장 알고리즘을 통해 정렬

- Comparable interface
```java
public interface Comparable<T> {
    public int compareTo(T o);
}
```
```
양수: 자리 바꿈
음수: 자리 유지
0: 동일 위치
```

### Comparator의 활용
- 객체가 Comparable을 구현하고 있지 않거나 사용자 정의 알고리즘으로 정렬하려는 경우
    - String을 알파벳 순이 아닌 글자 수 별로 정렬하려면?
- sort(List<T> list, Comparator<? Super T> c)