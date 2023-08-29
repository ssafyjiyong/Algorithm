Bingopan = [list(map(int, input().split())) for _ in range(5)]
Anounced = [list(map(int, input().split())) for _ in range(5)]

def bingo():

    cnt = 0

    for y in range(5):
        for x in range(5):
            cnt += 1

            for i in range(5):
                for j in range(5):
                    if Bingopan[i][j] == Anounced[y][x]:
                        Bingopan[i][j] = 'x'
                        bingo = 0

                        # 가로 빙고
                        for i in range(5):
                            r_bingo = 0
                            for j in range(5):
                                if Bingopan[i][j] == 'x':
                                    r_bingo += 1
                            if r_bingo == 5:
                                bingo += 1
                                if bingo == 3:
                                    return cnt

                        # 세로 빙고
                        for i in range(5):
                            c_bingo = 0
                            for j in range(5):
                                if Bingopan[j][i] == 'x':
                                    c_bingo += 1
                            if c_bingo == 5:
                                bingo += 1
                                if bingo == 3:
                                    return cnt

                        # 대각선 빙고(좌 - 우)
                        d_bingo = 0
                        for i in range(5):
                            if Bingopan[i][i] == 'x':
                                d_bingo += 1
                            if d_bingo == 5:
                                bingo += 1
                                if bingo == 3:
                                    return cnt

                        # 대각선 빙고(우 - 좌)
                        d_bingo_r = 0
                        for i in range(5):
                            if Bingopan[i][4-i] == 'x':
                                d_bingo_r += 1
                            if d_bingo_r == 5:
                                bingo += 1
                                if bingo == 3:
                                    return cnt

print(bingo())

