from collections import deque
N, M = map(int, input().split())

acc = [0] * (N+1)
info_lst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    info_lst[a].append(b)
    acc[b] += 1

q = deque()
for i in range(N+1):
    if acc[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    if now > 0:
        print(now, end=' ')
    for i in info_lst[now]:
        acc[i] -= 1
        if acc[i] == 0:
            q.append(i)