import random as rd

trash_positions = []

size_matrix = 10
trash_matrix = [[0 for _ in range(size_matrix)] for _ in range(size_matrix)]
vacuum_position = [size_matrix // 2, size_matrix // 2]  

while sum([sum(row) for row in trash_matrix]) < 13:
    r = rd.randrange(size_matrix)
    c = rd.randrange(size_matrix)

    if [r, c] != vacuum_position:
        trash_matrix[r][c] = 1
        trash_positions.append([r, c])

print("Posición inicial de la aspiradora:", vacuum_position)
print("Matriz de basura inicial:")
for row in trash_matrix:
    print(row)

count_movements = 0

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_direction = 0 
steps_in_direction = 1  
change_direction_count = 0  

# Límites de la espiral
left_limit = vacuum_position[0] - 1
right_limit = vacuum_position[0] + 1
top_limit = vacuum_position[1] - 1
bottom_limit = vacuum_position[1] + 1

while sum([sum(row) for row in trash_matrix]) > 0:
    # Movimiento en la dirección actual
    for _ in range(steps_in_direction):
        dx, dy = directions[current_direction]
        vacuum_position[0] += dx
        vacuum_position[1] += dy
        count_movements += 1
        
        if trash_matrix[vacuum_position[0]][vacuum_position[1]] == 1:
            trash_matrix[vacuum_position[0]][vacuum_position[1]] = 0
        
        if sum([sum(row) for row in trash_matrix]) == 0:
            break

    # Cambiar dirección (derecha -> abajo -> izquierda -> arriba)
    current_direction = (current_direction + 1) % 4
    change_direction_count += 1
    
    if change_direction_count % 2 == 0:
        steps_in_direction += 1
    
    # Actualizar los límites de la espiral
    left_limit = max(0, vacuum_position[0] - steps_in_direction // 2)
    right_limit = min(size_matrix - 1, vacuum_position[0] + steps_in_direction // 2)
    top_limit = max(0, vacuum_position[1] - steps_in_direction // 2)
    bottom_limit = min(size_matrix - 1, vacuum_position[1] + steps_in_direction // 2)

print("Posición final de la aspiradora:", vacuum_position)
print("Matriz de basura final:")
for row in trash_matrix:
    print(row)
print("Total de movimientos:", count_movements)
