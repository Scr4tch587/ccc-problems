#AC
x = input()
y = input()
list1 = x.split()
list2 = y.split()
start_col = int(list1[0])
start_row = int(list1[1])
end_col = int(list2[0])
end_row = int(list2[1])


grid = []
movement = [
    [1, 2],
    [1, -2],
    [2, 1],
    [2, -1],
    [-1, 2],
    [-1, -2],
    [-2, 1],
    [-2, -1]
]

for i in range(8):
    row = []
    for j in range(8):
        row.append(6)
    grid.append(row)
visited = []
def move(x, y, moves):
    if moves > 6:
        return
    elif 0 < x < 9 and 0 < y < 9 and moves < grid[x-1][y-1]:
        #print(str(x) + " " + str(y))
        grid[x-1][y-1] = moves
        for direction in movement:
            move(x + direction[0], y + direction[1], moves + 1)
    else:
        return

move(start_row, start_col, 0)
print(grid[end_row-1][end_col-1])
