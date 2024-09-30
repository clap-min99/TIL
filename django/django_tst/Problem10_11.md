### 문제 10. (서술형) Django의 Form과 ModelForm의 차이점을 설명하고, 각각 어떤 상황에서 사용하는 것이 적절한지 서술하시오.

Form은 직접 field를 정의하고 구성해야한다.
ModelForm은 model class를 기반으로 한다. 




### 문제 11. (서술형) Django의 MTV 패턴을 기반하여 HTTP 요청 응답이 반환되기까지의 흐름을 서술하시오.

Django의 MTV 패턴이란, 
Models, Templates, Views를 의미한다.

클라이언트로 부터 request가 들어오면 urls 경로에 따라 request를 보내고,
각 url은 정의된 view함수에 request를 보낸다.
request의 종류나 method에 따라 view함수는 반환하거나 렌더링할 templates를 보여준다.
이때 view함수 내에서 데이터를 생성, 수정, 삭제하기 위해서는 데이터를 조회해야 하는데 model 클래스의 필드를 불러옴으로써 조회할 수 있다.
