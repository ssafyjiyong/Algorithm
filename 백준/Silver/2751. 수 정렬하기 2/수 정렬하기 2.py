N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
std_lst = sorted(lst, key=lambda x:x)

for i in std_lst:
    print(i)
