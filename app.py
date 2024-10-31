from flask import Flask, render_template, jsonify, request
import random as rd

app = Flask(__name__)

# Tamaño de la matriz y configuración inicial
size_matrix = 10
matrix = [[0 for _ in range(size_matrix)] for _ in range(size_matrix)]
vacuum_position = [rd.randrange(size_matrix), rd.randrange(size_matrix)]
count_movements = 0
trash_collected = 0
mode = 'random'  # Inicialmente en modo aleatorio
trash_positions = []  # Para almacenar las posiciones de la basura

# Función para colocar basura en la matriz
def place_trash():
    while sum([sum(row) for row in matrix]) < 10:
        r = rd.randrange(size_matrix)
        c = rd.randrange(size_matrix)
        if (r != vacuum_position[0] or c != vacuum_position[1]) and matrix[r][c] != 1:
            matrix[r][c] = 1
            trash_positions.append([r, c])

# Inicializar posiciones de basura
place_trash()

@app.route('/')
def index():
    return render_template('interfaz.html')


def snake_route(vacuum_position):
    row, col = vacuum_position

    # Si estamos en la última fila
    if row == size_matrix - 1:
        if col == 0:  # Si está en la esquina inferior izquierda
            # Mover hacia arriba hasta la primera fila
            row = 0
            col = 0  # Reiniciar a la primera columna
        else:  # Si no está en la esquina inferior izquierda, mover a la izquierda
            col -= 1
    elif row % 2 == 0:  # Fila par: mover a la derecha
        if col < size_matrix - 1:  # Si no está en el extremo derecho
            col += 1
        else:  # Si está en el extremo derecho, bajar
            row += 1
    else:  # Fila impar: mover a la izquierda
        if col > 0:  # Si no está en el extremo izquierdo
            col -= 1
        else:  # Si está en el extremo izquierdo, bajar
            row += 1

    # No permitir que la fila sea menor que 0
    if row < 0:
        row = 0

    return [row, col]


def spiral_route(vacuum_position):
    # Inicializar variables si es la primera llamada
    if not hasattr(spiral_route, "visited"):
        spiral_route.visited = set()  # Almacenar celdas visitadas
        spiral_route.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba
        spiral_route.current_direction = 0  # Índice de dirección actual
        spiral_route.steps = 0  # Pasos en la dirección actual
        spiral_route.change_direction_after = 1  # Pasos antes de cambiar de dirección
        spiral_route.layer = 0  # Capa actual (cerca del borde)

        # Marcar la posición inicial como visitada
        spiral_route.visited.add(tuple(vacuum_position))

    row, col = vacuum_position

    # Intentar mover en la dirección actual
    for _ in range(4):  # Intentar en las 4 direcciones
        dr, dc = spiral_route.directions[spiral_route.current_direction]
        new_row = row + dr
        new_col = col + dc

        # Comprobar si la nueva posición está dentro de los límites y no ha sido visitada
        if 0 <= new_row < size_matrix and 0 <= new_col < size_matrix and (new_row, new_col) not in spiral_route.visited:
            vacuum_position[0], vacuum_position[1] = new_row, new_col  # Mover a la nueva posición
            spiral_route.visited.add((new_row, new_col))  # Marcar como visitada
            spiral_route.steps += 1  # Contar el paso
            return vacuum_position  # Salir una vez que se mueva exitosamente

        # Cambiar de dirección si no se puede mover
        spiral_route.current_direction = (spiral_route.current_direction + 1) % 4

    return vacuum_position  # Devolver la posición actual si no se pudo mover






@app.route('/move')
def move_vacuum():
    global vacuum_position, count_movements, matrix, trash_collected, mode, trash_positions

    if mode == 'random':
        option = rd.randint(1, 4)
        if option == 1:  # Arriba
            if vacuum_position[1] > 0:
                vacuum_position[1] -= 1
        elif option == 2:  # Abajo
            if vacuum_position[1] < size_matrix - 1:
                vacuum_position[1] += 1
        elif option == 3:  # Izquierda
            if vacuum_position[0] > 0:
                vacuum_position[0] -= 1
        elif option == 4:  # Derecha
            if vacuum_position[0] < size_matrix - 1:
                vacuum_position[0] += 1
    elif mode == 'short route':
        if trash_positions:
            next_position = short_route(vacuum_position, trash_positions)
            vacuum_position = next_position
    elif mode == 'snake':
        vacuum_position = snake_route(vacuum_position)
    elif mode == 'spiral':
        vacuum_position = spiral_route(vacuum_position)

    if matrix[vacuum_position[0]][vacuum_position[1]] == 1:
        collect_trash()

    count_movements += 1

    return jsonify({
        'matrix': matrix,
        'vacuum_position': vacuum_position,
        'count_movements': count_movements,
        'trash_collected': trash_collected
    })

@app.route('/reset_matrix')
def reset_matrix():
    global matrix, vacuum_position, trash_collected, trash_positions
    # Reiniciar matriz
    matrix = [[0 for _ in range(size_matrix)] for _ in range(size_matrix)]
    vacuum_position = [rd.randrange(size_matrix), rd.randrange(size_matrix)]
    trash_collected = 0
    trash_positions.clear()  # Limpiar las posiciones de basura
    place_trash()  # Colocar nueva basura

    return jsonify({
        'matrix': matrix,
        'vacuum_position': vacuum_position,
        'trash_collected': trash_collected
    })

@app.route('/set_mode')
def set_mode():
    global mode, vacuum_position
    # Obtener el nuevo modo de los parámetros de la URL
    new_mode = request.args.get('mode')
    if new_mode in ['random', 'short route', 'spiral', 'snake']:
        mode = new_mode
        # Reiniciar la posición a la primera celda solo para los modos 'snake' y 'spiral'
        if mode in ['snake', 'spiral']:
            vacuum_position = [0, 0]  # Reiniciar la posición a la primera celda
    return jsonify({'mode': mode})


def short_route(vacuum_position, trash_positions):
    # Calcular la distancia a la basura más cercana
    closest_trash = min(trash_positions, key=lambda p: abs(vacuum_position[0] - p[0]) + abs(vacuum_position[1] - p[1]))
    
    # Determinar el movimiento necesario
    if vacuum_position[0] < closest_trash[0]:
        return [vacuum_position[0] + 1, vacuum_position[1]]  # Mover hacia abajo
    elif vacuum_position[0] > closest_trash[0]:
        return [vacuum_position[0] - 1, vacuum_position[1]]  # Mover hacia arriba
    elif vacuum_position[1] < closest_trash[1]:
        return [vacuum_position[0], vacuum_position[1] + 1]  # Mover hacia la derecha
    elif vacuum_position[1] > closest_trash[1]:
        return [vacuum_position[0], vacuum_position[1] - 1]  # Mover hacia la izquierda
    return vacuum_position  # No moverse si ya está en la posición de basura

def collect_trash():
    global trash_collected, matrix, trash_positions
    # Limpiar la basura de la matriz y aumentar el contador
    matrix[vacuum_position[0]][vacuum_position[1]] = 0  # Limpiar basura
    trash_collected += 1  # Incrementar contador de basura
    trash_positions.remove(vacuum_position)  # Remover la posición de la basura de la lista
    # Colocar nueva basura en un lugar aleatorio
#    place_new_trash()

#def place_new_trash():
    # Colocar nueva basura en la matriz
#    r = rd.randrange(size_matrix)
#    c = rd.randrange(size_matrix)
#    while matrix[r][c] == 1 or (r == vacuum_position[0] and c == vacuum_position[1]):
#        r = rd.randrange(size_matrix)
#        c = rd.randrange(size_matrix)
#    matrix[r][c] = 1  # Colocar nueva basura
#    trash_positions.append([r, c])  # Añadir a la lista de posiciones de basura

if __name__ == '__main__':
    app.run(debug=True)
