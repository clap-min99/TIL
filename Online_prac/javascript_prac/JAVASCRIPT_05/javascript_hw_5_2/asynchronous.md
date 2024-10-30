## 동기, 비동기
프로그램의 실행 흐름에 따라 동기, 비동기로 나눈다.

### Synchronous 동기
프로그램의 실행 흐름이 순차적으로 진행된다. 즉 하나의 작업이 완료된 후에 다음 작업이 실행되는 식이다. 

```javascript
console.log('첫번째')
console.log('두번째')
console.log('세번째')
```
예를 들면 위 코드의 출력 순서는 

첫번째

두번째 

세번째

가 될 것이다. 

### Asynchronous 비동기
비동기는 특정 작업의 실행이 완료될 때까지 기다리지 않고 다음 작업을 즉시 실행하는 방식이다. 
(작업 완료 여부를 신경쓰지 않고 동시에 다른 작업을 수행할 수 있다.)

```javascript
console.log('Hi')

setTimeout(function myFunc() {
  console.log('work')
}, 3000)

console.log('Bye')
```
위 코드의 출력 순서는 Hi -> work -> Bye 가 아닌
Hi -> Bye -> work가 된다.
하지만 JavaScript는 한 번에 하나의 작업을 수행하는 **Single Thread** 언어로 동기적 처리를 진행한다.
자바스크립트를 수행하는 환경인 browser나 Node.js 도움을 받기 때문이다.


