#11/15 TLE
import sys
input1 = sys.stdin.readline()
rows = int(input1)
input2 = sys.stdin.readline()
columns = int(input2)
grid = []
for i in range(rows):
    row = sys.stdin.readline()
    row = row.split()
    row = list(map(int, row))
    grid.append(row)

start = grid[0][0]

location_dictionary = {}

for i in range(rows):
    for j in range(columns):
        if grid[i][j] in location_dictionary:
            locations = location_dictionary[grid[i][j]]
            locations.append((i + 1, j + 1))
            location_dictionary[grid[i][j]] = locations
        else:
            location_dictionary[grid[i][j]] = [(i + 1, j + 1)]
#print(location_dictionary)
visited = []
if rows * columns in location_dictionary:
    queue = location_dictionary[rows * columns]
    found = False
    while queue:
        location = queue[0]
        # print(location)
        if location in visited:
            pass
        else:
            if location == (1, 1):
                found = True
                break
            visited.append(queue[0])
            if location[0] * location[1] in location_dictionary:
                queue = queue + location_dictionary[location[0] * location[1]]
        queue.pop(0)

    if found == True:
        print("yes")
    else:
        print("no")
else:
    print("no")
