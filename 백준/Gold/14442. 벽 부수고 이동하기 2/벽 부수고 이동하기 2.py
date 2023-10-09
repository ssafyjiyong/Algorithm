from collections import deque
import sys

def bfs():
    q = deque()
    q.append((0, 0, K))
    v[0][0][K] = 1

    while q:
        ci, cj, power = q.popleft()
        # 만약에 끝 지점 방문했다면 리턴
        if ci == N-1 and cj == M-1:
            return v[ci][cj][power]

        for di, dj in ((1, 0), (-1 ,0), (0 ,1), (0 ,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M:
                # 다음 방문할 곳에 벽이 없다면
                if arr[ni][nj] == 0 and v[ni][nj][power] == 0:
                    v[ni][nj][power] = v[ci][cj][power]+1
                    q.append((ni,nj,power))
                elif power > 0 and arr[ni][nj]==1 and v[ni][nj][power-1]== 0 :
                    # 만약에 벽이고 깰 수 있는 힘이 있다면 
                    v[ni][nj ][power -1 ]=v[ci ][cj ][power ]+1 
                    q.append((ni,nj,power -1))
    return -1

input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
v = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

print(bfs())
