
main () {
    print(fibonacciLine(10));
}

num fibonacci(num n) {
    if (n == 0 || n == 1) {
        return n;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

List fibonacciLine(num n) {
    var list = new List(n);
    for (var x = 0; x < n; x++) {
        list[x] = fibonacci(x);
    }
    return list;
}

