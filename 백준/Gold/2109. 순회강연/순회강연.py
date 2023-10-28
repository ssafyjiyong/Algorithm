n = int(input())
info = []
Mx_d = 0
for _ in range(n):
    p, d = map(int, input().split())
    if d > Mx_d:
        Mx_d = d
    info.append((d,p))

std_info = sorted(info, key=lambda x:(-x[1]))

v = [0]*(Mx_d+1)
v[0] = 1
ans = 0
for d, p in std_info:
    if v[d] == 0:
        v[d] = 1
        ans += p
    else:
        a = d-1
        while a > 0:
            if v[a] == 0:
                v[a] = 1
                ans += p
                break
            else:
                a-=1
print(ans)