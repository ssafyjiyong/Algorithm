N = int(input())
A = list(map(int, input().split()))
Cap, Sub = map(int, input().split())

A_sub_come_in = []

for i in A:
    A_sub_come_in.append(i-Cap)

cnt = N

for i in A_sub_come_in:
    if i > Sub:
        cnt += i // Sub
        if i % Sub:
            cnt += 1
    elif Sub >= i > 0:
        cnt += 1

print(cnt)