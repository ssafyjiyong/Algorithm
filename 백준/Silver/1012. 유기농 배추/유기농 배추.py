from collections import deque
def bfs(si, sj):
    q = deque()
    q.append((si,sj))
    v = [[0]*M for _ in range(N)]
    v[si][sj] = 1
    while q:
        ci, cj = q.pop()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = di+ci, dj+cj
            if ni<0 or nj<0 or ni>=N or nj>=M:
                continue
            if v[ni][nj] == 1:
                continue
            if arr[ni][nj] == 1:
                v[ni][nj] = 1
                arr[ni][nj] = 0
                q.append((ni,nj))


T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        j ,i = map(int, input().split())
        arr[i][j] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                bfs(i,j)
    print(cnt)
