from collections import defaultdict

laberinto = [
    ["0", "0", "0", "0", "█", "█", "█", "█", "█"],
    ["█", "0", "█", "0", "0", "█", "0", "0", "█"],
    ["█", "█", "█", "0", "█", "M", "0", "0", "█"],
    ["█", "0", "0", "0", "0", "█", "0", "0", "█"],
    ["█", "0", "0", "█", "0", "0", "0", "█", "█"],
    ["█", "I", "0", "█", "0", "0", "0", "0", "0"],
    ["█", "█", "█", "█", "█", "█", "█", "█", "0"]
]

def imprimirMatriz(matrix):
    for fila in matrix:
        print(" ".join(fila))

def crearGrafo(laberinto):
    grafico = defaultdict(list)
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == "█":  # Ignorar muros
                continue
            if j < len(laberinto[0]) - 1 and laberinto[i][j + 1] != "█":  # Derecha
                grafico[(i, j)].append((i, j + 1))
            if j > 0 and laberinto[i][j - 1] != "█":  # Izquierda
                grafico[(i, j)].append((i, j - 1))
            if i < len(laberinto) - 1 and laberinto[i + 1][j] != "█":  # Abajo
                grafico[(i, j)].append((i + 1, j))
            if i > 0 and laberinto[i - 1][j] != "█":  # Arriba
                grafico[(i, j)].append((i - 1, j))
    return grafico

def dfs(grafico, start, end, visita=None):
    if visita is None:
        visita = set()
    visita.add(start)
    if start == end:
        return [start]
    for vecino in grafico[start]:
        if vecino not in visita:
            camino = dfs(grafico, vecino, end, visita.copy())
            if camino:
                return [start] + camino
    return None

grafico = crearGrafo(laberinto)

# Encontrar el inicio ("I") y el final ("M")
inicioNodos = []
finNodos = []
for i in range(len(laberinto)):
    for j in range(len(laberinto[0])):
        if laberinto[i][j] == "I":
            inicioNodos.append((i, j))
        if laberinto[i][j] == "M":
            finNodos.append((i, j))

# Buscar el camino desde cada inicio hasta cada final
for inicioNodo in inicioNodos:
    for finNodo in finNodos:
        camino = dfs(grafico, inicioNodo, finNodo)
        if camino:
            print("laberinto")
            imprimirMatriz(laberinto)
            print("El camino encontrado es:", camino)
            print("\nRecorrido:")
            for x, y in camino:
                if laberinto[x][y] != "I" and laberinto[x][y] != "M":
                    laberinto[x][y] = "O"
            imprimirMatriz(laberinto)
            print()
            break
    else:
        continue
    break
else:
    print("No hay camino posible desde ningún nodo de inicio al nodo final.")