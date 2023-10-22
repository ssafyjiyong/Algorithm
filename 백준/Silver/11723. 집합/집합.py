import sys
input = sys.stdin.readline

N = int(input())
S = 0
all = (1 << 20)-1

for _ in range(N):
    Order = list(input().split())
    if len(Order) > 1:
        Order[1] = int(Order[1])-1

    if Order[0] == 'add':
        S |= 1<<Order[1]
    elif Order[0] == 'remove':
        S &= ~(1<<Order[1])
    elif Order[0] == 'check':
        print(1 if S & (1 << Order[1]) else 0)
    elif Order[0] == 'toggle':
        S ^= 1<<Order[1]
    elif Order[0] == 'all':
        S = all
    else:
        S = 0