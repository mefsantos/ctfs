import subprocess as sp
import string as s
import re

chars = s.printable
# remove " to avoid closing the string 
chars = s.ascii_letters+s.digits+"-_"
base_flag = "CSCPT{"
tail_flag = "}"
lflag = list(base_flag)
lflag.extend("A" * (21 - len(base_flag) - len(tail_flag)))
lflag.append("}")
#['C', 'S', 'C', 'P', 'T', '{', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '}']
ix_to_change = 6
flag_to_test = lflag[:]
while ix_to_change in range(ix_to_change, len(lflag)-1):
	for c in chars:
		flag_to_test[ix_to_change] = c
		command = "./running " + "".join(flag_to_test)
		print("Command: %s" % command)
		proc = sp.Popen([""+command], stdout=sp.PIPE, shell=True)
		(out, err) = proc.communicate()
		if err:
			print("Error running the process. Exiting...")
			exit(1)
		mile_ran = map(int, re.findall(r'\d+', out))
		print(mile_ran)
		if len(mile_ran) <= 0:
			print("No Miles obtained... Actual message:\n%s" % out)
			exit(1)
		mile_ran = mile_ran[-1]
		if mile_ran > ix_to_change:
			print("found char (%s) at index (%d)" % (c, ix_to_change))
			ix_to_change = mile_ran
			break

print("Computation ended")
print("Flag: %s" % "".join(flag_to_test))
print("Done.")
