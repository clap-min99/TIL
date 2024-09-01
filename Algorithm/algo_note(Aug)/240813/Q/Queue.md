
## Queue



- Qpeek()
  
  가장 앞에 있는 원소를 검색하여 반환하는 연산
  현재 front의 한자리 뒤에 있는 원소, 즉 큐의 첫 번째 원소 반환
  

- 원형큐
    - 선형 큐 이용시 문제점
      
      - 잘못된 포화상태 인식
        
        선형 큐를 이용해 원소 삽입, 삭제를 계속할 경우 배열의 앞부분에 활용할 수 있는 공간이 있음에도 
        rear = n-1인 상태(포화상태)로 인식하여 더 이상의 삽입을 수행하지 않게됨.
        
        해결방법: 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용
        
    - 원형 큐의 구조
        
        - 초기 공백 상태
          : front = rear = 0
          
        - index 순환
    
        - front 변수  
            : 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 **항상 빈자리**로 둠
          
        |    |삽입위치|삭제위치|
        |---|-----|-----|
        |선형큐|rear = rear + 1|front = front + 1|
        |원형큐|rear = (rear+1)mod n| front= (front+1)mod n|
    
        ```python
        Q_SIZE = 4
        cQ = [0] * Q_SIZE
        front = rear = 0
        
        rear = (rear + 1) % Q_SIZE  # enq(1)
        cQ[rear] = 1
        
        rear = (rear + 1) % Q_SIZE  # enq(2)
        cQ[rear] = 2
        
        rear = (rear + 1) % Q_SIZE  # enq(3)
        cQ[rear] = 3
        
        front = (front+1) % Q_SIZE
        print(cQ[front])
        
        front = (front +1) % Q_SIZE
        print(cQ[front])
        
        rear = (rear+1) % Q_SIZE    # enq(10)
        cQ[rear] = 10
        
        rear = (rear+1)% Q_SIZE     # enq(20)
        cQ[rear] = 20
        
        print(cQ)
      ```
    

    
    