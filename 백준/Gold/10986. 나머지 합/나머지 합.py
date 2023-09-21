import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
nams = [0]*M
cnt = 0

for i in range(1, N):
    num[i] += num[i-1]

for i in num:
    nams[i % M] += 1

for i in num:
    if i % M == 0:
        cnt += 1

for i in nams:
    cnt += i * (i-1) // 2

print(cnt)