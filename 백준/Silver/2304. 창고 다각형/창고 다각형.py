N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

std_lst = sorted(lst, key=lambda x:(x[0], x[1]))

Mx = std_lst[0][1]
mx_pnt = std_lst[0][0]
mx_idx = 0
for i in range(1, len(std_lst)):
    if std_lst[i][1] > Mx:
        Mx = std_lst[i][1]
        mx_pnt = std_lst[i][0]
        mx_idx = i

ans = 0
high_top = std_lst[0][1]
high_idx = std_lst[0][0]
for i in range(1, mx_idx+1):
    if std_lst[i][1] > high_top:
        ans += high_top * (std_lst[i][0]-high_idx)
        high_top = std_lst[i][1]
        high_idx = std_lst[i][0]

high_top = std_lst[-1][1]
high_idx = std_lst[-1][0]
same_pnt = 0
for i in range(-1, mx_idx-len(std_lst)-1, -1):
    if std_lst[i][1] > high_top:
        ans += high_top * (high_idx-std_lst[i][0])
        high_top = std_lst[i][1]
        high_idx = std_lst[i][0]
    if std_lst[i][1] == Mx:
        same_pnt = std_lst[i][0]
        break

if same_pnt != 0:
    ans += (same_pnt-mx_pnt) * high_top

print(ans+Mx)
