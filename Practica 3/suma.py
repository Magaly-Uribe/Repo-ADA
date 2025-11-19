import time
import psutil
import os

def obtener_uso_memoria_mb():
    proceso = psutil.Process(os.getpid())
    return proceso.memory_info().rss / (1024 * 1024)

def medir_ejecucion(func, *args, **kwargs):
    mem_inicio = obtener_uso_memoria_mb()
    tiempo_inicio = time.perf_counter()
    resultado = func(*args, **kwargs)
    tiempo_fin = time.perf_counter()
    mem_fin = obtener_uso_memoria_mb()
    
    print(f"Resultado: {resultado}")
    print(f"Tiempo (segundos): {tiempo_fin - tiempo_inicio:.6f}")
    print(f"Uso de Memoria (MB): {mem_fin:.4f}")
    return resultado

def suma_digitos_iter(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma

medir_ejecucion(suma_digitos_iter, 888)
