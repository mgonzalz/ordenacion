#Consideramos n tareas t1, t2… tn sometidas a las restricciones anteriores. Es decir, hay que terminar algunas tareas antes de poder empezar otras. Así, por ejemplo, primero tenemos que preparar los cimientos de una casa antes de montar las paredes y los tabiques. En el ejercicio siguiente se propone calcular una ordenación de tareas sometidas a restricciones de prioridad.

#Ejercicio 5: Ordenación topológica

#Una restricción se expresa mediante un par (i,j) de números enteros comprendidos entre 1 y n, que indica que la tarea ti va antes que la tarea tj. Es decir, la tarea ti debe estar terminada antes de empezar la tarea tj. La relación binaria «... precede ...» así definida en el conjunto de las n tareas es una relación de orden parcial: algunas tareas no son comparables.

#1. Hacer un algoritmo que calcule una ordenación de la n tareas cumpliendo las restricciones.

#Está claro que no se pueden cumplir todas las restricciones. En este caso, no hay ordenación de las tareas. El algoritmo deberá tratar este caso correctamente.

n = int(input("Introduce el número de tareas: "))
restricciones = []
for i in range(n):
    restricciones.append([])
for i in range(n):
    for j in range(n):
        if i != j:
            print("¿La tarea", i+1, "precede a la tarea", j+1, "?")
            if input() == "si":
                restricciones[i].append(j)
print(restricciones)


