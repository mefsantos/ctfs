#! /bin/bash

# after saving the cleartext in a file (website in the solution.txt):
cat cleartext.txt | grep -oE "picoCTF{.*}" --color=none

