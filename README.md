# FOE
Materials for the IAP 2018 Fundamentals of Exploitation course.

## Schedule
1. Understanding the Playing Field
    * data representations - binary, hexadecimal, 2's complement, endianness
    * computer model - cpu, memory, registers, compilers, linkers
    * x86 architecture - x86, x86-64, assembly, stack, heap, memory layout
    * examining binaries - strings, readelf, objdump, symbols, sections, segments, got, plt
    * gdb - help, disassemble, break, run, x, display, etc.
2. Tools of the Trade, Memory Corruption, Shellcoding
    * pwntools - tubes, ssh, process, util, enhex, unhex, p64, u64
    * pwndbg - context, nearpc, stack, display (db, dw, dd, dq, ds, dps), break (bp, bd, be, bc, bl)
    * memory corruption - overwriting variables, overwriting return address, shellcode exploit
3. DEP, ROP, and ret2libc
    * mitigations - DEP/NX, ASLR, canaries, (full) relro, PIC/PIE, fortify source
    * dep, ret2libc, x86 vs x86-64, ret2libc_32
    * execve(), (srop)
    * aslr, rop given leak
4. Canaries, GOT+PLT
    * a word on reverse engineering, finding main()
    * got/plt, rop without leak
    * canaries, canary leak
5. Competition
