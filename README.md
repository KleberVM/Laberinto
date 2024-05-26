# Laberinto

Laberinto resuelto por estrategias de busqueda sin informacion (metodo primero en profundidad) traza la primera ruta que encuentra sin importar si es la mas larga y busqueda informada (metodo busqueda A* tambien conocido como primero lo mejor ) minimiza el costo estimado total de la solucion en palabras mas simples halla la ruta mas corta

## Caracteristicas
- Programa hecho en python
- No tiene interfaz grafica
- Usa la terminal para mostrar los resultados de la ruta
## Como funciona

Para agregar un laberinto se debe editar el codigo

### LaberintoCaminoCorto.py

- 1 representa los muros
- 0 representa el camino
```python
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
```
### LaberintoSinCaminoCorto.py
- 0 representa el camino
- █ representa el muro
- I representa el inicio
- M representa la meta
```python
laberinto = [
    ["0", "0", "0", "0", "█", "█", "█", "█", "█"],
    ["█", "0", "█", "0", "0", "█", "0", "0", "█"],
    ["█", "█", "█", "0", "█", "M", "0", "0", "█"],
    ["█", "0", "0", "0", "0", "█", "0", "0", "█"],
    ["█", "0", "0", "█", "0", "0", "0", "█", "█"],
    ["█", "I", "0", "█", "0", "0", "0", "0", "0"],
    ["█", "█", "█", "█", "█", "█", "█", "█", "0"]
]
```
