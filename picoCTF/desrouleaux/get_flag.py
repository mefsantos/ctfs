#! /usr/bin/python

from pwn import *
import re
import yaml
import operator

host, port = "2018shell.picoctf.com", 63299

local = True
context.log_level="critical"

responses = ""


src_ips = dict()
dst_ips = dict()
hashes = dict()
timestamps = dict()

if not local:
	con = remote(host, port)

try:

	with open('incidents.json') as json_file:
		data = yaml.safe_load(json_file)
	md = dict(data)
	tickets = md["tickets"]
	

	for entry in tickets:
		# print entry, "\n\n"
		ticket_dict = dict(entry)
		# print ticket_dict

		for key in ticket_dict:
			if key == "src_ip":
				if ticket_dict[key] not in src_ips:
					src_ips[ticket_dict[key]] = 0
				else:
					src_ips[ticket_dict[key]]+= 1
			elif key == "dst_ip":
				if ticket_dict[key] not in dst_ips:
					dst_ips[ticket_dict[key]] = 0
				else:
					dst_ips[ticket_dict[key]]+= 1
			elif key == "timestamp":
				if ticket_dict[key] not in timestamps:
					timestamps[ticket_dict[key]] = 0
				else:
					timestamps[ticket_dict[key]]+= 1
			elif "hash" in key:
				if ticket_dict[key] not in hashes:
					hashes[ticket_dict[key]] = 0
				else:
					hashes[ticket_dict[key]]+= 1
			else:
				continue
	print "src ips: ", sorted(src_ips.items(), key=operator.itemgetter(1))
	print "dst ips: ", sorted(dst_ips.items(), key=operator.itemgetter(1))
	print "hashes : ", sorted(hashes.items(), key=operator.itemgetter(1))
	print "stamps : ", sorted(timestamps.items(), key=operator.itemgetter(1))

	# con.recvuntil("> ")
	# con.sendline("%"+str(i) +"$s")
	# resp = con.recv()
	# #print resp
	# if "picoCTF" in resp:
	# 	print re.findall(r"picoCTF{.*}", resp)[0]
	# 	break
except Exception as e:
	print e

if not local:
	con.close()

