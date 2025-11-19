def actividad_seleccion(actividades):
    # actividades = [(inicio, fin)]
    actividades.sort(key=lambda x: x[1])

    seleccionadas = [actividades[0]]
    fin_actual = actividades[0][1]

    for inicio, fin in actividades[1:]:
        if inicio >= fin_actual:
            seleccionadas.append((inicio, fin))
            fin_actual = fin
    
    return seleccionadas

# Ejemplo
actividades = [(1,4),(3,5),(0,6),(5,7),(8,9),(5,9)]
print(actividad_seleccion(actividades))
