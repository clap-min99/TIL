## React

### React란

1. React
    사용자 인터페이스를 만들기 위한 javascript 라이브러리(**SPA** 라이브러리)

- React 특징
    1. component 기반 설계
        
        의미 단위 구성 

        재사용성 및 유지 보수성 증가

    2. 가상 돔 

        실제 DOM의 복사본으로 SPA에서의 동적인 변화를 효율적으로 관리하기 위해 사용

        DOM을 직접 변경하여 생기는 비효율 해결


2. JSX

    JSX = HTML + Javascript (Javascript XML)

    - Javascript를 확장한 문법

    - 모양은 HTML에 가까움

    - 내부적으로 JS 사용할 수 있음

    - react는 JSX를 이용해 화면을 그림 (컴포넌트)


- JSX 특징

    - JSX에서 사용되는 태그의 속성 이름이 HTML과 다름

        ex. class -> className / for -> htmlFor / onclick -> onClick
    
    - 태그를 명시적으로 닫아줘야 함
    
    - 하나의 태그로 감싸져 있어야 함

        ```html
        <div>
            <button className ="btn">Hello, world!</button>
            <input type="text" />
        </div> 
        ```
