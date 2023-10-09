h, m = map(int, input().split())
if m >= 45:
    m -= 45
    print(h, m)
else:
    m = 60-(45-m)
    h -= 1
    if h >= 0:
        print(h, m)
    else:
        h = 23
        print(h, m)
