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

def potencia_iter(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

medir_ejecucion(potencia_iter, 2, 5)
