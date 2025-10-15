def invertir_iter(cadena): #Mandamos una cadena
    invertida = "" #Declara una cadena vacia
    for c in cadena: #Itera cada elemento de la cadena
        invertida = c + invertida #Concatena ambas cadenas poniendo primero c
    return invertida #Retorna invertida

print(invertir_iter("perro"))
