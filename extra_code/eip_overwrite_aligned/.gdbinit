define hook-stop
info registers
x/10i $pc
end

b main
r < input.txt
