N = int(input())
lst = []
for _ in range(N):
    lst.append(str(input()))
std_lst = sorted(lst, key=lambda x:(len(x), x))

ans = []
for i in std_lst:
    if i not in ans:
        ans.append(i)

for i in ans:
    print(i)