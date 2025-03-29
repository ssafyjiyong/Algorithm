N, M = map(int, input().split())
lst = list(map(int,input().split()))
ans = [0]
tmp = 0
for i in range(N):
    tmp+=lst[i]
    ans.append(tmp)

for i in range(M):
    a, b = list(map(int,input().split()))
    print(ans[b]-ans[a-1])