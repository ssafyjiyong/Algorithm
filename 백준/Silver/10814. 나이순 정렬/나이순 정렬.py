N = int(input())
lst = []
for i in range(N):
    a, b = map(str, input().split())
    lst.append((int(a),b,i))
std_lst = sorted(lst, key=lambda x:(x[0], x[2]))
for i in std_lst:
    print(i[0], i[1])