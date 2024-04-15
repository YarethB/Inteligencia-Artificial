# Importa la clase PriorityQueue desde el módulo queue
from queue import PriorityQueue

# Define la clase PuzzleNode para representar nodos en el rompecabezas
class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        # Inicializa los atributos del nodo
        self.state = state  # Estado del rompecabezas
        self.parent = parent  # Nodo padre
        self.move = move  # Movimiento que llevó a este estado desde el padre
        self.depth = depth  # Profundidad en el árbol de búsqueda
        self.cost = 0  # Costo total

    # Define el método para comparar nodos basado en el costo
    def __lt__(self, other):
        return self.cost < other.cost

    # Define el método para verificar la igualdad de nodos basado en el estado
    def __eq__(self, other):
        return self.state == other.state

    # Define el método para calcular el hash del nodo basado en el estado
    def __hash__(self):
        return hash(str(self.state))

# Función para calcular la distancia de Manhattan de un estado dado
def manhattan_distance(state):
    n = len(state)
    distance = 0
    # Itera sobre todas las celdas del estado
    for i in range(n):
        for j in range(n):
            # Calcula la distancia de Manhattan para cada celda
            if state[i][j] != 0:
                target_row = (state[i][j] - 1) // n
                target_col = (state[i][j] - 1) % n
                distance += abs(i - target_row) + abs(j - target_col)
    return distance

# Función para obtener los estados vecinos de un estado dado
def get_neighbors(state):
    n = len(state)
    # Encuentra la posición del espacio en blanco
    blank_row, blank_col = find_blank(state)
    neighbors = []
    # Define los movimientos posibles: arriba, abajo, izquierda, derecha
    for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = blank_row + move[0], blank_col + move[1]
        # Verifica si el movimiento es válido dentro de los límites del rompecabezas
        if 0 <= new_row < n and 0 <= new_col < n:
            # Crea un nuevo estado intercambiando el espacio en blanco con una celda vecina
            new_state = [row[:] for row in state]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            neighbors.append(new_state)
    return neighbors

# Función para encontrar la posición del espacio en blanco en un estado dado
def find_blank(state):
    n = len(state)
    for i in range(n):
        for j in range(n):
            if state[i][j] == 0:
                return i, j

# Función para resolver el rompecabezas de 8-puzzle utilizando el algoritmo A*
def solve_8_puzzle(initial_state):
    # Estado objetivo del rompecabezas
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    # Inicializa la cola de prioridad y el conjunto de estados visitados
    queue = PriorityQueue()
    visited = set()
    
    # Crea el nodo inicial del rompecabezas
    initial_node = PuzzleNode(initial_state)
    # Calcula el costo del nodo inicial utilizando la distancia de Manhattan
    initial_node.cost = manhattan_distance(initial_state)
    # Agrega el nodo inicial a la cola de prioridad
    queue.put(initial_node)
    
    # Realiza la búsqueda hasta que la cola de prioridad esté vacía
    while not queue.empty():
        # Obtiene el nodo actual de la cola de prioridad
        current_node = queue.get()
        current_state = current_node.state
        
        # Verifica si el estado actual es el estado objetivo
        if current_state == goal_state:
            return current_node
        
        # Verifica si el estado actual ya ha sido visitado
        if tuple(map(tuple, current_state)) in visited:
            continue
        
        # Agrega el estado actual al conjunto de estados visitados
        visited.add(tuple(map(tuple, current_state)))
        
        # Genera y agrega los estados vecinos a la cola de prioridad
        for neighbor_state in get_neighbors(current_state):
            # Crea un nuevo nodo para el estado vecino
            neighbor_node = PuzzleNode(neighbor_state, current_node, move=(find_blank(current_state)[0] - find_blank(neighbor_state)[0], find_blank(current_state)[1] - find_blank(neighbor_state)[1]))
            # Actualiza la profundidad y el costo del nodo vecino
            neighbor_node.depth = current_node.depth + 1
            neighbor_node.cost = neighbor_node.depth + manhattan_distance(neighbor_state)
            # Agrega el nodo vecino a la cola de prioridad
            queue.put(neighbor_node)
    
    # Retorna None si no se encuentra solución
    return None

# Función para imprimir la solución encontrada
def print_solution(solution_node):
    if solution_node is None:
        print("No solution found.")
    else:
        moves = []
        while solution_node.parent:
            moves.append(solution_node.move)
            solution_node = solution_node.parent
        moves.reverse()
        print("Solution found in", len(moves), "moves:", moves)

# Ejemplo de uso del algoritmo de resolución del rompecabezas
initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution_node = solve_8_puzzle(initial_state)
print_solution(solution_node)
