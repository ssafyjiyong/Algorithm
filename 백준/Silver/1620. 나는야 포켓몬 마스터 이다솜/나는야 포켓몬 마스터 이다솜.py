N, M = map(int, input().split())
D = dict()
for i in range(1,N+1):
    a = str(input())
    D[str(i)]=a
    D[a]=str(i)

for _ in range(M):
    b = str(input())
    print(D.get(b))