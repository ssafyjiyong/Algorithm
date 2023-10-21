N = int(input())
cards = list(map(int, input().split()))
M = int(input())
wants = list(map(int, input().split()))

cards.sort()

cnt = {}
for i in cards:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in wants:
    print(cnt.get(i, 0), end=' ')