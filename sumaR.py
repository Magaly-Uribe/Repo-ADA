def suma_digitos_rec(n): #Recibe un numero
    if n == 0: #Si n vale 0 retorna 0
        return 0
    return n % 10 + suma_digitos_rec(n // 10) #Si no da el modulo 10 del numero y le suma la función recursiva con argumento de la división entera

print(suma_digitos_rec(123)) #Imprime el numero
