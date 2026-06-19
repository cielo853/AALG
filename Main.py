import time
import os


# Laberinto
laberinto = [
    ['F',1,1,1,0,1,1,1,1],
    [-2,0,0,-1,0,1,0,1,0],
    [1,1,0,-1,1,1,1,1,0],
    [1,0,1,-1,0,0,0,-1,0],
    [1,1,1,1,1,1,1,1,0],
    [-1,0,0,0,0,0,0,1,1],
    [1,1,1,1,-1,1,1,1,0],
    [1,0,0,0,1,0,0,1,1],
    ['I',1,-1,1,1,1,0,1,1]
]
filas = 9
columnas = 9

inicio = (8,0)
final = (0,0)

vidas_iniciales = 3


camino = []
visitado = []

solucion = [
    [0]*9 for i in range(9)
]
def limpiar():
    os.system("cls" if os.name=="nt" else "clear")
def mostrar(matriz):
    for fila in matriz:
        print(" ".join(str(x).rjust(2) for x in fila))
    print()
def mostrar_paso(x,y,vidas):
    copia=[fila[:] for fila in laberinto]
    for a,b in camino:
        copia[a][b]="*"
    copia[x][y]="R"
    limpiar()
    print("LABERINTO - MOVIMIENTO DEL RATON")
    print("--------------------------------")
    mostrar(copia)
    print("Vidas restantes:",vidas)
    time.sleep(0.5)
def es_valido(x,y):
    if x<0 or y<0 or x>=filas or y>=columnas:
        return False
    if laberinto[x][y]==0:
        return False
    if (x,y) in visitado:
        return False
    return True
def backtracking(x,y,vidas):
    if vidas <=0:
        return False
    if (x,y)==final:

        solucion[x][y]="F"
        return True
    visitado.append((x,y))
    camino.append((x,y))
    mostrar_paso(x,y,vidas)
    valor=laberinto[x][y]
    if isinstance(valor,int):
        if valor==-1:
            vidas-=1
        elif valor==-2:
            vidas-=2
    #Movimientos
    movimientos=[
        (1,0),   
        (0,1),   
        (-1,0),  
        (0,-1)   
    ]
    for dx,dy in movimientos:
        nx=x+dx
        ny=y+dy
        if es_valido(nx,ny):
            if backtracking(nx,ny,vidas):
                solucion[x][y]="*"
                return True
    # retroceso
    camino.pop()
    visitado.remove((x,y))
    mostrar_paso(x,y,vidas)
    return False
print("LABERINTO ORIGINAL")
print("------------------")
mostrar(laberinto)
print("Buscando camino...\n")
resultado=backtracking(
    inicio[0],
    inicio[1],
    vidas_iniciales
)
if resultado:
    solucion[inicio[0]][inicio[1]]="I"
    print("SALIDA ENCONTRADA")
    print("CAMINO FINAL:")
    mostrar(solucion)
else:
    print(" NO EXISTE CAMINO VIABLE")