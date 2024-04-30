# Basic Syntax 1

## Template Syntax
### Template Syntax
DOM을 기본 구성 요소 인스턴스의 데이터에 선언적으로 바인딩할(Vue Instance와 DOM을 연결) 수 있는 HTML 기반 템플릿 구문(확장된 문법 제공)을 사용

### Template Syntax 종류
1. Text Interpolation
2. Raw HTML
3. Attribute Bindings
4. JavaScript Expressions

### 1. Text Interpolation
```html
<p>Message: {{ msg }} </p>
```
- 데이터 바인딩의 가장 기본적인 형태
- 이중 중괄호 구문 (콧수염 구문)을 사용
- 콧수염 구문은 해당 구성 요소 인스턴스의 msg 속성 값으로 대체
- msg 속성이 변경될 때마다 업데이트 됨

### 2. Raw HTML
```html
<div v-html="rawHtml"></div>

<script>
  const rawHtml = ref('<span style="color:red">This should be red.</span>')
</script>
```
- 콧수염 구문은 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML을 출력하려면 v-html을 사용해야 함

### 3. Attribute Bindings
```html
<div v-bind:id="dynamicId"></div>

<script>
  const dynamicId = ref('my-id')
</script>
```
- 콧수염 구문은 HTML 속성 내에서 사용할 수 없기 때문에 v-bind를 사용
- HTML의 id 속성 값을 vue의 dynamicId 속성과 동기화 되도록 함
- 바인딩 값이 null이나 undefind인 경우 렌더링요소에서 제거됨

### 4. JavaScript Expressions
- Vue는 모든 데이터 바인딩 내에서 JavaScript 표현식의 모든 기능을 지원
- Vue 템플릿에서 JavaScript 표현식을 사용할 수 있는 위치
  1. 콧수염 구문 내부
  2. 모든 directive의 속성 값("v-"로 시작하는 특수 속성)


### Expressions 주의사항
- 각 바인딩에는 하나의 단일 표현식만 포함될 수 있음
  - 표현식은 값으로 평가할 수 있는 코드 조각(return 뒤에 사용할 수 있는 코드여야 함)

- 작동하지 않는 경우  
```html
<!-- 표현식이 아닌 선언식 -->
{{ const number = 1 }}

<!-- 제어문은 삼항 표현식을 사용해야 함 -->
{{ if (ok) {return message} }}
```

## Directive
### Directive
'v-' 접두사가 있는 특수 속성

### Directive 특징
- Directive의 속성 값은 단일 JavaScript 표현식이어야 함(v-for, v-on 제외)
- 표현식 값이 변경될 때 DOM에 반응적으로 업데이트를 적용
- 예시  
  ```html
    <p v-if="seen">Hi There</p>
  ```

### Directive 전체 구문
`v-on:submit.prevent="onSubmit"`
- v-on -> Name, Starts with v- May be omitted when using shorthands
- submit -> Argument, Follows the colon or shorthand symbol
- prevent -> Modifiers, Denoted by the leading dot
- onSubmit -> Value, Interpreted as JavaScript expressions

### Directive - "Arguments"
- 일부 directive는 directive 뒤에 콜론(":")으로 표시되는 인자를 사용할 수 있음
- 아래 예시의 href는 HTML <a> 요소의 href 속성 값을 myUrl 값에 바인딩 하도록 하는 v-bind의 인자  
  ```html
  <a v-bind:href="myUrl">Link</a>
  ```

- 아래 예시의 click은 이벤트 수신할 이벤트 이름을 작성하는 v-on의 인자  
  ```html
  <button v-on:click="doSomething">Button</button>
  ```

### Directive - "Modifiers"
- ".(dot)"로 표시되는 특수 접미사로, directive가 특별한 방식으로 바인딩되어야 함을 나타냄
- 아래 예시의 .prevent는 발생한 이벤트에서 event.preventDefault()를 호출하도록 v-on에 지시하는 modifier

### Built-in Directives
- v-text
- v-show
- v-if
- v-for
- ...

## Dynamically data binding
## v-bind

### v-bind
하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩

### v-bind 사용처
1. Attribute Bindings
2. Class and Style Bindings

## Attribute Bindings
### Attribute Bindings
- HTML의 속성 값을 Vue의 상태 속성 값과 동기화 되도록 함  
  ```html
  <!-- v-bind.html -->
  <img v-bind:src="imageSrc">
  <a v-bind:href="myUrl">Move to url</a>
  ```

- v-bind shorthand (약어)
  - ':' (colon)  
  ```html
  <img :src="imageSrc">
  <a :href="myUrl">Move to url</a>
  ```

- Dynamic attribute name (동적 인자 이름)
  - 대괄호([])로 감싸서 directive argument에 JavaScript 표현식을 사용할 수도 있음
  - JavaScript 표현식에 따라 동적으로 평가된 값이 최종 argument 값으로 사용됨  
  ```html
  <button :[key]="myValue"></button>
  ```
  - 대괄호 안에 작성하는 이름은 반드시 소문자로만 구성 가능(브라우저가 속성 이름을 소문자로 강제 변환하기 때문)

