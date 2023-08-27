for _ in range(4):
    sj1, si1, ej1, ei1, sj2, si2, ej2, ei2 = map(int, input().split())
    if ej1 < sj2 or ej2 < sj1 or ei1 < si2 or ei2 < si1:
        ans = 'd'
    elif ej1 == sj2 or ej2 == sj1:
        if ei1 == si2 or ei2 == si1:
            ans = 'c'
        else:
            ans = 'b'
    elif ei1 == si2 or ei2 == si1:
        ans = 'b'
    else:
        ans = 'a'

    print(ans)