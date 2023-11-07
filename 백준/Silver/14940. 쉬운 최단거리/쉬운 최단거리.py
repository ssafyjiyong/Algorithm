from collections import deque

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = di+ci, dj+cj
            if ni < 0 or nj < 0 or ni >= n or nj >=m:
                continue
            if v[ni][nj] != -1:
                continue
            if arr[ni][nj] != 1:
                continue
            v[ni][nj] = v[ci][cj]+1
            q.append((ni,nj))


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[-1]*m for _ in range(n)]
flag = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            v[i][j] = 0
            bfs(i,j)
        if arr[i][j] == 0:
            v[i][j] = 0

for i in v:
    print(*i)