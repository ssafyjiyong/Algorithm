import sys
input = sys.stdin.readline

def dfs(start):
    global cnt
    cnt += 1
    for i in arr[start]:
        if visited[i] == 1:
            continue
        visited[i] = 1
        dfs(i)

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
cnt = 0
visited = [0] * (N+1)
visited[0] = 1
visited[1] = 1
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(1)

print(cnt-1)
