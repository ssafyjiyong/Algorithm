N = int(input())
paper = [[0]*100 for _ in range(100)]

for _ in range(N):
    A, B = map(int, input().split())
    for i in range(A, A + 10):
        for j in range(B, B + 10):
            paper[i][j] = 1

dy = [-1,1,0,0]
dx = [0,0,-1,1]

cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if ny < 0 or nx < 0 or ny >= 100 or nx >= 100 or paper[ny][nx] == 0:
                    cnt += 1

print(cnt)