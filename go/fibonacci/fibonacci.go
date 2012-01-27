package main

import "fmt"

func main() {
    fmt.Println(fibonacciLine(10))
}

func fibonacci(n int) int {
    if n == 0 || n == 1 {
        return n
    }
    return fibonacci(n-1) + fibonacci(n-2)
}

func fibonacciLine(n int) []int {
    var list []int

    for x := 0; x < n; x++ {
        list = append(list, fibonacci(x))
    }

    return list
}
