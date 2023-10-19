from collections import deque

q=deque()
N=int(input())
for i in range(1, N+1):
    q.append(i)

while 1:
    if len(q) == 1:
        print(q[0])
        break

    q.popleft()
    a = q.popleft()
    q.append(a)