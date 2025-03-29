N = int(input())
lst = list(map(int, input().split()))
cnt = 0
lst.sort()

for i in range(N):
    target = lst[i]
    a = 0
    b = N-1
    while a < b:
        if a == i:
            a+=1
            continue
        if b == i:
            b-=1
            continue
        if lst[a] + lst[b] == target:
            cnt += 1
            break
        elif lst[a] + lst[b] > target:
            b-=1
        else:
            a+=1

print(cnt)