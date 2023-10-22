import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i,j))
            v[i][j] = 1
        if arr[i][j] == -1:
            v[i][j] = -1

while q:
    ci, cj = q.popleft()
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci+di, cj+dj
        if ni<0 or nj<0 or ni>=N or nj>=M:
            continue
        if arr[ni][nj] == -1:
            continue
        if v[ni][nj] != 0:
            continue
        v[ni][nj] = v[ci][cj]+1
        q.append((ni,nj))

flag = 0
Mx = 0
for i in range(N):
    for j in range(M):
        if v[i][j] == 0:
            flag = 1
            break
        Mx = max(Mx, v[i][j])
    if flag == 1:
        break

if flag == 0:
    print(Mx-1)
else:
    print(-1)