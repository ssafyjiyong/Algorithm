from collections import deque

q=[]

N, K = map(int, input().split())
for i in range(1, N+1):
    q.append(i)

ans = []

while 1:
    if len(q) == 1:
        ans.append(q[0])
        break

    if len(q) >= K:
        ans.append(q.pop(K-1))
        for _ in range(K-1):
            a = q.pop(0)
            q.append(a)

    else:
        x = K % len(q)
        ans.append(q.pop(x - 1))
        if x == 0:
            continue
        for _ in range(x - 1):
            a = q.pop(0)
            q.append(a)

print('<', end='')
for i in range(len(ans)-1):
    print(ans[i], end='')
    print(', ', end='')
print(ans[-1], end='')
print('>', end='')