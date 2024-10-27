import random as rd

def lenght(pos1,pos2):
    return (pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2

def short_route(vacuum,trash_positions,size_matrix):
    circuit = []
    while trash_positions:
        trash = trash_positions[0].copy()
        for trash_p in trash_positions:
            if lenght(vacuum,trash) < lenght(vacuum,trash_p):
                trash = trash_p.copy()

        while not vacuum == trash:
            positions = []
            for option in range(1,5):
                if option == 1: # Up
                    if vacuum[1] > 0:
                        positions.append([vacuum[0],vacuum[1]-1])
                elif option == 2:   # Down
                    if vacuum[1] < size_matrix-1:
                        positions.append([vacuum[0],vacuum[1]+1])
                elif option == 3:   # Left
                    if vacuum[0] > 0:
                        positions.append([vacuum[0]-1,vacuum[1]])
                elif option == 4:   # Right
                    if vacuum[0] < size_matrix-1:
                        positions.append([vacuum[0]+1,vacuum[1]])

            vacuum_p = positions[0].copy()
            for position in positions:
                if lenght(position,trash) < lenght(vacuum_p,trash):
                    vacuum_p = position.copy()

            circuit.append(vacuum_p.copy())
            vacuum = vacuum_p.copy()

        trash_positions.remove(trash)
    return circuit



trash_positions = []

size_matrix = 10
trash_matrix = [[0 for _ in range(size_matrix)] for _ in range(size_matrix)]
vacuum_position = [0,0]

vacuum_position[0] = rd.randrange(size_matrix)
vacuum_position[1] = rd.randrange(size_matrix)

while sum([sum(row) for row in trash_matrix]) < 13:
    r = rd.randrange(size_matrix)
    c = rd.randrange(size_matrix)

    if r != vacuum_position[0] and c != vacuum_position[1]:
        trash_matrix[r][c] = 1
        trash_positions.append([r,c])

circuit = short_route(vacuum_position.copy(),trash_positions,size_matrix)

print(circuit)
print(len(circuit))
print(vacuum_position)
print(trash_matrix)
count_movements = 0

while circuit:
    vacuum_position = circuit[0].copy()
    count_movements += 1
    
    if trash_matrix[vacuum_position[0]][vacuum_position[1]] == 1:
        trash_matrix[vacuum_position[0]][vacuum_position[1]] = 0
    
    circuit.remove(vacuum_position)

print(vacuum_position)
print(trash_matrix)
print(count_movements)
