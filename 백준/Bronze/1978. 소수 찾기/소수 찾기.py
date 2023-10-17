def prime_num(value):
    not_prime_set = {1}
    for i in range(2, value+1):
        for j in range(value, i, -1):
            if j%i==0:
                not_prime_set.add(j)
    return not_prime_set


N = int(input())
lst = list(map(int, input().split()))
Mx = max(lst)
cnt = 0

for i in lst:
    if i not in prime_num(Mx):
        cnt += 1

print(cnt)