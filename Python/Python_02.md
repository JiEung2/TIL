# Python 02

## Data Types

### list
여러 개의 값을 순서대로 저장하는 `변경 가능한` 시퀀스 자료형, 배열이랑 같음.

### 리스트 표현
- 0개 이상의 객체를 포함하여 데이터 목록을 저장
- 대괄호([])로 표기
- 데이터는 어떤 자료형도 저장할 수 있음
```python
my_list_1 = []

my_list_2 = [1, 'a', 3, 'b', 5]

my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
```

### 리스트의 시퀀스 특징
```python
my_list = [1, 'a', 3, 'b', 5]

# 인덱싱
print(my_list[1]) # a

# 슬라이싱
print(my_list[2:4]) # [3, 'b']
print(my_list[:3]) # [1, 'a', 3]
print(my_list[3:]) # ['b' , 5]
print(my_list[0:5:2]) # [1, 3, 5]
print(my_list[::-1]) # [5, 'b', 3, 'a', 1]

# 길이
print(len(my_list)) # 5
```

### 중첩된 리스트 접근
- 출력 값 예상해보기
```python
my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]

print(len(my_list)) # -> 5
print(my_list[4][-1]) # -> !!!
print(my_list[-1][1][0]) # -> w
```

### 리스트는 가변 (변경 가능)
```python
my_list = [1, 2, 3]
my_list[0] = 100

print(my_list) # [100, 2, 3]
```

### tuple(튜플)
여러 개의 값을 순서대로 저장하는 `변경 불가능한` 시퀀스 자료형

### 튜플 표현
- 0개 이상의 객체를 포함하며 데이터 목록을 저장
- `소괄호(())로 표기`
- 데이터는 어떤 자료형도 저장할 수 있음

```python
my_tuple_1 = ()

my_tuple_2 = (1,) # 얘는 틀린게 아니라 튜플로 표현하기 위해서는 ','를 붙여줘야함. 안붙여주면 그냥 정수 1이 되어버림.

my_tuple_3 = (1, 'a', 3, 'b', 5)
```

### 튜플의 시퀀스 특징
- 리스트랑 똑같음
- 다만 표현이 소괄호로 이루어짐
```python
my_list = (1, 'a', 3, 'b', 5)

# 인덱싱
print(my_list[1]) # a

# 슬라이싱
print(my_list[2:4]) # (3, 'b')
print(my_list[:3]) # (1, 'a', 3)
print(my_list[3:]) # ('b' , 5)
print(my_list[0:5:2]) # (1, 3, 5)
print(my_list[::-1]) # (5, 'b', 3, 'a', 1)

# 길이
print(len(my_list)) # 5
```

### 튜플은 불변 (변경 불가)

```python
my_tuple = (1, 'a', 3, 'b', 5)

# TypeError: 'tuple' object does not support item assignment
my_tuple[1] = 'z'
```

### 튜플은 어디에 쓰일까?
- 튜플의 불변 특성을 사용한 안전하게 여러 개의 값을 전달, 그룹화, 다중 할당 등
  `개발자가 직접 사용하기 보다 '파이썬 내부 동작'에서 주로 사용됨`

  ```python
  x, y = (10, 20)

  print(x)
  print(y)

  # 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능
  x, y = 10, 20
  ```

### range
연속된 정수 시퀀스를 생성하는 `변경 불가능한` 자료형

### range 표현
- range(n)
  - 0부터 n-1까지의 숫자 시퀀스
- range(n, m)
  - n부터 m-1까지의 숫자 시퀀스

  ```python
  my_range_1 = range(5)
  my_range_2 = range(1, 10)

  print(my_range_1) # range(0, 5)
  print(my_range_2) # range(1, 10)
  ```

- range를 print하면 0,1,2,3,4 이렇게 보이는게 아니라 위 주석처럼 보임
- 그래서 range는 주로 반복문과 함께 사용
  ```python
  # 리스트로 형 변환 시 데이터 확인 가능
  print(list(my_range_1)) # [0, 1, 2, 3, 4]
  print(list(my_range_2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

## Non-sequence Types
### dict(딕셔너리)
`key - value` 쌍으로 이루어진 `순서와 중복이 없는` `변경 가능한` 자료형

### 딕셔너리 표현
- key는 변경 불가능한 자료형만 사용 가능(str, int, float, tuple, range ...)
- value는 모든 자료형 사용 가능
- 중괄호`{}`로 표기

```python
my_dict_1 = {}
my_dict_2 = {'key':'value'}
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict_1) # {}
print(my_dict_2) # {'key': 'value'}
print(my_dict_3) # {'apple': 12, 'list': [1, 2, 3]}
```

### 딕셔너리 사용
- key를 통해 value에 접근
- key는 변경을 못하지만 value는 변경 가능
- 중복이 안됨
```python
my_dict = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict['apple']) # 12
print(my_dict['list']) # [1, 2, 3]

# 값 변경
my_dict['apple'] = 100
print(my_dict) # {'apple': 100, 'list': [1, 2, 3]}
```

### set
`순서와 중복이 없는` `변경 가능한 자료형`
- 수학에서의 집합과 동일한 연산 처리 가능
- 중괄호`{}`로 표기, 딕셔너리와 표기가 겹치지만 key,value의 쌍이 아니라 괜찮음
- 다만 빈 값의 세트를 만들기 위해서는 set()를 호출해주어야함.
```python
my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1) # set()
print(my_set_2) # {1, 2, 3} -> 순서가 없기 때문에 인덱스도 없음, 이것도 순서로 표시된건 아님
print(my_set_3) # {1} -> set를 만들 때 같은 값으로 만들면 중복이 없기 때문에 하나만 나옴
```

### 세트의 집합 연산
```python
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2) # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2) # {1, 2}

# 교집합
print(my_set_1 & my_set_3) # {3}
```

## Other Types

### None
파이썬에서 '값이 없음'을 표현하는 자료형

### None 표현
```python
variable = None

print(variable) # None
```

### Boolean
참(True)과 거짓(False)을 표현하는 자료형

### Boolean 표현
- 비교 / 논리 연산의 평가 결과로 사용됨
- 주로 조건 / 반복문과 함께 사용
```python
bool_1 = True
bool_2 = False

print(bool_1) # True
print(bool_2) # False
print(3 > 1) # True
print('3' != 3) # True
```

## Collection
여러 개의 항목 또는 요소를 담는 자료 구조 (str, list, tuple, set, dict)

|컬렉션|변경 가능 여부|순서 여부|
|:---:|:---:|:---:|
|str|X|O|
|list|O|O|
|tuple|X|O|
|set|O|X|
|dict|O|X|

## Type Conversion
### 암시적 형변환(Implicit Type conversion)
파이썬이 자동으로 형변환을 하는 것
### 암시적 형변환 예시
- Boolean과 Numeric Type에서만 가능
```python
print(3 + 5.0) # 8.0

print(True + 3) # 4

print(True + False) # 1
```

### 명시적 형변환(Explicit Type conversion)
개발자가 직접 형변환을 하는 것, 암시적 형변환이 아닌 경우를 모두 포함
### 명시적 형변환 예시
- str -> integer : 형식에 맞는 숫자만 가능
- integer -> str : 모두 가능
```python
print(int('1')) # 1

print(str(1) + '등') # 1등

print(float('3.5')) # 3.5

print(int(3.5)) # 3

# ValueError: invalid literal for int() with base 10: '3.5'
print(int('3.5'))
```

### 컬렉션 간 형변환 정리!
![\[Alt text\](image.png)](Python_02-1.png)

## 연산자
### 산술 연산자
- 내가 알고있는 그 기본 연산자들
- `+`, `-`, `//`, `**` 등등

### 복합 연산자
- 연산과 할당이 함께 이루어지는 그 연산자들
- `+=`, `//=`, `**=`, `%=` 등등

### 비교 연산자
- 내가 알고있는 그 비교 연산자들
- `<`, `>=`, `is`, `is not` 등등

### is 비교 연산자
- 메모리 내에서 같은 객체를 참조하는지 확인
- ==는 동등성(equality), is는 식별성(identity)
- 값을 비교하는 ==와 다름
- is -> 같음
- is not -> 같지 않음

```python
# SyntaxWarning
# ==은 값(데이터)을 비교하는 것이지만 is 레퍼런스(주소)를 비고하기 때문
# is 연산자는 되도록이면 None, True, False 등을 비교할 때 사용
print(2.0 is 2) # False
```

### 논리 연산자
|기호|연산자|내용|
|:---:|:---:|:---:|
|and|논리곱|두 피연산자 모두 True인 경우에만 전체 표현식을 True로 평가|
|or|논리합|두 피연사 중 하나라도 True인 경우 전체 표현식을 True로 평가|
|not|논리부정|단일 피연산자를 부정|
- 비교 연산자와 함께 사용 가능

### 단축평가
논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작

### 단축평가 예시 문제
```python
vowels = 'aeiou'

print(('a' and 'b') in vowels) # False a가 true라서 b까지 가야됨 그래서 b
print(('b' and 'a') in vowels) # True b가 true라서 a까지 가야됨 그래서 a

print(3 and 5) # 5
print(3 and 0) # 0
print(0 and 3) # 0
print(0 and 0) # 0

print(5 or 3) # 5
print(3 or 0) # 3
print(0 or 3) # 3
print(0 or 0) # 0
```

### 단축평가 동작
- and
  - 첫 번째 피연산자가 False인 경우, 전체 표현식은 False로 결정
    두 번째 피연산자는 평가되지 않고 그 값이 무시
  - 첫 번째 피연산자가 True인 경우, 전체 표현식의 결과는 두 번째 피연산자에 의해 결정
    두 번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환
- or
  - 첫 번째 피연산자가 True인 경우, 전체 표현식은 True로 결정
    두 번째 피연산자는 평가되지 않고 그 값이 무시
  - 첫 번째 피연산자가 False인 경우, 전체 표현식의 결과는 두 번째 피연산자에 의해 결정
    두번 째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환

### 단축평가 이유
코드 실행을 최적화하고, 불필요한 연산을 피할 수 있도록 함

### 멤버십 연산자
- 특정 값이 시퀀스나 다른 컬렉션에 속하는지 여부를 확인
- in: 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하는지를 확인
- not in: 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하지 않는지를 확인

### 시퀀스형 연산자
- +와 *는 시퀀스 간 연산에서 산술 연산자일때와 다른 역할을 가짐
- +: 결합 연산자
- *: 반복 연산자

### 연산자 우선순위 정리
![!\[Alt text\](image.png)](Python_02-2.png)