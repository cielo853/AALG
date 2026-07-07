import random
def fuerza_bruta(monedas, i, j):
    if i > j:
        return 0
    if i == j:
        return monedas[i]
    tomar_izq = monedas[i] + min(
        fuerza_bruta(monedas, i+2, j),
        fuerza_bruta(monedas, i+1, j-1)
    )
    tomar_der = monedas[j] + min(
        fuerza_bruta(monedas, i+1, j-1),
        fuerza_bruta(monedas, i, j-2)
    )
    return max(tomar_izq, tomar_der)


def turno_pc_fuerza_bruta(monedas, izq, der):
    if monedas[izq] + min(
        fuerza_bruta(monedas, izq+2, der) if izq+2 <= der else 0,
        fuerza_bruta(monedas, izq+1, der-1) if izq+1 <= der-1 else 0
    ) >= monedas[der] + min(
        fuerza_bruta(monedas, izq+1, der-1) if izq+1 <= der-1 else 0,
        fuerza_bruta(monedas, izq, der-2) if izq <= der-2 else 0
    ):
        return 'I'
    else:
        return 'D'


def main():
    print("==============================")
    print("   JUEGO DE MONEDAS")
    print("   Modo: Fuerza Bruta")
    print("==============================")


    monedas = [random.randint(1, 20) for _ in range(6)]
    print(f"\nMonedas generadas: {monedas}")


    izq = 0
    der = len(monedas) - 1
    puntaje_tu = 0
    puntaje_pc = 0


    while izq <= der:
        print(f"\nMonedas disponibles: {monedas[izq:der+1]}")


        print("\n--- TU TURNO ---")
        print(f"Izquierda = {monedas[izq]}  |  Derecha = {monedas[der]}")
        eleccion = ""
        while eleccion not in ["I", "i", "D", "d"]:
            eleccion = input("Elige (I)zquierda o (D)erecha: ")
            if eleccion not in ["I", "i", "D", "d"]:
                print("Opcion invalida. Por favor elige I o D")


        if eleccion in ["I", "i"]:
            print(f"Tomaste: {monedas[izq]}")
            puntaje_tu += monedas[izq]
            izq += 1
        else:
            print(f"Tomaste: {monedas[der]}")
            puntaje_tu += monedas[der]
            der -= 1


        print(f"Tu puntaje: {puntaje_tu}")


        if izq > der:
            break


        print("\n--- TURNO PC ---")
        decision = turno_pc_fuerza_bruta(monedas, izq, der)


        if decision == 'I':
            print(f"PC toma izquierda: {monedas[izq]}")
            puntaje_pc += monedas[izq]
            izq += 1
        else:
            print(f"PC toma derecha: {monedas[der]}")
            puntaje_pc += monedas[der]
            der -= 1


        print(f"Puntaje PC: {puntaje_pc}")


    print("\n==============================")
    print("      RESULTADO FINAL")
    print("==============================")
    print(f"Tu puntaje : {puntaje_tu}")
    print(f"Puntaje PC : {puntaje_pc}")


    if puntaje_tu > puntaje_pc:
        print("GANASTE!")
    elif puntaje_pc > puntaje_tu:
        print("LA PC GANO!")
    else:
        print("EMPATE!")


if __name__ == "__main__":
    main()
