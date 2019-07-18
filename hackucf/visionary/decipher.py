#! /bin/python

table = []
with open("table.tsv") as in_file:
	for line in in_file:
		table.append(line.split(" "))

print len(table), len(table[0])
print table[0]