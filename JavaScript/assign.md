## JavaScript에서 동기, 비동기 동작의 차이점을 md파일에 작성하여 제출하시오.

### 동기
동기는 프로그램의 실행 흐름이 순차적으로 진행되는 것으로 하나의 작업이 완료된 후에 다음 작업이 실행되는 방식이다.

### 비동기
비동기는 프로그램의 실행 흐름이 순차적이지 않으며, 작업이 완료되기를 기다리지 않고 다음 작업이 실행되는 방식으로 작업의 완료 여부를 신경 쓰지 않고 동시에 다른 작업들을 수행할 수 있다.

### 자바스크립트에서의 동기와 비동기
자바스크립트는 Single Thread언어로 기본적으로 동기적 처리방식이다. 따라서 자바스크립트는 한번에 여러 일을 수행할 수 없는데 JavaScript Runtime 즉 자바 스크립트가 동작할 수 있는 환경인 브라우저 환경에서 자바 스크립트가 비동기 처리가 가능하게 도와준다.

따라서 정리하자면 자바스크립트는 한 번에 하나의 작업을 수행하는 동기적 처리를 진행하지만 브라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐 Event Loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 된다.