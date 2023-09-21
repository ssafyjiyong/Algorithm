s1 = str(input())
s2 = str(input())
l1 = len(s1)
l2 = len(s2)

dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

for i in range(1, l1+1):
    for j in range(1, l2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

y = l1
x = l2
ans = []
while 1:
    if dp[y][x] == 0:
        break
    if dp[y-1][x] == dp[y][x-1] == dp[y][x]-1:
        ans.append(s2[x-1])
        x -= 1
        y -= 1
    else:
        if dp[y-1][x] > dp[y][x-1]:
            y -= 1
        else:
            x -= 1
ans.reverse()
print(''.join(ans))