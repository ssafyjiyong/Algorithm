from copy import deepcopy

kids = [int(input()) for _ in range(9)]

def whoisreal(kids):
    copy_kids = deepcopy(kids)
    for i in range(0,8):
        for j in range(i+1, 9):
            kids[i] = 0
            kids[j] = 0
            if sum(kids) == 100:
                return kids
            else:
                kids = deepcopy(copy_kids)


ans = whoisreal(kids)
ret = sorted(ans)
ret.pop(0)
ret.pop(0)

for i in ret:
    print(i)