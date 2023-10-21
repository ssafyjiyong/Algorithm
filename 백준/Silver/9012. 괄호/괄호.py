import sys
from collections import deque
input = sys.stdin.readline


T = int(input())
for _ in range(1, T+1):
    lst = list(map(str, input()))
    valid_check = deque()
    flag = 0

    if lst[0] == ')':
        flag = 1
        print('NO')
        continue

    for i in lst:
        if i == '\n':
            break

        if i == '(':
            valid_check.append(i)
        else:
            if len(valid_check) == 0:
                flag = 1
                break
            a = valid_check.popleft()
            if a == ')':
                flag = 1
                break

    if len(valid_check) > 0:
        flag = 1

    if flag == 1:
        print('NO')
    else:
        print('YES')

