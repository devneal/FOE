global _start

section .text
_start:
    ; print routine

    ; exit routine

section .data
    message: db "Hello, world!", 0x0a, 0x00
    mlen: equ $-message
