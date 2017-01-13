#!/usr/bin/python

# cat | ./stringnum $(./stringnum_sol.py )
def to_num(s):
    assert len(s) == 4
    ret = 0
    for i in range(4):
        ret += ord(s[i]) * 256**i
    return str(ret)

str1 = "refe"
str2 = "_iz_"
str3 = "cool"

print to_num(str1) + " " + to_num(str2) + " " + to_num(str3)
