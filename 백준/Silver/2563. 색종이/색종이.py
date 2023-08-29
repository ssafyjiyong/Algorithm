N = int(input())
paper = [[0]*101 for _ in range(101)]


for i in range(N):
    A, B = map(int, input().split())

    for i in range(A, A+10):
        for j in range(B, B+10):
            paper[i][j] = 1

ans = 0

for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            ans += 1

print(ans)