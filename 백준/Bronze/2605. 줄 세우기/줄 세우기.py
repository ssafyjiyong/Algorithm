N = int(input())
order = list(map(int, input().split()))
arr = []

a = 1

for i in range(N):
    arr.append(a)
    for j in range(order[i]):
        arr.append(arr.pop(-(order[i])-1))
    a += 1

print(*arr)
