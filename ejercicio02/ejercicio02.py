#Consideramos n tareas t1, t2… tn sometidas a las restricciones anteriores. Es decir, hay que terminar algunas tareas antes de poder empezar otras. Así, por ejemplo, primero tenemos que preparar los cimientos de una casa antes de montar las paredes y los tabiques. En el ejercicio siguiente se propone calcular una ordenación de tareas sometidas a restricciones de prioridad.

#Ejercicio 5: Ordenación topológica

#Una restricción se expresa mediante un par (i,j) de números enteros comprendidos entre 1 y n, que indica que la tarea ti va antes que la tarea tj. Es decir, la tarea ti debe estar terminada antes de empezar la tarea tj. La relación binaria «... precede ...» así definida en el conjunto de las n tareas es una relación de orden parcial: algunas tareas no son comparables.

#1. Hacer un algoritmo que calcule una ordenación de la n tareas cumpliendo las restricciones.

#Está claro que no se pueden cumplir todas las restricciones. En este caso, no hay ordenación de las tareas. El algoritmo deberá tratar este caso correctamente.



def ordenacion_topologica(n, restricciones):
    # Inicializar diccionario de restricciones entrantes
    restr_ent = {i: 0 for i in range(1, n+1)}
    for i, j in restricciones:
        restr_ent[j] += 1
    cola = [i for i in range(1, n+1) if restr_ent[i] == 0]
    orden = []
    while cola:
        tarea = cola.pop(0)
        orden.append(tarea)
        for i, j in restricciones:
            if i == tarea:
                restr_ent[j] -= 1
                if restr_ent[j] == 0:
                    cola.append(j)
    if len(orden) < n:
        return None
    else:
        return orden
    

