def invertir_rec(cadena): #Mandamos una cadena
    print("%s",cadena)
    if len(cadena) == 0: #Verifica que no este vacia o retorna 0
        return cadena 
    return cadena[-1] + invertir_rec(cadena[:-1]) #Hace la llamada recursiba para comenzar de nuevo

print(invertir_rec("hola")) #Imprime
