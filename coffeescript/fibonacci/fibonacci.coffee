
fibonacci = (n) ->
    if n in [0..1]
        n
    else
        fibonacci(n-1) + fibonacci(n-2)

fibonacciLine = (n) ->
    for x in [0...n]
        fibonacci(x)

print(fibonacciLine(10))
