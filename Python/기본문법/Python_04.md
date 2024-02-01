# Python_04
## 모듈(Module)
한 파일로 묶인 변수와 함수의 모음. 특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)

### 모듈 예시
- 파이썬의 math 모듈
- 파이썬이 미리 작성해 둔 수학 관련 변수와 함수가 작성된 모듈

### 모듈 가져오기
- 모듈 내 변수와 함수에 접근하려면 `import`문이 필요
- 내장 함수 help를 사용해 모듈에 무엇이 들어있는지 확인 가능

### 모듈 사용하기
- `.(dot)`은 "점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라" 라는 의미의 연산자

```py
# 모듈명.변수명
print(math.pi)

# 모듈명.함수명
print(math.wqrt(4))
```

### 모듈을 import하는 다른 방법
- `from`절을 활용해 특정 모듈을 미리 참조하고 어떤 요소를 import 할지 명시

### 모듈 주의사항
- `만약 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생`
- 마지막에 import된 이름으로 대체됨

```py
from math import pi, sqrt
from my_math import sqrt
```

```py
# 그래서 모듈 내 모든 요소를 한번에 import 하는 * 표기는 권장하지 않음

from math import *
```

### 사용자 정의 모듈
그냥 내가 다른 py파일에 함수를 정의하고 import해서 그 함수를 사용 가능함

## 파이썬 표준 라이브러리 (PSL)
파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음
모듈 < 패키지 < 라이브러리

### 패키지
관련된 모듈들을 하나의 디렉토리에 모아 놓은 것
- PSL 내부 패키지: 설치 없이 바로 import하여 사용
- 외부 패키지: `pip`를 사용하여 설치 후 import 필요

### pip(파이썬 패키지 관리자)
외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템

### 패키지 설치
- 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치할 수 있음(==이나 >= 사용)

### requests 외부 패키지 설치 및 사용 예시
```shell
$ pip install requests
```
```py
import requests

url = 'https://random-data-api.com/api/v2/user'
response = requests.get(url).json()

print(response)
```

### 패키지 사용 목적
모듈들의 이름 공간을 구분하여 충돌을 방지. 모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할

## 제어문(Control Statement)
코드의 실행 흐름을 제어하는 데 사용되는 구문. `조건`에 따라 코드블록을 실행하거나 `반복`적으로 코드를 실행

## 조건문(Conditional Statement)
주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

- if / elif / else -> 파이썬 조건문에 사용되는 키워드

### `if` statement
- if statement의 기본 구조
```py
if 표현식:
    코드블록
elif 표현식:
    코드블록
else:
    코드 블록
```

## 반복문
주어진 코드 블록을 여러 번 반복해서 실행하는 구문
- 특정 작업을 반복적으로 수행
- 주어진 조건이 참인 동안 반복해서 실행

### for / while
파이썬 반복문에 사용되는 키워드

### `for` statement
임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복
- for statement의 기본 구조
```py
for 변수 in 반복 가능한 객체:
    코드 블록
```

### 반복 가능한 객체(iterable)
반복문에서 순회할 수 있는 객체(시퀀스 객체 뿐만 아니라 dict, set 등도 포함)

### for문 원리
- 리스트 내 첫 항목이 반복 변수에 할당되고 코드블록이 실행
- 다음으로 반복 변수에 리스트의 2번째 할당되고 코드블록이 다시 실행
- ...마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 실행

### 문자열 순회
- 문자열이 시퀀스이기 때문에 문자열도 char로 순회가 가능함 

### range 순회
- range()를 통해 반복

### 딕셔너리 순회
- for key in dict_name: 으로 순회가 가능함. key만 나오기 때문에 value는 dict_name[key]로 사용 가능

### 인덱스로 리스트 순회
- 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경 가능

### 중첩된 반복문
- n중 반복문, 그냥 아는 거
- 안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 중첩 반복을 사용해 각 안쪽 반복을 순회

### `while` statement
주어진 조건식이 참(True)인 동안 코드를 반복해서 실행 == 조건식이 거짓(False)가 될 때 까지 반복

- while statement의 기본 구조
```py
while 조건식:
    코드 블록
```
`while 문은 반드시 종료 조건이 필요`

### for / while
- for
  - iterable의 요소를 하나씩 순회하며 반복
  - 반복 횟수가 명확하게 정해져 있는 경우에 유용
  - 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때
- while
  - 주어진 조건식이 참인 동안 반복
  - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
  - 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

### continue
- 현재 반복문의 남은 코드를 건너뛰고 다음 반복으로 넘어감

### break와 continue 주의사항
- break와 continue를 남용하는 것은 코드의 가독성을 저하시킬 수 있음
- 특정한 종료 조건을 만들어 break를 대신하거나, if문을 사용해 continue처럼 코드를 건너 뛸 수도 있음
- 약간의 시간이 들더라도 가능한 코드의 가독성을 유지하고 코드의 의도를 명확하게 작성하도록 노력하는 것이 중요

## List Comprehension
간결하고 효율적인 리스트 생성 방법

### List Comprehension 구조
```py
[expression for 변수 in iterable]

list(expression for 변수 in iterable)
```

### List Comprehension 활용
```py
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]

print(squared_numbers) # [1, 4, 9, 16, 25]
```

### [참고] List Comprehension과 if 조건문
```py
[expression for 변수 in iterable if 조건식]

list(expression for 변수 in iterable if 조건식)
```
```py
result = [i for i in range(10) if i % 2 == 1]
```

### Comprehension을 남용하지 말자.

## 참고
### pass
아무런 동작도 수행하지 않고 넘어가는 역할 -> 문법적으로 문장이 필요하지만 프로그램 실행에는 영향을 주지 않아야 할 때 사용

### pass 예시
1. 코드 작성 중 미완성 부분
  - 구현해야할 부분이 나중에 추가될 수 있고, 코드를 컴파일하는 동안 오류가 발생하지 않음
2. 조건문에서 아무런 동작을 수행하지 않아야 할 때
3. 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행하는 방법

### enumerate(iterable, start=0)
iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

### enumerate 예시
```py
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
  print(f'인덱스 {index}: {fruit}')
```