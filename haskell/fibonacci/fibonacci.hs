fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)
fibonacci_line n = [fibonacci x | x <- [0..n-1]]
main = print (fibonacci_line 10)
