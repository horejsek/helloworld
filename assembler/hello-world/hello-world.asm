section .data
    hello:     db 'Hello world!',10 ; 10 is ascii code of new line.
    helloLen:  equ $-hello

section .text
    global start

start:
    MOV EAX,4               ; System call - write.
    MOV EBX,1               ; File desctiptor - standard output.
    MOV ECX,hello           ; Stuff for write.
    MOV EDX,helloLen        ; Length of 'stuff for write'.
    INT 80h                 ; Say to kernel: do this.

    MOV EAX,1               ; System call - sys_exit.
    MOV EBX,0               ; Return code.
    INT 80h
