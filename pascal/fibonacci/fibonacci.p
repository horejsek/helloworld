program Fibonacci;

type
    arrayOfInteger = array of integer;

function fibonacci(n: integer): integer;
begin
    if (n = 0) or (n = 1) then
        fibonacci := n
    else
        fibonacci := fibonacci(n-1) + fibonacci(n-2);
end;

function fibonacciLine(n: integer): arrayOfInteger;
var
    x: integer;
    list: arrayOfInteger;
begin
    SetLength(list, n);
    for x := 0 to n-1 do
        list[x] := fibonacci(x);
    fibonacciLine := list;
end;

var
    x, length: integer;
    res: arrayOfInteger;
begin
    length := 10;
    res := fibonacciLine(length);
    for x := 0 to length do
        writeln(res[x]);
end.
