
<< Region_Completa >>


Orden de compilación

	
1. Estructura_Vecinos.py
	Genera la estructura de vecinos de la matriz de sitios de 192x202
	output:
		Estructura_Vecinos.csv

2. Generacion_Vecinos.py
	Genera la estructura de vecinos por generación
	input:
		Matriz_Datos_Iniciales.csv
	output:
		Generacion_Vecinos.csv
		Matriz_Generacion_Vecinos.csv

3. Elevacion_Relativa.py
	Genera la elevación relativa al rio de cada centroide
	input:
		Generacion_Vecinos.csv
		Centroides-Elevacion_QGIS.csv
		Estructura_Vecinos.csv
	output:
		elev.npy
		Elevacion_Relativa.csv





