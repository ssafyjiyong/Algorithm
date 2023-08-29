a = int(input())
end = int(a ** 0.5)
check = [0] * (a + 1)

for i in range(2, end+1):
    if check[i] == 1:
        continue
    for j in range(i+i, a + 1, i):
        check[j] = 1

prime_nums = []
for i in range(2, a + 1):
    if check[i] == 0:
        prime_nums.append(i)

H,L,Sum,cnt = 0,0,0,0

if len(prime_nums) >= 1:
    while 1:
        if Sum == a:
            cnt += 1
        if Sum >= a or H == len(prime_nums):
            Sum -= prime_nums[L]
            L += 1
        elif Sum < a:
            Sum += prime_nums[H]
            H += 1
        if L == len(prime_nums) or prime_nums[L] > a:
            break

    print(cnt)
else:
    print(0)