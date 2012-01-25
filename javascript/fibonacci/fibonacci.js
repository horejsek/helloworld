
function fibonacci(n) {
    if (n == 0 || n == 1) {
        return n;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

function fibonacciLine(n) {
    var list = new Array;
    for (var x = 0; x < n; x++) {
        list.push(fibonacci(x));
    }
    return list;
}

print(fibonacciLine(10));
