# Queue
- 먼저 넣은 데이터를 가장 먼저 꺼는 데이터 구조입니다.
- FIFO(First-In, First-Out : 선입선출) 또는 LILO(Last-In, Last-Out) 방식을 사용합니다.
- Enqueue : 큐에 데이터를 넣는 기능을 의미합니다. python list의 append() 메서드와 유사합니다.
- Dequeue : 큐에서 데이터를 꺼내는 기능을 의미합니다. python list의 pop(0) 메소드와 유사합니다.
- Queue Library (import queue)
  1. Queue() : 일반적인 Queue
  2. LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 Queue(Stack과 동일)
  3. PriorityQueue() : 데이터마다 우선순위를 정하여 정렬된 큐로, 우선 순위가 높은 순으로 출력되는 구조
