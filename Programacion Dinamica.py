import random


def construir_tabla_dp(monedas):
    n = len(monedas)
    dp = [[0] * n for _ in range(n)]


    for i in range(n):
        dp[i][i] = monedas[i]


    for largo in range(2, n+1):
        for i in range(n - largo + 1):
            j = i + largo - 1
            x = dp[i+2][j] if i+2 <= j else 0
            y = dp[i+1][j-1] if i+1 <= j-1 else 0
            z = dp[i][j-2] if i <= j-2 else 0
            dp[i][j] = max(
                monedas[i] + min(x, y),
                monedas[j] + min(y, z)
            )
    return dp


def turno_pc_dp(dp, monedas, izq, der):
    res_a = dp[izq+1][der] if izq+1 <= der else 0
    res_b = dp[izq][der-1] if izq <= der-1 else 0


    if res_a <= res_b:
        return 'I'
    else:
        return 'D'


def main():
    print("==============================")
    print("   JUEGO DE MONEDAS")
    print("   Modo: Programacion Dinamica")
    print("==============================")


    monedas = [random.randint(1, 20) for _ in range(6)]
    print(f"\nMonedas generadas: {monedas}")


    dp = construir_tabla_dp(monedas)


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
        decision = turno_pc_dp(dp, monedas, izq, der)


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
DeprecationWarning