lst = []
for _ in range(9):
    lst.append(int(input()))

Mx = max(lst)

for i in range(len(lst)):
    if lst[i] == Mx:
        print(Mx)
        print(i+1)
        break