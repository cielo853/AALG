Algoritmo JuegoMonedas_DP
	Definir monedas Como Entero
	Definir tabla Como Entero
	Definir n, i, j, largo, opA, opB, resA, resB Como Entero
	Definir izq, der, puntajeTu, puntajePC Como Entero
	Definir eleccion Como Caracter
	Definir continuar Como Logico
	
	Dimension monedas(6)
	Dimension tabla(6,6)
	
	n <- 6

	Escribir "Monedas generadas aleatoriamente:"
	Para i <- 1 Hasta n Con Paso 1 Hacer
		monedas(i) <- Aleatorio(1, 20)
		Escribir "Moneda ", i, ": ", monedas(i)
	FinPara
	

	Para i <- 1 Hasta n Con Paso 1 Hacer
		Para j <- 1 Hasta n Con Paso 1 Hacer
			tabla(i,j) <- 0
		FinPara
	FinPara
	

	Para i <- 1 Hasta n Con Paso 1 Hacer
		tabla(i,i) <- monedas(i)
	FinPara
	

	Para largo <- 2 Hasta n Con Paso 1 Hacer
		Para i <- 1 Hasta n-largo+1 Con Paso 1 Hacer
			j <- i + largo - 1
			
			Si i+2 <= j Entonces
				resA <- tabla(i+2,j)
				Si tabla(i+1,j-1) < resA Entonces
					resA <- tabla(i+1,j-1)
				FinSi
			SiNo
				resA <- 0
			FinSi
			
			Si i <= j-2 Entonces
				resB <- tabla(i+1,j-1)
				Si tabla(i,j-2) < resB Entonces
					resB <- tabla(i,j-2)
				FinSi
			SiNo
				resB <- 0
			FinSi
			
			opA <- monedas(i) + resA
			opB <- monedas(j) + resB
			
			Si opA > opB Entonces
				tabla(i,j) <- opA
			SiNo
				tabla(i,j) <- opB
			FinSi
			
		FinPara
	FinPara
	

	puntajeTu <- 0
	puntajePC <- 0
	izq <- 1
	der <- n
	continuar <- Verdadero
	
	Escribir "=============================="
	Escribir "   JUEGO DE MONEDAS"
	Escribir "=============================="
	
	Mientras izq <= der Y continuar Hacer
		

		Escribir ""
		Escribir "Monedas disponibles:"
		Para i <- izq Hasta der Con Paso 1 Hacer
			Escribir monedas(i), " "
		FinPara

		Escribir ""
		Escribir "--- TU TURNO ---"
		Escribir "Izquierda = ", monedas(izq), "  |  Derecha = ", monedas(der)
		
		eleccion <- ""
		Mientras eleccion <> "I" Y eleccion <> "i" Y eleccion <> "D" Y eleccion <> "d" Hacer
			Escribir "Elige (I)zquierda o (D)erecha: "
			Leer eleccion
			Si eleccion <> "I" Y eleccion <> "i" Y eleccion <> "D" Y eleccion <> "d" Entonces
				Escribir "Opcion invalida. Por favor elige I o D"
			FinSi
		FinMientras
		
		Si eleccion = "I" O eleccion = "i" Entonces
			Escribir "Tomaste: ", monedas(izq)
			puntajeTu <- puntajeTu + monedas(izq)
			izq <- izq + 1
		SiNo
			Escribir "Tomaste: ", monedas(der)
			puntajeTu <- puntajeTu + monedas(der)
			der <- der - 1
		FinSi
		
		Escribir "Tu puntaje: ", puntajeTu
		

		Si izq > der Entonces
			continuar <- Falso
		SiNo

			Escribir ""
			Escribir "--- TURNO PC ---"
			

			Si izq+1 <= der Entonces
				resA <- tabla(izq+1, der)
			SiNo
				resA <- 0
			FinSi
			

			Si izq <= der-1 Entonces
				resB <- tabla(izq, der-1)
			SiNo
				resB <- 0
			FinSi
			
			Si resA <= resB Entonces
				Escribir "PC toma izquierda: ", monedas(izq)
				puntajePC <- puntajePC + monedas(izq)
				izq <- izq + 1
			SiNo
				Escribir "PC toma derecha: ", monedas(der)
				puntajePC <- puntajePC + monedas(der)
				der <- der - 1
			FinSi
			
			Escribir "Puntaje PC: ", puntajePC
		FinSi
		
	FinMientras

	Escribir ""
	Escribir "=============================="
	Escribir "      RESULTADO FINAL"
	Escribir "=============================="
	Escribir "Tu puntaje : ", puntajeTu
	Escribir "Puntaje PC : ", puntajePC
	
	Si puntajeTu > puntajePC Entonces
		Escribir "GANASTE!"
	SiNo
		Si puntajeTu < puntajePC Entonces
			Escribir "LA PC GANO!"
		SiNo
			Escribir "EMPATE!"
		FinSi
	FinSi
	
FinAlgoritmo
