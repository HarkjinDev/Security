# ACM 호텔
# https://www.acmicpc.net/problem/10250

T = int(input())

for _ in range(T):
    # H(호텔층수), W(각 층의 방 수), N(몇 번째 손님)
    H, W, N = map(int, input().split())

    num = N // H + 1
    floor = N % H
    if N % H == 0:
        num = N // H
        floor = H
    print(f'{floor*100+num}')


      



