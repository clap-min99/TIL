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


### Hooks

- useState

    `const [value, setvalue] = useState(0)`

    배열을 return 

    첫 번째 요소는 state, 

    두번째 요소(setstate)는 해당 state를 set해주는 setter 함수

    useState 함수의 인자로 넘겨주는 값 -> state의 초기값 설정
    
    상태가 변경되면 **컴포넌트 다시 렌더링**

    ```js
    import React, { useState } from 'react';

    function Counter() {
    const [count, setCount] = useState(0); // 상태 선언

    return (
        <div>
        <p>Count: {count}</p>
        <button onClick={() => setCount(count + 1)}>Increase</button>
        </div>
    );
    }
    ```

- useEffect

    - 목적

        컴포넌트에서 *side effect*를 관리하는데 사용

        부수효과(side effect)란, 컴포넌트 렌더링 외 발생하는 비동기 작업이나 외부 작업을 의미(데이터 요청,  DOM 조작 등)

    - 사용 예시

        ```js
        import React, { useState } from 'react';

        function Counter() {
        const [count, setCount] = useState(0); // 상태 선언

        return (
            <div>
            <p>Count: {count} </p>
            <button onClick={() => setCount(count + 1)}>Increase</button>
            </div>
        );
        }
        ```
    
    - 특징

        의존성 배열 

        `useEffect(callback, [dependencies])`

        특정 값이 변경될 때만 부수 효과를 실행하려면 의존성 배열 사용

        배열이 비어 있으면 [], 부수 효과는 **컴포넌트가 처음 마운트 될 때만** 실행.


        - 클린업 함수
            
            리소스 해제를 위해 정리(cleanup) 함수 반환 가능(useEffect에서 return 되는 함수)

            ```js
            useEffect(() => {
            const timer = setInterval(() => console.log('Timer...'), 1000);

            return () => clearInterval(timer); // 컴포넌트 언마운트 시 실행
            }, []);
            ```

- useCallback

    - 목적

        함수형 컴포넌트에서 함수의 재생성을 방지하기 위해 사용

        React는 컴포넌트가 렌더링될 때마다 내부에 정의된 함수도 새로 생성되는데, useCallback을 사용하면 이를 메모이제이션(Memoization)하여 동일한 함수 인스턴스를 재사용할 수 있다.

    - 사용 예시

        ```js
        import React, { useState, useCallback } from 'react';

        function Counter() {
        const [count, setCount] = useState(0);

        const increment = useCallback(() => {
            setCount((prevCount) => prevCount + 1);
        }, []); // 의존성 배열이 비어 있으므로 컴포넌트가 처음 렌더링될 때만 함수 생성

        return (
            <div>
            <p>Count: {count}</p>
            <button onClick={increment}>Increase</button>
            </div>
        );
        }
        ```

    - useCallback 동작원리

        useCallback은 함수와 함께 의존성 배열을 전달받음
        
        의존성 배열이 변경되지 않으면 이전에 메모이제이션된 함수 인스턴스를 재사용
        
        의존성 배열 내 값이 변경되면 새로운 함수가 생성

### React router


### API 연동(axios)

- Axios API

    [axios api reference](https://axios-http.com/docs/api_intro)

    