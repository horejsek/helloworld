
fibonacci := [:n |
    ((n == 0) | (n == 1)) ifTrue: [
        n.
    ] ifFalse: [ | a b |
        a := fibonacci value:n-1.
        b := fibonacci value:n-2.
        a+b.
    ].
].

fibonacciLine := [:n |
    list := Array new: n.

    1 to: n do: [:x | | a |
        a := fibonacci value:x-1.
        list at: x put: a.
    ].

    list.
].

length := 10.
res := fibonacciLine value:length.
1 to: length do: [:x |
    (res at: x) printNl.
].
