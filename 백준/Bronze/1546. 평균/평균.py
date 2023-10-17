N = int(input())
lst = list(map(int, input().split()))
n_lst = []
Mx = max(lst)
for i in lst:
    n_lst.append(i/Mx*100)
print(sum(n_lst)/len(n_lst))