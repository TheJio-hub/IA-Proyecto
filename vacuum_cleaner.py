import random as rd

size_matrix = 10
trash_matrix = [[0 for _ in range(size_matrix)] for _ in range(size_matrix)]
vacuum_position = [0, 0]

vacuum_position[0] = rd.randrange(size_matrix)
vacuum_position[1] = rd.randrange(size_matrix)

while sum([sum(row) for row in trash_matrix]) < 13:
    r = rd.randrange(size_matrix)
    c = rd.randrange(size_matrix)
    if r != vacuum_position[0] and c != vacuum_position[1]:
        trash_matrix[r][c] = 1

count_movements = 0

while sum([sum(row) for row in trash_matrix]) > 0:
    option = rd.randint(1, 4)
    if option == 1:  # Up
        if vacuum_position[1] > 0:
            vacuum_position[1] -= 1
            count_movements += 1
    elif option == 2:  # Down
        if vacuum_position[1] < size_matrix - 1:
            vacuum_position[1] += 1
            count_movements += 1
    elif option == 3:  # Left
        if vacuum_position[0] > 0:
            vacuum_position[0] -= 1
            count_movements += 1
    elif option == 4:  # Right
        if vacuum_position[0] < size_matrix - 1:
            vacuum_position[0] += 1
            count_movements += 1

    # Clean the trash
    if trash_matrix[vacuum_position[0]][vacuum_position[1]] == 1:
        trash_matrix[vacuum_position[0]][vacuum_position[1]] = 0

def get_simulation_data():
    return {"matrix": trash_matrix, "vacuum_position": vacuum_position}
