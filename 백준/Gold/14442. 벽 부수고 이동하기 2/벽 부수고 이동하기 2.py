from collections import deque
import sys
input = sys.stdin.readline

def bfs(si, sj, power):
    q = deque()
    q.append((si, sj, power))
    while q:
        ci, cj, power = q.popleft()
        # 만약에 끝에 도달 했다면 리턴
        if ci == N-1 and cj == M-1:
            return print(v[ci][cj][power])

        # 만약에 힘이 없는데 끝 지점 방문했다면 리턴
        if v[-1][-1][0] != 0:
            return print(v[-1][-1][0])

        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if ni<0 or nj<0 or ni>=N or nj>=M:
                continue

            # 다음 방문할 곳에 벽이 없고 방문한 적도 없다면
            if arr[ni][nj] == 0 and v[ni][nj][power] == 0:
                # 방문해보자
                v[ni][nj][power] = v[ci][cj][power] + 1
                q.append((ni, nj, power))

            # 만약에 벽이고 깰 수 있는 힘도 있고, 지금 힘으로 방문한 적이 없다면
            elif arr[ni][nj] == 1 and power > 0 and v[ni][nj][power-1]==0:
                v[ni][nj][power-1] = v[ci][cj][power] + 1
                q.append((ni, nj, power-1))
                
    return print(-1)

N, M, K = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
v = [[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
v[0][0][K] = 1

bfs(0, 0, K)
