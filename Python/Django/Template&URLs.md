# Django 02

## Template System

### Django Template system
데이터 표현을 제어하면서, 표현과 관련된 부분을 담당

### Django Template Language(DTL)
Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

### DTL Syntax
1. Variable
   - render 함수의 세번째 인자로 딕셔너리 데이터를 사용
    - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
    - dot('.')를 사용하여 변수 속성에 접근할 수 있음
2. Filters
   - 표시할 변수를 수정할 때 사용 (변수 + '|' + 필터)
    - chained(연결)이 가능하며 일부 필터는 인자를 받기도 함
    - 약 60개의 built-in template filters를 제공
    - {{ variable|filter }} -> {{ name|truncatewords:30}}
3. Tags
   - 반복 또는 논리를 수행하여 제어 흐름을 만듦
    - 일부 태그는 시작과 종료 태그가 필요
    - 약 24개의 built-in template tags를 제공
    - {% tag %} -> {% if %} {% endif %}
4. Comments
    - DTL에서의 주석
    - {# name #}
    - {% comment %} ... {% endcomment %}

    
## 템플릿 상속
### 기본 템플릿 구조의 한계
- 만약 모든 템플릿에 bootstrap을 적용하려면?  
    -> 모든 템플릿에 bootstrap CDN을 작성해야 할까?
  
### 템플릿 상속(Template inheritance)
페이지의 공통요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축

### 'extends' tag
```html
{% extends 'path' %}
```
자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림  
-> 반드시 자식 템플릿 최상단에 작성되어야 함(2개 이상 사용 불가)

### 'block' tag
```html
{% block name %}{% endblock name %}
```
하위 템플릿에서 재정의할 수 있는 블록을 정의  
(상위 템플릿에 작성하며 하위 템플릿이 작성할 수 있는 공간을 지정하는 것)

## HTML form(요청과 응답)

### 데이터를 보내고 가져오기(Sending and Retrieving form data)
- Html 'form' element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기  
- Html 'form'은 HTTP 요청을 서버에 보내는 가장 편리한 방법

### 'form' element
사용자로부터 할당된 데이터를 서버로 전송  
-> 웹에서 사용자 정보를 입력하는 여러 방식(text, password, checkbox 등)을 제공

### action & method (form의 핵심 속성 2가지)
"데이터를 어디(action)로 어떤 방식(method)으로 요청할지"

- action
    - 입력 데이터가 전송될 URL을 지정(목적지)
    - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
    
- method
    - 데이터를 어떤 방식으로 보낼 것인지 정의
    - 데이터의 HTTP request methods(GET, POST)를 지정
    
### 'input' element
사용자의 데이터를 입력 받을 수 있는 요소(type 속성 값에 따라 다양한 유형의 입력 데이터를 받음)

### 'name' attribute(input의 핵심 속성)
입력한 데이터에 붙이는 이름(key)  
-> 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음

### Query String Parameters
- 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법
- 문자열은 '&'로 연결된 key=value 쌍으로 구성되며, 기본 URL과는 '?'로 구분됨
- 예시 -> http://host:port/path?key=value&key=value

### HTTP request 객체
form으로 전송한 데이터 뿐만 아니라 모든 요청 관련 데이터가 담겨 있음(view 함수의 첫번째 인자)

### form 데이터를 가져오는 방법
`request.GET.get('message')`
- request.GET -> <QueryDict: {'message':['안녕!']}>
- .get('message') -> 딕셔너리 get 메서드를 사용해서 키의 값을 조회

### catch 로직 마무리
```python
def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)
```
### 추가 템플릿 경로 지정
- 템플릿 기본 경로 외 커스텀 경로 추가하기
- setting.py에서 TEMPLATES의 'DIRS'설정
- 'DIRS': [BASE_DIR / 'templates,] -> 기본 프로젝트 폴더 안의 templates 폴더로 접근

### DTL 주의사항
- python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 명칭을 그렇게 설계했을 뿐이지 Python 코드로 실행되는 것이 아니며 Python과는 관련 없음
- 프로그래밍적 로직이 아니라 표현을 위한 것임을 명심
- 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리

## Django URLs

### 요청과 응답에서 Django URLs의 역할
![img.png](Template&URLs-1.png)

### URL dispatcher(운항 관리자, 분배기)
URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)

### 현재 URL 관리의 문제점
템플릿의 많은 부분이 중복되고, URL의 일부만 변경되는 상황이라면 계속해서 비슷한 URL과 템플릿을 작성해 나가야 할까?  
![img.png](Template&URLs-2.png)

### Variable Routing
URL 일부에 변수를 포함시키는 것(변수는 view 함수의 인자로 전달할 수 있음)

### Variable routing 작성법
`<path_converter:variable_name>`

### Path converters
URL 변수의 타입을 지정(str, int 등 5가지 타입 지원)

### Trailing Slashes
- Django는 URL 끝에 '/'가 없다면 자동으로 붙임
- "기술적인 측면에서, foo.com/bar와 foo.com/bar/는 서로 다른 URL"
    - 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 이 두 주소를 서로 다른 페이지로 보기 때문
- 그래서 Django는 검색 엔진이 혼동하지 않게 하기 위해 무조건 붙이는 것을 선택한 것
- 그러나 모든 프레임워크가 이렇게 동작하는 것은 아니니 주의