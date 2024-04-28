# Ajax with Django

## Ajax와 서버

### Ajax(Asynchronous JavaScript and XML)
비동기적인 웹 애플리케이션 개발에 사용하는 기술

### Ajax를 활용한 클라이언트 서버 간 동작
- XML 객체 생성 및 요청 -> Ajax 요청 처리 -> 응답 데이터 생성 -> JSON 데이터 응답 -> Promise 객체 데이터를 활용해 DOM 조작(웹 페이지의 일부분 만을 다시 로딩)

## 비동기 팔로우 구현

### Ajax 적용
1. 프로필 페이지에 axios CDN 작성
2. form 요소 선택을 위해 id 속성 지정 및 선택
    - action과 method 속성은 삭제
        - 요청은 axios로 대체되기 때문

3. form 요소에 이벤트 핸들러 할당 및 submit 이벤트의 기본 동작 취소
4. axios 요청 작성
    1. url에 작성할 user pk는 어떻게 작성해야 할까?
    2. csrftoken은 어떻게 보내야 할까?

5. url에 작성할 user pk 가져오기 (HTML -> JavaScript)
    ```html
    <form id="follow-form" data-user-id = "{{ person.pk }}">
        ...
    </form>

    ...
    <script>
        ...
        formTag.addEventListener('submit', function (event){
            event.preventDefault()

            const userId = event.currentTarget.dataset.userId
            const userId = this.dataset.userId
            const userId = formTag.dataset.userId
        })
        ...
    </script>
    ```

### 'data-*' 속성
사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM 사이에서 교환 할 수 있는 방법

### data-* 사용 예시
```html
<div data-my-id="my-data"></div>

<script>
    const myId = event.target.dataset.myId
</>
```
- 모든 사용자 지정 데이터는 JavaScript에서 dataset 속성을 통해 사용
- 주의 사항
    1. 대소문자 여부에 상관없이 'xml' 문자로 시작 불가
    2. 세미콜론 포함 불가
    3. 대문자 포함 불가


6. 요청 url 작성 마무리

```html
<script>
    formTag.addEventListener('submit', function (event){
        event.preventDefault()

        const userId = event.currentTarget.dataset.userId

        axios({
            method: 'post',
            url: `/accounts/${userId}/follow/`,
        })
    })
</script>
```

7. 문서상 input hidden 타입으로 존재하는 csrf token 데이터를 이제는 axios로 전송해야 함
    - csrf 값을 가진 input 요소를 직접 선택 후 axios에 작성하기
    ```html
    <script>
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

        formTag.addEventListener('submit', function(event) {
            event.preventDefault()

            const userId = event.currentTarget.dataset.userId

            axios({
                method:'post',
                url: `/accounts/${userId}/follow/`
                headers: {'X-CSRFToken': csrftoken,},
            })
        })
    </script>
    ```

8. 팔로우 버튼을 토글하기 위해서는 현재 팔로우 상태인지 언팔로우 상태인지에 대한 상태 확인이 필요
> Django의 view 함수에서 팔로우 여부를 파악 할 수 있는 변수를 추가로 생성해 JSON 타입으로 응답하기
- 팔로우 상태 여부를 JavaScript에게 전달할 데이터 작성
- 응답은 더 이상 HTML 문서가 아닌 JSON 데이터로 응답

```py
from django.http import JsonResponse

...
    if person.follwers.filter(pk = request.user.pk).exists():
        person.followers.remove(request.user)
        is_followed = False
    else:
        person.followers.add(request.user)
        is_followed = True
    context = {
        'is_followed': is_followed,
    }
    return JsonResponse(context)
```

9. 응답 데이터 is_followed에 따라 팔로우 버튼을 토글하기
```html
<script>
    axios({
        method:'post',
        url: `/accounts/${userId}/follow/`
        headers: {'X-CSRFToken': csrftoken,},
    })
    .then((response) => {
        const isFollowed = response.data.is_followed
        const followBtn = document.querySelector('input[type=submit]')
        if (isFollowed === true){
            followBtn.value = 'Unfollow'
        } else{
            followBtn.value = 'Follow'
        }
    })

</script>
```