from copy import deepcopy

N = int(input())

# [0, 5] [1, 3] [2, 4]

dices = [list(map(int, input().split())) for _ in range(N)]
Max = -21e8

for p in range(6):
    dices_copy = deepcopy(dices)
    for j in range(6):
        if dices[1][j] == dices[0][p]:
            if p == 0:
                dices[0].pop(0)
                dices[0].pop(4)
            elif p == 1:
                dices[0].pop(1)
                dices[0].pop(2)
            elif p == 2:
                dices[0].pop(2)
                dices[0].pop(3)
            elif p == 3:
                dices[0].pop(3)
                dices[0].pop(1)
            elif p == 4:
                dices[0].pop(4)
                dices[0].pop(2)
            elif p == 5:
                dices[0].pop(5)
                dices[0].pop(0)

            if j == 0:
                below = dices[1].pop(j)
                above = dices[1].pop(4)
                break
            elif j == 1:
                below = dices[1].pop(j)
                above = dices[1].pop(2)
                break
            elif j == 2:
                below = dices[1].pop(j)
                above = dices[1].pop(3)
                break
            elif j == 3:
                below = dices[1].pop(j)
                above = dices[1].pop(1)
                break
            elif j == 4:
                below = dices[1].pop(j)
                above = dices[1].pop(2)
                break
            elif j == 5:
                below = dices[1].pop(j)
                above = dices[1].pop(0)
                break

    for i in range(2, N):
        for j in range(6):
            if dices[i][j] == above:
                if j == 0:
                    below = dices[i].pop(j)
                    above = dices[i].pop(4)
                    break
                elif j == 1:
                    below = dices[i].pop(j)
                    above = dices[i].pop(2)
                    break
                elif j == 2:
                    below = dices[i].pop(j)
                    above = dices[i].pop(3)
                    break
                elif j == 3:
                    below = dices[i].pop(j)
                    above = dices[i].pop(1)
                    break
                elif j == 4:
                    below = dices[i].pop(j)
                    above = dices[i].pop(2)
                    break
                elif j == 5:
                    below = dices[i].pop(j)
                    above = dices[i].pop(0)
                    break

    Sum = 0
    for i in dices:
        Sum += max(i)
    if Sum > Max:
        Max = Sum
    dices = deepcopy(dices_copy)

print(Max)
