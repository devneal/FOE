# REFE
Materials for the IAP 2018 Reverse Engineering for Exploitation course.

## Schedule
1. Language of Linux
    * C Primer
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
        * voltron
2. Various crackmes
    * crackmes
        * tut0-func (functions/basics)
        * crackme0x00a (strings/modification)
        * crackme0x05 (add password/debugging)
        * level1 crackme (xor password)
        * level2 crackme (self-modification + product password)
        * level3 crackme (anti-debugging + self-modification + sum password)
    * Programming in Assembly
        * exit
        * helloworld
        * oneko (if we have time)
        * bash shell
3. Exploitation I
    * Overwriting Local Variables
    * Overwriting the Return Address
    * Shellcoding + NOP sled (+ shellcode env var?)
    * Return-to-libc
    * Return-Oriented Programming
4. Exploitation II
    * Format String Corruption
    * Format String GOT/PLT Overwrite
    * Heap Vulnerabilities
    * Mitigation Techniques
5. Competition / Talk
    * Half-day competition (1 challenge)
    * Talk by Andy Sellars (?)
