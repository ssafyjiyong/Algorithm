from collections import deque

N, M = map(int, input().split())
info = [[] for _ in range(N)]
acc = [0]*N
ans = [0]*N
order_box = []

for _ in range(M):
    A, B = map(int, input().split())
    info[B-1].append(A)
    acc[B-1] += 1

q = deque()
for i in range(N):
    if acc[i] == 0:
        q.append(i)
        ans[i] = 1

while q:
    now = q.popleft()
    order_box.append(now + 1)
    for i in range(N):
        if acc[i] == 1 and acc[info[i][0]-1] == 0:
            acc[i] -= 1
            q.append(i)
        elif acc[i] > 1:
            acc[i] -= 1

for p in info:
    if len(p) != 0:
        for i in range(N):
            if len(info[i]) == 1:
                if ans[i] < ans[info[i][0]-1] + 1:
                    ans[i] = ans[info[i][0]-1] + 1
            elif len(info[i]) >= 1:
                for j in range(len(info[i])):
                    if ans[i] < ans[info[i][j]-1] + 1:
                        ans[i] = ans[info[i][j]-1] + 1
                        
print(*ans)