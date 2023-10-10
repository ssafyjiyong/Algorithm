T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())

    if N <= H:
        YY = N
    else:
        if N%H != 0:
            YY = N%H
        else:
            YY = H

    if N <= H:
        XX = 1
    else:
        if N%H != 0:
            XX = N//H+1
        else:
            XX = N//H

    print(YY, end='')
    if XX < 10:
        print(0, end='')
        print(XX)
    else:
        print(XX)
