from collections import deque

N = int(input())
q = deque()
lst = []
for _ in range(N):
    lst.append(tuple(map(str, input().split())))

for i in lst:
    if i[0] == 'push':
        q.append(i[1])
    elif i[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif i[0] == 'size':
        print(len(q))
    elif i[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif i[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])