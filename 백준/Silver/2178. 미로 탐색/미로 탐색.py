from collections import deque

def bfs(si, sj):
    global visited
    queue = deque()
    queue.append((si, sj))
    while queue:
        ci, cj = queue.popleft()
        for di, dj in ((-1,0), (0,1), (1,0), (0,-1)):
            ni = di + ci
            nj = dj + cj
            if 0 > ni or 0 > nj or ni >= N or nj >= M:
                continue
            if visited[ni][nj] != 0:
                continue
            if maze[ni][nj] == 0:
                continue
            visited[ni][nj] += visited[ci][cj] + 1
            queue.append((ni, nj))

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1

bfs(0, 0)

print(visited[-1][-1])