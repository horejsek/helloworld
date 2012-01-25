
def fibonacci(n)
    if n == 0 or n == 1
        return n
    else
        return fibonacci(n-1) + fibonacci(n-2)
    end
end

def fibonacciLine(n)
    list = Array.new
    for i in (0..n)
        list << fibonacci(i)
    end
    return list
end

puts fibonacciLine(10)
