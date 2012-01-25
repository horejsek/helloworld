
function fibonacci {
    if [ $1 -le 0 ] || [ $1 -le 1 ]; then
        return $1
    else
        fibonacci $(($1-1))
        local a=$?
        fibonacci $(($1-2))
        local b=$?
        return $(($a+$b))
    fi
}

function fibonacciLine {
    for i in $(seq 0 $(($1-1))); do
        fibonacci $i
        echo $?
    done
}

fibonacciLine 10
