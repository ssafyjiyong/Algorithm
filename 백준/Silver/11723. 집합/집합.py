import sys
input = sys.stdin.readline

N = int(input())
S = set()
for _ in range(N):
    Order = list(map(str, input().split()))

    if Order[0] == 'add':
        S.add(int(Order[1]))
    elif Order[0] == 'remove' and int(Order[1]) in S:
        S.remove(int(Order[1]))
    elif Order[0] == 'check':
        print(+(int(Order[1]) in S))
    elif Order[0] == 'toggle':
        if int(Order[1]) in S:
            S.remove(int(Order[1]))
        else:
            S.add(int(Order[1]))
    elif Order[0] == 'all':
        S = set(i for i in range(1,21))
    elif Order[0] == 'empty':
        S = set()
