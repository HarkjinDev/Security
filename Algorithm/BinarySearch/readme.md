# Binary Search (이진탐색)
- Big-O : O(log N)
- 오름차순으로 정렬된 리스트에서 특정 값의 위치를 찾는 알고리즘
- 모든 값을 순회해야 하는 일반적인 Search보다 더 빠르다는 장점이 있음
- 중앙값을 찾는 값에 비교
  + (중앙값) > (찾는 값) : 중앙 값 기준으로 왼쪽(작은 부분)을 탐색
  + (중앙값) < (찾는 값) : 중앙 값 기준으로 오른쪽(큰 부분)을 탐색   

## 이진탐색 프로세스
1. left를 0으로 초기화, right를 검색하는 리스트(배열)의 마지막 원소의 인덱스로 초기화
2. mid 변수를 (left+right)/2로 설정하며 계속해서 탐색
3. left > right가 되는 순간 탐색이 종료되고 그전에 해당 값을 찾으면 종료

## 코딩테스트
### 수 찾기
- https://www.acmicpc.net/problem/1920
- N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
- https://github.com/HarkjinDev/Security/blob/main/Algorithm/BinarySearch/BAEKJOON_1920.py
