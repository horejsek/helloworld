<?php

function fibonacci($n) {
    if ($n == 0 || $n == 1) {
        return $n;
    } else {
        return fibonacci($n-1) + fibonacci($n-2);
    }
}

function fibonacciLine($n) {
    $list = array();
    for ($x = 0; $x < $n; $x++) {
        $list[] = fibonacci($x);
    }
    return $list;
}

foreach (fibonacciLine(10) as $value) {
    echo $value . "\n";
}

