N, M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if cards[i] + cards[j] + cards[k] <= M and cards[i] + cards[j] + cards[k] > ans:
                ans = cards[i] + cards[j] + cards[k]

print(ans)