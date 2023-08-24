H, W = map(int, input().split())
sky = [list(map(str, input())) for _ in range(H)]
forecast = [[-1]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if sky[i][j] == 'c':
            forecast[i][j] = 0

x = 1
for i in range(H):
    for j in range(W):
        if forecast[i][j] == 0:
            for k in range(j+1, W):
                if forecast[i][k] == 0:
                    break
                forecast[i][k] = x
                x += 1
            x=1
            
for i in forecast:
    print(*i)