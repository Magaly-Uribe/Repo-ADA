#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int inicio, fin;
} Act;

int cmp(const void *a, const void *b) {
    return ((Act*)a)->fin - ((Act*)b)->fin;
}

void seleccionarActividades(Act act[], int n) {
    qsort(act, n, sizeof(Act), cmp);

    printf("Actividades seleccionadas:\n");
    int ultima = 0;
    printf("[%d, %d]\n", act[0].inicio, act[0].fin);

    for (int i = 1; i < n; i++) {
        if (act[i].inicio >= act[ultima].fin) {
            printf("[%d, %d]\n", act[i].inicio, act[i].fin);
            ultima = i;
        }
    }
}

int main() {
    Act act[] = {{1,4}, {3,5}, {0,6}, {5,7}, {8,9}, {5,9}};
    int n = 6;

    seleccionarActividades(act, n);
    return 0;
}
