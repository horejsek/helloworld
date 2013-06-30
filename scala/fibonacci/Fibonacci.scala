
object Fibonacci {
    def main(args: Array[String]) {
        for (x <- fibonacciLine(10)) {
            println(x)
        }
    }

    def fibonacciLine(n: Int): List[Int] = {
        return (0 to n-1).map(x => fibonacci(x)).toList
    }

    def fibonacci(n: Int): Int = {
        if (n == 0 || n == 1) return n
        else return fibonacci(n-1) + fibonacci(n-2)
    }
}

