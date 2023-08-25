N, K = map(int, input().split()) # N 전체 날짜 수, K 합 구할 연속 일
lst = list(map(int, input().split()))

Sum = 0
for i in range(K):
    Sum += lst[i]

Max = Sum
for i in range(N-K):
    Sum -= lst[i]
    Sum += lst[i+K]
    if Sum > Max:
        Max = Sum

print(Max)
