N = int(input())
lst = list(map(str, input().split()))
cards = [0,1,2,3,4,5,6,7,8,9]

Mx_ans = [9-p for p in range(N+1)]
Mn_ans = [p for p in range(N+1)]

repeat_Mx = 0
repeat_Mn = 0

for i in range(N):
    if lst[i] == '<':
        repeat_Mx += 1

for i in range(N):
    if lst[i] == '>':
        repeat_Mn += 1

for _ in range(repeat_Mx):
    for i in range(N):
        if lst[i] == '<':
            if Mx_ans[i] > Mx_ans[i+1]:
                Mx_ans[i], Mx_ans[i+1] = Mx_ans[i+1], Mx_ans[i]

for _ in range(repeat_Mn):
    for i in range(N):
        if lst[i] == '>':
            if Mn_ans[i] < Mn_ans[i+1]:
                Mn_ans[i], Mn_ans[i+1] = Mn_ans[i+1], Mn_ans[i]

for i in Mx_ans:
    print(i, end='')
print()
for i in Mn_ans:
    print(i, end='')