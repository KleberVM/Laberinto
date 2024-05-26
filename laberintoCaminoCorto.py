class Nodo:
    def __init__(self, x, y, obstaculo):
        self.x = x
        self.y = y
        self.obstaculo = obstaculo
        self.padre = None
        self.h = 0
        self.g = 0
        
def heuristic(nodo, meta):
    return abs(nodo.x - meta.x) + abs(nodo.y - meta.y)

def resolver_laberinto(laberinto, inicio, meta):# metodo usado A* para hallar la meta
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    nodos_visitados = []  # almacenamos los nodos visitados
    nodos_por_visitar = [inicio]# nodos por visitar , iniciamos con el primero que seria el inicio
    
    while nodos_por_visitar:#while continúa hasta que no haya más nodos por visitar (nodos_por_visitar sea vacía).
        # Ordenar nodos por su heurística + costo acumulado
        nodos_por_visitar.sort(key=lambda nodo: nodo.h + nodo.g)#En cada iteración del bucle, el método ordena los nodos por su heurística más el costo acumulado
        actual = nodos_por_visitar[0]#selecciona el primer nodo de la lista ordenada
        nodos_por_visitar = nodos_por_visitar[1:]
        
        if actual.x == meta.x and actual.y == meta.y: #Se comprueba si el nodo actual coincide con el nodo de destino
            path = []
            while actual.padre: #Si coinciden, se reconstruye el camino desde el nodo de inicio hasta el nodo de destino 
                path.append((actual.x, actual.y)) #
                actual = actual.padre
            path.append((actual.x, actual.y))
            path.reverse()
            return path#y se devuelve como solución.
        
        for movimiento in movimientos:#Si el nodo actual no es la meta, el método procede a explorar los vecinos del nodo actual.
            x = actual.x + movimiento[0]#Para cada movimiento posible en las direcciones arriba, abajo, izquierda y derecha
            y = actual.y + movimiento[1]
            if x < 0 or y < 0 or x >= len(laberinto) or y >= len(laberinto[0]) or laberinto[x][y] == 1:#se verifica si el movimiento es válido (si no se sale del laberinto o si no choca con un obstáculo)
                continue
            
            nuevo_nodo = Nodo(x, y, laberinto[x][y])#Si el movimiento es válido, se crea un nuevo nodo para ese movimiento
            nuevo_nodo.padre = actual#se establece su padre como el nodo actual
            nuevo_nodo.g = actual.g + 1  # Costo acumulado desde el nodo inicial,se calcula su costo acumulado (g) y su heurística (h)
            nuevo_nodo.h = heuristic(nuevo_nodo, meta)
            if nuevo_nodo not in nodos_visitados:#se agrega a la lista de nodos por visitar si aún no ha sido visitado
                nodos_visitados.append(nuevo_nodo)#El nodo actual se agrega a la lista de nodos visitados
                nodos_por_visitar.append(nuevo_nodo)#Los nuevos nodos por visitar se agregan a la lista de nodos por visitar para ser considerados en futuras iteraciones
    
    return None#Si el bucle while termina sin encontrar una solución, es decir, si no se encuentra ningún camino desde el nodo inicial hasta la meta, el método devuelve None.

# Ejemplo de uso
laberinto = [
    [0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0]
]

inicio = Nodo(0, 0, 0)# 
meta = Nodo(6, 8, 0)#los primeros 2 digitos del nodo representan la posicion , el ultimo digito 0 = vacio , 1 = si existe un muro o ya esta ocupado

print("Laberinto:")# imprimimos el la matriz
for fila in laberinto:
    print(fila)

print("\nResolviendo laberinto...")
solucion = resolver_laberinto(laberinto, inicio, meta)

if solucion:
    print("\nRecorrido del laberinto resuelto: ",solucion )

    for x, y in solucion:
        laberinto[x][y] = 8 # 8 = camino recorrido
    for fila in laberinto:# imprimimos el la matriz
        print(fila)
else:
    print("\nNo se encontró una solución.")