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

def busqueda_binaria_rec(lista, x, izq=0, der=None):
    if der is None:
        der = len(lista) - 1
    if izq > der:
        return -1
    mid = (izq + der) // 2
    if lista[mid] == x:
        return mid
    elif lista[mid] < x:
        return busqueda_binaria_rec(lista, x, mid + 1, der)
    else:
        return busqueda_binaria_rec(lista, x, izq, mid - 1)

medir_ejecucion(busqueda_binaria_rec, [1,3,5,7,9], 7)