#!/usr/bin/python
from pwn import *
import operator
import random

MOD = 1000000007

def welcome(conn):
    # pwnlib.tubes.remote.remote
    # pwnlib.util.packing
    conn.sendline("Welcome to the pwntools tutorial server!")
    remote_test(conn)
    packing_test(conn)
    packing_test(conn)
    conn.sendline("You're done")

def fail(conn):
    conn.sendline("lolnope")
    exit(1)

##################################
### pwnlib.tubes.remote.remote ###
##################################
def suffix(n):
    if 4 <= n % 100 <= 20:
        suff = "th"
    else:
        suff = {1:"st", 2:"nd", 3:"rd"}.get(n % 10,"th")
    return str(n) + suff

def remote_question(conn, prompt, ans):
    print ans
    conn.sendline(prompt)
    user_input = conn.readline()
    if int(user_input) != ans:
        fail(conn)

def remote_test(conn):
    primes = open("10000.txt").read().rstrip()
    conn.sendline("Answer my questions to proceed")
    conn.sendline("This might come in handy:")
    conn.sendline("https://primes.utm.edu/lists/small/10000.txt")

    primes = map(int, primes.split(','))

    # sum
    remote_question(conn, "What's the sum of the first 10000 prime numbers?", sum(primes))

    # product
    remote_question(conn, "What's the product of the first 10000 prime numbers (mod {})?".format(MOD),
             reduce(lambda x, y: (x * y) % MOD, primes))

    # index
    pos = random.randint(1, 10000)
    remote_question(conn, "What's the {} prime number?".format(suffix(pos)),
             primes[pos - 1])

    conn.sendline("Congratulations")

############################
### pwnlib.util.fiddling ###
############################
def random_hex_word():
    return "".join([hex(random.randint(0, 256))[2:].zfill(2) for _ in range(8)])

def random_data_word():
    return "".join([chr(random.randint(0, 256)) for _ in range(8)])

def packing_test(conn):
    conn.sendline("Send this hex back as data")
    hex_str = random_hex_word()
    conn.sendline(hex_str)
    user_input = conn.read(9).strip()
    if enhex(user_input) != hex_str:
        fail(conn)

    conn.sendline("Send this data back as hex")
    hex_str = random_data_word()
    conn.sendline(hex_str)
    user_input = conn.readline().strip()
    if unhex(user_input) != hex_str:
        fail(conn)

    conn.sendline("Send back the xor of these hex strings as data")
    hex1 = random_hex_word()
    hex2 = random_hex_word()
    conn.sendline(hex1)
    conn.sendline(hex2)
    user_input = conn.readline().strip()
    if user_input != xor(unhex(hex1), unhex(hex2)):
        fail(conn)

    conn.sendline("Congratulations")

###########################
### pwnlib.util.packing ###
###########################
def packing_test(conn):
    conn.sendline("Send this hex back as a 64-bit little-endian word")
    hex_str = random_hex_word()
    conn.sendline(hex_str)
    user_input = conn.readline().strip()
    if user_input != p64(int(hex_str, 16)):
        fail(conn)

    conn.sendline("Unpack this 64-bit little-endian word into hex")
    data_str = random_data_word()
    conn.sendline(data_str)
    user_input = conn.readline().strip()
    ans = hex(u64(data_str))[2:]
    if user_input != ans:
        fail(conn)

    conn.sendline("Congratulations")

s = server(8888, callback = welcome)
