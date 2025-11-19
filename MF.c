#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
    double peso;
    double valor;
    double ratio;
} Articulo;

// Función de comparación para qsort (orden descendente por ratio)
int comparar_ratio(const void *a, const void *b) {
    Articulo *art1 = (Articulo *)a;
    Articulo *art2 = (Articulo *)b;
    
    if (art2->ratio > art1->ratio) return 1;
    if (art2->ratio < art1->ratio) return -1;
    return 0;
}

// Genera número aleatorio entre min y max
double random_double(double min, double max) {
    return min + (max - min) * ((double)rand() / RAND_MAX);
}

// Genera n artículos con valores aleatorios
void generar_articulos(Articulo *articulos, int n) {
    for (int i = 0; i < n; i++) {
        articulos[i].peso = random_double(1.0, 50.0);
        articulos[i].valor = random_double(10.0, 100.0);
        articulos[i].ratio = articulos[i].valor / articulos[i].peso;
    }
}

// Resuelve el problema de la mochila fraccionaria
double mochila_fraccionaria(double capacidad, Articulo *articulos, int n, double *peso_usado) {
    // Ordenar artículos por ratio valor/peso (descendente)
    qsort(articulos, n, sizeof(Articulo), comparar_ratio);
    
    double valor_total = 0.0;
    *peso_usado = 0.0;
    
    for (int i = 0; i < n; i++) {
        if (*peso_usado + articulos[i].peso <= capacidad) {
            // Tomar el artículo completo
            *peso_usado += articulos[i].peso;
            valor_total += articulos[i].valor;
        } else {
            // Tomar fracción del artículo
            double peso_restante = capacidad - *peso_usado;
            double fraccion = peso_restante / articulos[i].peso;
            valor_total += articulos[i].valor * fraccion;
            *peso_usado = capacidad;
            break;
        }
    }
    
    return valor_total;
}

void ejecutar_prueba(int n, double capacidad, int seed) {
    printf("\nPRUEBA CON %d ARTICULOS\n", n);
    
    // Asignar memoria para artículos
    Articulo *articulos = (Articulo *)malloc(n * sizeof(Articulo));
    if (articulos == NULL) {
        printf("Error: No se pudo asignar memoria\n");
        return;
    }
    
    // Generar artículos
    srand(seed);
    generar_articulos(articulos, n);
    
    printf("Capacidad de la mochila: %.2f\n", capacidad);
    
    
    // Resolver el problema y medir tiempo
    clock_t inicio = clock();
    double peso_usado;
    double valor_optimo = mochila_fraccionaria(capacidad, articulos, n, &peso_usado);
    clock_t fin = clock();
    
    double tiempo_ms = ((double)(fin - inicio) / CLOCKS_PER_SEC) * 1000.0;
    
    
    printf("Valor máximo obtenido: %.2f\n", valor_optimo);
    printf("Peso utilizado: %.2f / %.2f\n", peso_usado, capacidad);
    printf("Tiempo de ejecución: %.4f ms\n", tiempo_ms);
    
    free(articulos);
}

int main() {

    // Pruebas con diferentes cantidades de artículos
    ejecutar_prueba(10, 250.0, 42);
    ejecutar_prueba(100, 2500.0, 43);
    ejecutar_prueba(1000, 25000.0, 44);
    
    return 0;
}
