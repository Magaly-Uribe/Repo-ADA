#include <stdio.h>

void cambio(int N) {
    int monedas[] = {25, 10, 5, 1};
    int cantidad[4] = {0};
    
    for (int i = 0; i < 4; i++) {
        cantidad[i] = N / monedas[i];
        N %= monedas[i];
    }

    printf("Cambio:\n");
    printf("25 -> %d\n10 -> %d\n5 -> %d\n1 -> %d\n",
           cantidad[0], cantidad[1], cantidad[2], cantidad[3]);
}

int main() {
    int N;
    printf("Ingresa N: ");
    scanf("%d", &N);
    cambio(N);
    return 0;
}
