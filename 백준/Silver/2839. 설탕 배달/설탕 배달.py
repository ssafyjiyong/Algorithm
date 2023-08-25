N = int(input())

flag = 0
Min = 21e8

for i in range(1667):
    for j in range(1001):
        if (3*i) + (5*j) == N and (i+j) < Min:
            Min = i + j
            flag = 1

if flag == 1:
    print(Min)
else:
    print(-1)

