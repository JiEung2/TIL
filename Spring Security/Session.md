```java
http
        .sessionManagement((auth) -> auth
                .maximumSessions(1)
                .maxSessionsPreventsLogin(true));
http
        .sessionManagement((auth) -> auth
                .sessionFixation().changeSessionId());
```

1. 세션 관리에 대한 설정
```java
http
        .sessionManagement((auth) -> auth
                .maximumSessions(1)
                .maxSessionsPreventsLogin(true));
```
- `maximumSession(1)`: 사용자당 최대 세션 수를 1개로 제한한다. 즉, 한 계정으로 동시에 하나의 로그인만 가능하다.
- `maxSessionPreventsLogin(true)`: 이미 세션이 존재할 경우 새로운 로그인을 막는다. 예를 들어, 이미 로그인한 사용자가 다른 브라우저나 기기에서 로그인을 시도하면 거부된다.

2. 세션 고정 공격(Session Fixation Attack)을 방지하기 위한 설정
```
http
        .sessionManagement((auth) -> auth
                .sessionFixation().changeSessionId());
```
- `sessionFixation().changeSessionId()`: 인증 시 새로운 세션 ID를 생성한다. 이는 사용자가 로그인할 때마다 새로운 세션 ID를 부여하여 세션 고정 공격을 방지한다.

## 세션 고정 공격(Session Fixation Attack)
1. 세션 고정 공격이란?
- 공격자가 미리 알고있는 세션 ID를 피해자의 브라우저에 심은 후, 피해자가 그 세션 ID로 로그인하도록 유도하는 공격
- 이를 통해 공격자는 피해자의 인증된 세션을 공유할 수 있게 된다.

### 세션 고정 공격 단계
1. 세션 ID 생성 및 고정
- 공격자는 시스템에서 유효한 세션 ID를 생성한다. 이 세션 ID는 공격자가 미리 준비해 둔 것.
2. 피해자에게 세션 ID 전달
- 공격자는 여러 방법을 통해 피해자에게 이 세션 ID를 전달한다. 예를 들어, 피싱 이메일, 링크를 클릭하게 유도하는 방식 등이 존재.
3. 피해자가 세션 ID로 로그인
- 피해자가 공격자가 제공한 세션 ID를 사용하여 시스템에 로그인한다. 이 때, 시스템은 피해자가 로그인했다고 인식하고 해당 세션 ID를 인증된 상태로 전환
4. 세션 탈취
- 공격자는 이미 알고있는 세션 ID를 통해 시스템에 접근하여, 피해자의 권한으로 다양한 할동을 수행할 수 있다.

### 세션 고정 공격 방지 방법
1. 세션 ID 재생성: 사용자가 로그인할 때마다 새로운 세션 ID를 생성하도록 설정. 이를 통해 이전 세션 ID가 유효하지 않게 되어 공격자가 이를 악용할 수 없다.
2. HTTPS 사용: HTTPS를 통해 세션 ID를 암호화하여 전송한다. 이를 통해 세션 ID가 네트워크를 통해 전달되는 동안 가로챌 수 없게 된다.
3. 세션 타임아웃 설정: 세션의 유효시간을 짧게 설정하여 오래된 세션 ID가 더 이상 사용되지 않도록 한다.
4. XSS 방지: 크로스 사이트 스크립팅(XSS) 공격을 방지하여, 공격자가 자바스크립트를 통해 세션 ID를 훔칠 수 없도록 한다.

위의 코드에서는 sessionFixation().changeSessionId()를 통해 로그인 시 새로운 세션 ID를 생성하는 설정으로 세션 고정 공격을 방지.