import random
import time

class Articulo:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
        self.ratio = valor / peso if peso > 0 else 0

def mochila_fraccionaria(capacidad, articulos):

    # Ordenar artículos por ratio valor/peso en orden descendente
    articulos_ordenados = sorted(articulos, key=lambda x: x.ratio, reverse=True)
    
    valor_total = 0.0
    peso_actual = 0.0
    
    for articulo in articulos_ordenados:
        if peso_actual + articulo.peso <= capacidad:
            # Tomar el artículo completo
            peso_actual += articulo.peso
            valor_total += articulo.valor
        else:
            # Tomar fracción del artículo
            peso_restante = capacidad - peso_actual
            fraccion = peso_restante / articulo.peso
            valor_total += articulo.valor * fraccion
            peso_actual = capacidad
            break
    
    return valor_total, peso_actual

def generar_articulos(n, seed=42):
    """Genera n artículos con pesos y valores aleatorios"""
    random.seed(seed)
    articulos = []
    for i in range(n):
        peso = random.uniform(1, 50)
        valor = random.uniform(10, 100)
        articulos.append(Articulo(peso, valor))
    return articulos

def ejecutar_pruebas():
    """Ejecuta pruebas con 10, 100 y 1000 artículos"""
    capacidades = [250, 2500, 25000]  # Capacidades proporcionales
    cantidades = [10, 100, 1000]
    
    for i, n in enumerate(cantidades):
        print(f"\nPRUEBA CON {n} ARTÍCULOS")
        
        # Generar artículos
        articulos = generar_articulos(n, seed=42+i)
        capacidad = capacidades[i]
        
        print(f"Capacidad de la mochila: {capacidad:.2f}")
        
        # Resolver el problema
        inicio = time.time()
        valor_optimo, peso_usado = mochila_fraccionaria(capacidad, articulos)
        tiempo = time.time() - inicio
        
        print(f"Valor máximo obtenido: {valor_optimo:.2f}")
        print(f"Peso utilizado: {peso_usado:.2f} / {capacidad:.2f}")
        print(f"Tiempo de ejecución: {tiempo*1000:.4f} ms")

if __name__ == "__main__":
    ejecutar_pruebas()
    
