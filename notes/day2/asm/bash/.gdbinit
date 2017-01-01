define hook-stop
info registers
x/5i $pc
x/12xw $sp
end

b _start
r
