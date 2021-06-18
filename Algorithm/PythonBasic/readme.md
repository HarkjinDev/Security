# Python Basic

### 한개의 정수 입력 받기
`a = int(sys.stdin.readline())`

### 정해진 개수 입력 받기
`a,b,c = map(int,sys.stdin.readline().split())`

### 임의의 개수 입력 받기
`data = list(map(int,sys.stdin.readline().split()))`

### 공백/개행 없이 입력 받기
`a = int(sys.stdin.readline().strip())`

### 임의의 개수의 정수 n줄 입력받아 2차원 리스트에 저장할 때
```
data = []   
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
```

### 문자열 n줄을 입력받아 리스트 저장
```
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
```

### 두 인수 입력 받기
`a, b = input().split()`   
ex) split(:) : 으로 나누기

### 실수 출력
`format(a,".2f")`

### 16진수 출력
`print('%x'%n, '%X'%n) // x소문자 X대문자`

### 8진수 출력
`print('%O'%n, '%o'%n)`

### 입력값 X진수로 바꾸기(ex, 16진수)
`int(input(),base=16)`

### 공백없이 출력
`print(......, sep='')`

### 줄바꿈 없이 출력
`print(...., end=' ')`

### NxM 값 받아서 2차원 배열 생성
```
N, M = map(int, stdin.readline().split())

stack = [[0]*N for _ in range(M)]
```

