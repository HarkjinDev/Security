# GraphSearch

## Adjacency Materix(인접 행렬) - O(N+E)
![adjacency_materix](/Algorithm/GraphSearch/adjacency_materix.png)
- 인접행렬은 그래프의 노드를 2차원 배열로 만든 것
- 완성된 배열의 모양은 1, 2, 3, 4, 5, 6의 정점을 연결하는 노드에 다른 노드들이 인접 정점이라면 1, 아니면 0을 넣음
- 장점
  1) 차원 배열 안에 모든 정점들의 간선 정보를 담기 때문에 배열의 위치를 확인하면 두 점에 대한 연결 정보를 조회할 때 O(1) 의 시간 복잡도면 가능
  2) 구현이 비교적 간단
- 단점
  1) 모든 정점에 대해 간선 정보를 대입해야 하므로 O(n²) 의 시간복잡도가 소요
  2) 무조건 2차원 배열이 필요하기에 필요 이상의 공간이 낭비

## Adjacency List(인접 리스트) - O(N²)
![adjacency_list](/Algorithm/GraphSearch/adjacency_list.png)
- 그래프의 노드들을 리스트로 표현한것
- 주로 정점의 리스트 배열을 만들어 관계를 설정해줌으로써 구현
- 장점
  1) 정점들의 연결 정보를 탐색할 때 O(n) 의 시간이면 가능 (n: 간선의 갯수)
  2) 필요한 만큼의 공간만 사용하기때문에 공간의 낭비가 적음
- 단점
  1) 특정 두 점이 연결되었는지 확인하려면 인접행렬에 비해 시간이 오래 걸림 (배열보다 search 속도느림)
  2) 구현이 비교적 어렵다.

## DFS(Depth First Search, 깊이 우선 탐색)
- 루트 노드나 임의의 노드에서 시작하여 최대로 진입할 수 잇는 깊이까지 탐색한 후 돌아와 다른 노드로 탐색하는 방식
- Stack을 활용
- 재귀함수로 사용 가능
- 장점
  1) 현 경로상의 노드들만 기억하면 되므로 저장공간 수요가 비교적 적음
  2) 목표 노드가 깊은 단계에 있을 경우 해를 빨리 구할 수 있음
- 단점
  1) 해가 없는 경로가 깊을 경우 탐색시간이 오래 걸릴 수 있음
  2) 얻어진 해가 최단 경로가 된다는 보장이 없음

## BFS(Breadth Frist Search, 너비 우선 탐색)
- 루트 노드나 임의의 노드에서 시작하여 인접한 노드를 먼저 모두 확인한 후 다음 depth를 탐색
- Queue를 사용
- 특징
  1) 시작 정점부터 거리가 가까운 정점의 순서로 탐색
  2) 재귀적으로 동작하지 않음
  3) FIFO 원칙으로 탐색

## DFS vs BFS
![graphsearch](/Algorithm/GraphSearch/graphsearch.gif)
- 모든 정점 방문 : DFS나 BFS 동일
- 경로의 특징을 둘 때 : DFS
- 최단거리 : BFS가 유리
- 검색 대상이 크다면 : DFS 고려
- 검색 대상이 크지 않고, 대상이 별로 멀지 않다면 : BFS 고려

## 코딩테스트
### DFS와 BFS
- https://www.acmicpc.net/problem/1260
- 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
- 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
- https://github.com/HarkjinDev/Security/blob/main/Algorithm/GraphSearch/BAEKJOON_1260.py
### 데스나이트
- https://www.acmicpc.net/problem/16948
- 게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다. 
- 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.
- 크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자. 체스판의 행과 열은 0번부터 시작한다.
- 데스 나이트는 체스판 밖으로 벗어날 수 없다.
- https://github.com/HarkjinDev/Security/blob/main/Algorithm/GraphSearch/BAEKJOON_16948.py
### 미로 탐색
- https://www.acmicpc.net/problem/2178
- N×M크기의 배열로 표현되는 미로가 있다.
- 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
- 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
- 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
- https://github.com/HarkjinDev/Security/blob/main/Algorithm/GraphSearch/BAEKJOON_2178.py
