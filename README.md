# REFE
Materials for the IAP 2018 Reverse Engineering for Exploitation course.

## TODO

* Restructure notes to match new schedule
* Laredo VMs / docker container for each student?
* More day 1 exercises and ROP exercises

## Schedule
1. Linux, ELF, and RE
    * LD_PRELOAD / LD_LIBRARY_PATH (?)
    * Assembly Primer (reading only)
        * Registers
        * cdecl
    * ELF Format
        * ELF-Walkthrough.png
        * readelf
        * objdump
        * nm
    * Reverse Engineering Tools
        * file
        * objdump
        * strings
        * strace, ltrace, xtrace
        * shellnoob
        * hex editor
    * GDB
        * break
        * run
        * continue
        * x
        * nexti
        * stepi
        * pwndbg / voltron
    * pwntools
        * u64/p64
        * process / remote
        * read / recvuntil / readline
        * send / sendline
        * interactive
        * gdb attach
    * crackmes
        * tut0-func (functions/basics)
        * crackme0x00a (strings/modification)
        * crackme0x05 (add password/debugging)
        * level1 crackme (xor password)
        * level2 crackme (self-modification + product password)
        * level3 crackme (anti-debugging + self-modification + sum password)
2. Fundamentals of PWN
    * Overwriting Local Variables
    * Overwriting the Return Address
    * Shellcoding + NOP sled (+ shellcode env var?)
    * Return-to-libc
3. DEP, ROP, and ASLR
    * Return-Oriented Programming
    * one_gadget
    * DEP
    * ASLR
4. Stack Canaries, GOT/PLT, RELRO, PIE
    * Stack Canaries
    * GOT/PLT Overwrite
    * RELRO
    * PIE
5. Miscellaneous
    * Half-day competition (1 challenge)
    * Talk by Andy Sellars (?)
