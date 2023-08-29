N = int(input())
paper = [[0]*1001 for _ in range(1001)]

for p in range(N):

    x, y, horizon, vertical = map(int, input().split())

    for i in range(y, y+vertical):
        for j in range(x, x+horizon):
            paper[i][j] = p+1

for p in range(N):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if paper[i][j] == p+1:
                cnt += 1
    print(cnt)