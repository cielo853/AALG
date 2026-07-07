Funcion JuegoMonedaFuerzaBruta <- FuerzaBruta(monedas, i, j)
    Definir valorOptimo, opcionIzquierda, opcionDerecha Como Entero;
    Si i > j Entonces
        valorOptimo <- 0;
    Sino
        Si i == j Entonces
            valorOptimo <- monedas[i];
        Sino
            opcionIzquierda <- monedas[i] + Minimo(FuerzaBruta(monedas, i + 2, j), FuerzaBruta(monedas, i + 1, j - 1));
            opcionDerecha <- monedas[j] + Minimo(FuerzaBruta(monedas, i + 1, j - 1), FuerzaBruta(monedas, i, j - 2));
            valorOptimo <- Maximo(opcionIzquierda, opcionDerecha);
        FinSi
    FinSi
FinFuncion
Funcion res <- Maximo(a, b)
    Definir res Como Entero;
    Si a > b Entonces 
        res <- a; 
    Sino 
        res <- b; 
    FinSi
FinFuncion
Funcion res <- Minimo(a, b)
    Definir res Como Entero;
    Si a < b Entonces 
        res <- a; 
    Sino 
        res <- b; 
    FinSi
FinFuncion
Algoritmo JuegoMonedasInteractivo
    Definir cantidadMonedas, i, izquierda, derecha, seleccion, turno, puntuacionJ1, puntuacionJ2 Como Entero;
    Definir monedas Como Entero;
    Dimension monedas[100];
    Escribir "Ingrese la cantidad de monedas para el juego (Ejemplo: 4, 6, 8, 10):";
    Leer cantidadMonedas;
    Para i <- 0 Hasta cantidadMonedas - 1 Con Paso 1 Hacer
        Escribir "Ingrese el valor para la moneda en la posición ", i + 1, ":";
        Leer monedas[i];
    FinPara
    izquierda <- 0;
    derecha <- cantidadMonedas - 1;
    turno <- 1;
    puntuacionJ1 <- 0;
    puntuacionJ2 <- 0;
    
    Escribir "-------------------------------------------------------";
    Escribir "Predicción:";
    Escribir "El Jugador 1 puede asegurar un puntaje máximo de: ", FuerzaBruta(monedas, izquierda, derecha);
    Escribir "-------------------------------------------------------";
    Mientras izquierda <= derecha Hacer
        Escribir "";
        Escribir "FILA ACTUAL DE MONEDAS:";
        Para i <- izquierda Hasta derecha Con Paso 1 Hacer
            Escribir Sin Saltar "[ ", monedas[i], " ] ";
        FinPara
        Escribir "";
        Escribir "Puntajes actualizados -> Jugador 1: ", puntuacionJ1, " | Jugador 2: ", puntuacionJ2;
        Escribir "Turno del JUGADOR ", turno;
        Repetir
            Escribir "Elija una opcion: (1) Moneda Izquierda [", monedas[izquierda], "] o (2) Moneda Derecha [", monedas[derecha], "]";
            Leer seleccion;
            Si seleccion <> 1 Y seleccion <> 2 Entonces
                Escribir "Opcion no valida. Por favor ingresa un numero correcto (1 o 2).";
            FinSi
        Hasta Que seleccion == 1 O seleccion == 2
        Si seleccion == 1 Entonces
            Si turno == 1 Entonces
                puntuacionJ1 <- puntuacionJ1 + monedas[izquierda];
            Sino
                puntuacionJ2 <- puntuacionJ2 + monedas[izquierda];
            FinSi
            izquierda <- izquierda + 1;
        Sino
            Si turno == 1 Entonces
                puntuacionJ1 <- puntuacionJ1 + monedas[derecha];
            Sino
                puntuacionJ2 <- puntuacionJ2 + monedas[derecha];
            FinSi
            derecha <- derecha - 1;
        FinSi
        Si turno == 1 Entonces
            turno <- 2;
        Sino
            turno <- 1;
        FinSi
    FinMientras
    
    Escribir "";
    Escribir "-------------------------------------------------------";
    Escribir "¡JUEGO TERMINADO!";
    Escribir "Puntaje Final -> Jugador 1: ", puntuacionJ1, " | Jugador 2: ", puntuacionJ2;
    Si puntuacionJ1 > puntuacionJ2 Entonces
        Escribir "¡Gana el Jugador 1!";
    Sino
        Si puntuacionJ2 > puntuacionJ1 Entonces
            Escribir "¡Gana el Jugador 2!";
        Sino
            Escribir "¡Empate!";
        FinSi
    FinSi
    Escribir "-------------------------------------------------------";
FinAlgoritmo
