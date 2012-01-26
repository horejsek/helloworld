
public class Fibonacci
{
    public static void main(String[] args)
    {
        int length = 10;
        int[] res = fibonacciLine(length);

        for (int x = 0; x < length; x++) {
            System.out.println(res[x]);
        }
    }

    public static int fibonacci(int n)
    {
        if (n == 0 || n == 1) {
            return n;
        } else {
            return fibonacci(n-1) + fibonacci(n-2);
        }
    }

    public static int[] fibonacciLine(int n)
    {
        int[] list = new int[n];
        for (int x = 0; x < n; x++) {
            list[x] = fibonacci(x);
        }
        return list;
    }
}
