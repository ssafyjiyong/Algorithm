from collections import deque

N, L = map(int, input().split())
lst = list(map(int, input().split()))
mydeque = deque();

for i in range(N):
    while mydeque and mydeque[-1][1] > lst[i]:
        mydeque.pop()
    mydeque.append([i, lst[i]])
    if mydeque[0][0] <= i -L:
        mydeque.popleft()
    print(mydeque[0][1], end=' ')