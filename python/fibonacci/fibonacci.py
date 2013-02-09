
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_line(n):
    return [fibonacci(x) for x in range(n)]

print fibonacci_line(10)
