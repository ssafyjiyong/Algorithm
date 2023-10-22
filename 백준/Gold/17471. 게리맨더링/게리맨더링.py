from itertools import combinations
from collections import deque


def bfs(combi_list):
    q = deque()
    q.append(combi_list[0])
    v = [0]*N
    Sum = 0
    while q:
        now = q.popleft()
        v[now] = 1
        Sum += populations[now]
        for i in connections[now]:
            if v[i] == 1:
                continue
            if i in combi_list:
                v[i] = 1
                q.append(i)
    return Sum, sum(v)


N = int(input())
populations = list(map(int, input().split()))
info = []
for i in range(N):
    info.append(i)

connections = []
for _ in range(N):
    connections.append(list(map(int, input().split())))
for i in connections:
    i.pop(0)
    for j in range(len(i)):
        i[j] -= 1


Mn = 21e8

for i in range(1, N//2+1):
    combis = list(combinations(info, i))
    for combi in combis:
        Sum1, checker1 = bfs(combi)
        Sum2, checker2 = bfs([i for i in range(N) if i not in combi])
        if checker1 + checker2 == N:
            Mn = min(Mn, abs(Sum1-Sum2))

if Mn == 21e8:
    print(-1)
else:
    print(Mn)