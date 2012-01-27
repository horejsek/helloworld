#include <stdio.h>
#include <stdlib.h>

int fibonacci(int n);
int* fibonacciLine(int n);

int main(void)
{
    int x, length = 10;
    int* res = fibonacciLine(length);
    for (x = 0; x < length; x++) {
        printf("%d\n", res[x]);
    }
    free(res);
    return 0;
}

int fibonacci(int n)
{
    if (n == 0 || n == 1) {
        return n;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

int* fibonacciLine(int n)
{
    int x;
    int* list = (int*)malloc(n*sizeof(int));
    for (x = 0; x < n; x++) {
        list[x] = fibonacci(x);
    }
    return list;
}
