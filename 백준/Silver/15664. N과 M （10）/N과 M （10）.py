from itertools import combinations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans_list = list(combinations(lst,m))
ans_set = set()
for i in ans_list:
    ans_set.add(i)

ans = list(ans_set)
for i in ans:
    print(*i)