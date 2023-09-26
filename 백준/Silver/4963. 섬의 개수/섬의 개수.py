import sys
from collections import deque
input = sys.stdin.readline

def bfs(si, sj):
    global visited, arr, ans
    q = deque()
    q.append((si, sj))
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
            ni = ci + di
            nj = cj + dj
            if ni < 0 or nj < 0 or ni >= h or nj >= w:
                continue
            if visited[ni][nj] == 1:
                continue
            if arr[ni][nj] == 0:
                continue
            visited[ni][nj] = 1
            q.append((ni, nj))

while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    visited = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                ans += 1
                bfs(i, j)

    print(ans)