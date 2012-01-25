#include <iostream>

using namespace std;

int fibonacci(int n);
int* fibonacciLine(int n);

int main(void)
{
    int length = 10;
    int* res = fibonacciLine(length);
    for (int x = 0; x < length; x++) {
        cout << res[x] << endl;
    }
    delete [] res;
    return 0;
}

int fibonacci(int n) {
    if (n == 0 || n == 1) {
        return n;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

int* fibonacciLine(int n) {
    int* list = new int[n];
    for (int x = 0; x < n; x++) {
        list[x] = fibonacci(x);
    }
    return list;
}
