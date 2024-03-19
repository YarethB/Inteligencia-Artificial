import time

def solve_maze(maze, start, end):  # En esta parte definimos la función DFS
    stack = [start]  # Aqui iniciamos una pila con un nodo inicial
    while stack:  # Creamos un bucle que sera el principal de DFS
        x, y = stack[-1]  # Con esto podemos obtener las coordenadas actuales

        if (x, y) == end:  # Verificamos si se llego al final 
            return True, stack  # Retornamos la solucion encontrada y el camino

        maze[x][y] = '2'  # Marcamos el nodo actual como visitado

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Creamos un bucle para visitar cada direccion vecina
            nx, ny = x + dx, y + dy  # Obtenemos las coordenadas de los vecinos

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):  # Marcamos los limites
                if maze[nx][ny] == '0' or maze[nx][ny] == 'E':  # Verificamos si el camino esta libre o es el final
                    stack.append((nx, ny))  # Agregamos las coordenadas del vecino al stack
                    break  # Detiene el bucle para explorar el siguiente vecino
        else:
            stack.pop()  # Si no hay vecinos validos retrocede

    return False, []  # Si no hay solucion retorna falso y una lista vacia

def find_solution_time(maze, start, end):
    start_time = time.time()
    solved, path = solve_maze(maze, start, end) # Llamamos a la funcion del algoritmo DFS
    if solved:  # Si encontramos una solución
        print("Laberinto Resuelto")  # Imprimimos un mensaje de laberinto resuelto
        for x, y in path:  # Iteramos sobre el camino encontrado
            if maze[x][y] != 'S' and maze[x][y] != 'E':  # Si no es el punto inicial ni el final
                maze[x][y] = '*'  # Marcar el camino en el laberinto con un asterisco
        for row in maze:  # Imprimimos el laberinto con el camino encontrado
            print("".join(row))
    else:  # Si no se encontramos una solución
        print("No solution found.")  # Imprimimos un mensaje de no solución encontrada

    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    # Definimos el laberinto
    maze = [
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['S', '1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '0', '1', '1', '1'],
        ['1', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '0', '1', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '0', '1', '1', '1', '0', '1'],
        ['1', '0', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['0', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
        ['0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
        ['0', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '0', '0', '0', '1', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', 'E'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    ]

    start = (1, 0)  # Marcamos las coordenadas del punto inicial
    end = (19, 19)  # Marcamos las coordenadas del punto final
    solution_time = find_solution_time(maze, start, end)
    print("Time invertido: {:.6f} segundos".format(solution_time))

    
    