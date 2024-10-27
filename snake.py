import random as rd

trash_positions = []

size_matrix = 10
trash_matrix = [[0 for _ in range(size_matrix)] for _ in range(size_matrix)]
vacuum_position = [0,0]

vacuum_position[0] = 0
vacuum_position[1] = 0

while sum([sum(row) for row in trash_matrix]) < 13:
    r = rd.randrange(size_matrix)
    c = rd.randrange(size_matrix)

    if r != vacuum_position[0] and c != vacuum_position[1]:
        trash_matrix[r][c] = 1
        trash_positions.append([r,c])

print(vacuum_position)
print(trash_matrix)
count_movements = 0
option = 4

while sum([sum(row) for row in trash_matrix]) > 0:
    if option == 1: # Up
        if vacuum_position[1] > 0:
            vacuum_position[1]-=1
            count_movements += 1
    elif option == 2:   # Down
        if vacuum_position[1] < size_matrix-1:
            vacuum_position[1]+=1
            count_movements += 1
        if vacuum_position[0] == 0:
            option = 4
        else:
            option = 3
    elif option == 3:   # Left
        if vacuum_position[0] > 0:
            vacuum_position[0]-=1
            count_movements += 1
        if vacuum_position[0] == 0:
            option = 2
    elif option == 4:   # Right
        if vacuum_position[0] < size_matrix-1:
            vacuum_position[0]+=1
            count_movements += 1
        if vacuum_position[0] == size_matrix-1:
            option = 2
    
    if trash_matrix[vacuum_position[0]][vacuum_position[1]] == 1:
        trash_matrix[vacuum_position[0]][vacuum_position[1]] = 0


print(vacuum_position)
print(trash_matrix)
print(count_movements)
