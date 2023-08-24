L = int(input())
N = int(input())
wish_paper = []

# 가장 많이 케익 기대한 사람
Max_pcs = 0
greedy = 0
for i in range(N):
    From, To = map(int, input().split())
    wish_paper.append([From, To])
    pieces = To - From + 1
    if pieces > Max_pcs:
        Max_pcs = pieces
        greedy = i+1
print(greedy)

# 실제로 많이 받은 사람
cake = [0] * (L+1)
person = 1
for i in wish_paper:
    for j in range(i[0], i[1]+1):
        if cake[j] == 0:
            cake[j] = person
    person += 1

Max = 0
who = 0
for i in range(1,N+1):
    if cake.count(i) > Max:
        Max = cake.count(i)
        who = i

print(who)