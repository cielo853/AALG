import random

def contar_multiplos(matriz):
    if len(matriz) == 0:
        return 0
    if len(matriz) == 1:
        return contar_fila(matriz[0])
    mid = len(matriz) // 2
    izq = matriz[:mid]
    der = matriz[mid:]
    return contar_multiplos(izq) + contar_multiplos(der)

def contar_fila(fila):
    if len(fila) == 0:
        return 0
    if len(fila) == 1:
        return 1 if (fila[0] % 5 == 0 or fila[0] % 7 == 0) else 0
    mid = len(fila) // 2
    izq = fila[:mid]
    der = fila[mid:]
    return contar_fila(izq) + contar_fila(der)

def main():
    N = 11 
    matriz = [[random.randint(99, 999) for _ in range(N)] for _ in range(N)]
    
    print("Matriz generada (11x11):")
    for fila in matriz:   
        print(" ".join(f"{x:3d}" for x in fila))  
    
    cantidad = contar_multiplos(matriz)
    print(f"\nCantidad de números múltiplos de 5 o 7: {cantidad}")

if __name__ == "__main__":
    main()
