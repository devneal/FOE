#!/bin/bash

if [[ $# -eq 0 ]]; then
    echo "Usage: ./extract_shellcode.sh <binary>"
    exit 0
fi

for i in $(objdump -d $1 -M intel |grep "^ " |cut -f2); do
    echo -n '\x'$i
done

echo
