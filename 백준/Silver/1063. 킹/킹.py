King, Stone, N = map(str, input().split())
N = int(N)
Move_to = []
for _ in range(N):
    Move_to.append(input())

# 체스판 생성
chess_board = [[0]*8 for _ in range(8)]

# 킹의 좌표 찾기
King_y = 8 - int(King[1])
King_x = ord(King[0])-65

# 돌의 좌표 찾기
Stone_y = 8 - int(Stone[1])
Stone_x = ord(Stone[0])-65


# 이동값 정보 입력하기
Order_letter = ['R','L','B','T','RT','LT','RB','LB']
Order_commend = [[0,1], [0,-1], [1,0], [-1,0], [-1,1], [-1,-1], [1,1], [1,-1]]

# 이동 값 정보 찾고 적용
for i in Move_to:
    for k in range(8):
        if i == Order_letter[k] and 0 <= King_y + Order_commend[k][0] < 8 and 0 <= King_x + Order_commend[k][1] < 8:
            # 돌이랑 겹치는 경우
            if King_y + Order_commend[k][0] == Stone_y and King_x + Order_commend[k][1] == Stone_x:
                if 0 <= Stone_y + Order_commend[k][0] < 8 and 0 <= Stone_x + Order_commend[k][1] < 8:
                    Stone_y += Order_commend[k][0]
                    Stone_x += Order_commend[k][1]
                    King_y += Order_commend[k][0]
                    King_x += Order_commend[k][1]
                break
            # 돌이랑 겹치지 않는 경우
            else:
                King_y += Order_commend[k][0]
                King_x += Order_commend[k][1]
                break

# 킹의 좌표 찾기
King_y = 8 - int(King_y)
King_x = chr(King_x+65)

# 돌의 좌표 찾기
Stone_y = 8 - int(Stone_y)
Stone_x = chr(Stone_x+65)

print(f'{King_x}{King_y}')
print(f'{Stone_x}{Stone_y}')