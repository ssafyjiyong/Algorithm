di = [-1,1,0,0]
dj = [0,0,-1,1]

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0
    for i in range(n):
        for j in range(m):
            cnt = arr[i][j]
            for k in range(4):
                for p in range(1, arr[i][j]+1):
                    dy = i + di[k] * p
                    dx = j + dj[k] * p
                    if 0 <= dy < n and 0 <= dx < m:
                        cnt += arr[dy][dx]
                if cnt > max_v:
                    max_v = cnt
    print(f'#{tc} {max_v}')