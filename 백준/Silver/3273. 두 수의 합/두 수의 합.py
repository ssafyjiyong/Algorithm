n = int(input())
arr = list(map(int, input().split()))
x = int(input())

L, cnt, Sum = 0,0,0
H = -1

arr.sort()

while 1:
    if abs(L) + abs(H) == n:
        break
    if arr[H] + arr[L] == x:
        cnt += 1
    if arr[H] + arr[L] <= x:
        L += 1
    else:
        H -= 1

print(cnt)