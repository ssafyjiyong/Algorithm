Col, Row = map(int, input().split())
n = int(input())

all_col = [0, Col]
all_row = [0, Row]


for i in range(n):
    option, here = map(int, input().split())
    if option == 0:
        all_row.append(here)
    else:
        all_col.append(here)

all_col.sort()
all_row.sort()

max_col = 0
max_row = 0

for i in range(1, len(all_col)):
    if all_col[i] - all_col[i-1] > max_col:
        max_col = all_col[i] - all_col[i-1]

for i in range(1, len(all_row)):
    if all_row[i] - all_row[i-1] > max_row:
        max_row = all_row[i] - all_row[i-1]

print(max_col * max_row)