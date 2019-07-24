#! /bin/sh

# after cracking the substitution cipher and save in cleartext.txt
cat cleartext.txt | head -n 2 | tail -n 1 | cut -d "-" -f 2

