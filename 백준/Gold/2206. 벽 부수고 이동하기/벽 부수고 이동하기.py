from collections import deque

def bfs(si, sj, power):
    q = deque()
    q.append((si, sj, power))
    while q:
        ci, cj, power = q.popleft()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if ni<0 or nj<0 or ni>=N or nj>=M:
                continue
            # 다음 방문할 곳에 벽이 없고 방문한 적도 없다면
            if arr[ni][nj] == 0 and v[ni][nj][power] == 0:
                # 방문해보자
                v[ni][nj][power] = v[ci][cj][power] + 1
                q.append((ni, nj, power))
            # 만약에 벽이고 깰 수 있는 힘이 있다면
            if arr[ni][nj] == 1 and power == 1:
                v[ni][nj][power-1] = v[ci][cj][power] + 1
                q.append((ni, nj, power-1))
    if v[N-1][M-1][power] != 0:
        return print(v[N-1][M-1][power])
    else:
        return print(-1)

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
v = [[[0,0] for _ in range(M)] for _ in range(N)]
v[0][0][0] = 1
v[0][0][1] = 1

bfs(0, 0, 1)
