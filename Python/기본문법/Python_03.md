## 함수(Functions)
특정 작업을 수행하기 위한 재사용 가능한 코드 묶음

### 함수를 사용하는 이유
- 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
- `재사용성`이 높아지고, 코드의 `가독성과 유지보수성` 향상

### 내장 함수(Built-in function)
파이썬이 기본적으로 제공하는 함수(별도의 import없이 바로 사용 가능)
- ex) abs, print 등등

### 함수 호출(function call)
함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것

## 함수의 구조
함수는 기본적으로 Input과 Output이 존재
![!\[Alt text\](image.png)](Python_03-1.png)

```python
def make_sum(pram1, pram2):
  """이것은 두 수를 받아
  두 수의 합을 반환하는 함수입니다.

  >>> make_sum(1, 2)
  3
  """
  return pram1 + pram2
```
- 위에서 pram1, pram2은 `parameter(매개변수)`라고 불림
- return pram1 + pram2 부분은 `return value`
- 매개변수와 return 사이의 부분을 `function body`라고 불림
- 함수 내에서 지금 주석처리된 부분은 `Docstring`이라고 일반 주석으로 표현하는 것이 아닌 함수의 설명과 사용 방법에 대한 주석임.

### 함수의 정의와 호출
- 함수 정의(정의)
  - 함수 정의는 def 키워드로 시작
  - def 키워드 이후 함수 이름 작성
  - 괄호 안에 매개변수를 정의할 수 있음
  - 매개변수(parameter)는 함수에 전달되는 값을 나타냄

- 함수 body
  - 콜론`:` 다음에 들여쓰기 된 코드 블록
  - 함수가 실행될 때 수행되는 코드를 정의
  - Docstring은 함수 body 앞에 선택적으로 작성 가능한 함수 설명서

- 함수 반환 값
  - 함수는 필요한 경우 결과를 반환할 수 있음
  - return 키워드 이후에 반환할 값을 명시
  - return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환

- 함수 호출
  - 함수를 호출하기 위해서는 함수의 이름과 필요한 `인자(argument)`를 전달해야 함
  - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 `매개변수`에 대입됨

## 매개변수와 인자
### 매개변수(parameter)
함수를 정의할 때, 함수가 받을 값을 나타내는 변수

### 인자(argument)
함수를 호출할 때, 실제로 전달되는 값

### 인자의 종류(중요)
### Positional Arguments(위치인자)
- 함수 호출 시 인자의 위치에 따라 전달되는 인자
-> `위치인자는 함수 호출 시 반드시 값을 전달해야 함`

```python
def greet(name, age):
  print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Alice', 25)
```

### Default Argument Values(기본 인자 값)
- 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨

```python
def greet(name, age = 30):
  print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Alice') # 안녕하세요, Alice님! 30살이시군요.
greet('Charlie', 40) # 안녕하세요, Charlie님! 40살이시군요.
```

### Keyword Arguments(키워드 인자)
- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
`단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함`

```python
def greet(name, age):
  print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name = 'Alice', age = 35) # 안녕하세요, Alice님! 35살이시군요.
greet(age=35, 'Charlie') # positional argument follows keyword argument
```

### Arbitrary Argument List(임의의 인자 목록)
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 `*`를 붙여 사용하며, 여러 개의 인자를 `tuple`로 처리

```python
def calculate_sum(*args):
  print(Args)
  total = sum(args)
  print(f'합계: {total}')

calculate_sum(1, 2, 3)
# (1, 2, 3)
# 합계: 6
```

### Arbitrary Keyword Argument Lists(임의의 키워드 인자 목록)
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 함수 정의시 매개변수 앞에 `**`를 붙여 사용하며, 여러 개의 인자를 dictinary로 묶어 처리

```python
def print_info(**kwargs):
  print(kwargs)

print_info(name='Eve', age=30) # {'name': 'Eve', 'age':30}
```

### 함수 인자 권장 작성 순서
- 위치 -> 기본 -> 가변 -> 가변 키워드
- 호출 시 인자를 전달하는 과정에서 혼찬을 줄일 수 있도록 함
`단, 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정될 수 있음`

```python
def func(pos1, pos2, default_arg='default', *args, **kwargs):
  ...
```

## 함수와 Scope
### Python의 범위(Scope)
- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope
  - global scope: 코드 어디에서든 참조할 수 있는 공간
  - local scope: `함수`가 만든 scope(함수 내부에서만 참조 가능)
- variable
  - global variable: global scope에 정의된 변수
  - local variable: local scope에 정의된 변수

### Scope 예시
- num은 local scope에 존재하기 때문에 global에서 사용할 수 없음
- 이는 변수의 수명주기와 연관이 있음

### 변수 수명주기(lifecycle)
- 변수의 수명주기는 변수가 선언되는 위치와 스코프에 따라 결정됨
1. built-in scope
  - 파이썬이 실행된 이후부터 영원히 유지
2. global scope
  - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope
  - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### 이름 검색 규칙(Name Resolution)
- 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름
  1. Local scope: 지역 범위(현재 작업 중인 범위)
  2. Enclosed scope: 지역 범위 한 단계 위 범위
  3. Global scope: 최상단에 위치한 범위
  4. Built-in sopce: 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)
`함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음`

### LEGB Rule 예시
- sum이라는 이름을 global scope에서 사용하게 되면서 기존에 built-in scope에 있던 내장함수 sum을 사용하지 못하게 됨
- sum을 참조 시 LEGB Rule에 따라 global에서 먼저 찾기 때문

```python
print(sum)
print(sum)(range(3)) # 3

sum = 5

print(sum) # 5
print(sum(range(3))) # TypeError: 'int' object is not callable

```

### 'global' 키워드
- 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

### 'global' 키워드 주의사항
- global 키워드 선언 전에 접근 시 에러
- 매개변수에 global 사용 불가

`global 키워드는 가급적 사용하지 않는 것을 권장. 함수로 값을 바꾸고자 한다면 항상 인자로 넘기고 함수의 반환 값을 사용하는 것을 권장`

## 재귀 함수
함수 내부에서 자기 자신을 호출하는 함수

### 재귀 함수 특징
- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

### 재귀함수는
1. 종료 조건을 명확히
2. 반복되는 호출이 종료 조건을 향하도록

## 유용한 함수
### 유용한 내장 함수
- map과 zip 함수

### map(function, iterable)
순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

```python
numbers = [1, 2, 3]
result_cnt = map(str, numbers)

print(result_cnt)  # <map object at 0x00000239C915D760>
print(list(result_cnt))  # ['1', '2', '3']
```

### zip(*iterables)
임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
```python
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair) # <zip object at 0x000001C76DE58700>
print(list(pair)) # [('jane', 'peter'), ('ashle', 'jay')]
```

### lambda 함수
이름 없이 정의되고 사용되는 익명 함수

### lambda 함수 구조
`lamda 매개변수: 표현식`
- lambda 키워드
  - 람다 함수를 선언하기 위해 사용되는 키워드
- 매개변수
  - 함수에 전달되는 매개변수들
  - 여러 개의 매개변수가 있을 경우 쉼표로 구분
- 표현식
  - 함수의 실행되는 코드 블록으로, 결과값을 반환하는 표현식으로 작성

### lambda 함수 예시
- 간단한 연산이나 함수를 한 줄로 표현할 때 사용
- 함수를 매개변수로 전달하는 경우에도 유용하게 활용

```python
def func(x):
  return x ** 2
number = [1, 2, 3, 4, 5]
print(list(map(func, number)))
```

```python
number = [1, 2, 3, 4, 5]
print(list(map(lambda x : x**2, number)))
```

## Packing & Unpacking
### Packing(패킹)
여러 개의 값을 하나의 변수에 묶어서 담는 것

### 패킹 예시
- 변수에 담긴 값들은 튜플(tuple) 형태로 묶임

```python
packed_values = 1, 2, 3, 4, 5
print(packed_values) # (1, 2, 3, 4, 5)
```

### `*`을 활용한 패킹
- *b는 남은 요소들을 리스트로 패킹하여 할당
```python
numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers

print(a) # 1
print(b) # [2, 3, 4]
print(c) # 5
```

- print 함수에서 임의의 가변 인자를 작성할 수 있었던 이유
  -> 인자 개수에 상관 없이 튜플 하나로 패킹 되어서 내부에서 처리
  ![!\[Alt text\](image.png)](Python_03-2.png)

### Unpacking(언패킹)
패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것

### 언패킹 예시
- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
```python
packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values

print(a, b, c, d, e) # 1 2 3 4 5
```

### `*`을 활용한 언패킹
- `*`는 리스트의 요소를 언패킹
```python
names = ['alice', 'jane', 'peter']
print(*names) # alice jane peter
```

### `**`을 활용한 언패킹
- `**`는 딕셔너리 키-값 쌍을 함수의 키워드 인자로 언패킹
```python
def my_function(x, y, z):
  print(x, y, z)

my_dict = {'x':1, 'y':2, 'z':3} # 대신 매개변수의 이름과 인자의 이름이 무조건 같아야함.
my_function(**my_dict) # 1 2 3
```

### `*`, `##` 패킹 / 언패킹 연산자 정리
- `*`
  - 패킹 연산자로 사용될 때, 여러 개의 인자를 하나의 튜플로 묶는 역할
  - 언패킹 연산자로 사용될 때, 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달
- '**'
  - 언패킹 연산자로 사용될 때, 딕셔너리의 키-값 쌍을 키워드 인자로 언패킹하여 함수의 인자로 전달하는 역할