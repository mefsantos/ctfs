#! /bin/python

import requests as r
import math as m
import time
import re
import sys

DEBUG_PRINTS = False

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

# post 
url = "http://ctf.hackucf.org:4000/calc/calc.php"
post_param = "answer"
session_cookie = ".eJwVj8FqwzAQBX-l7NkHy21yMPTQktQksDIKcsPq5tZOZEmrQN3SSCH_Xvf4YGbg3aAfeIpQn_owjwVMA9TrtSggXuLnCPUNHj6gBuNQUKaK3MEaVlfZYDb6fweW-lzJrFKrdyu5QYH61WHTJdlsH7FSFVWdMNoy5pdSOsnk8LfVb4GyDejs4qsSm4NDPTjcBDZHY8n5J8q-pLz3rfZXqf3Sfp_I7RfeWtJnYXibDHclHSlhVoIYk2T1DPcCfubxK_a8HAAeT3Mfvy8z3P8A5PhPcA.EBEgvw.GXCGC2JYlu_ZprAQb1RQSPneAKE"
PHPSESSID = "f0c5766652d044436d5fc1b5e143c970"
cookies = {
"PHPSESSID": PHPSESSID,
"session": session_cookie
}

i=0
#while True:
while True:
	get_page = r.get(url = url, cookies=cookies)

	page_content = cleanhtml(str(get_page.content)).strip().split("\n")[0]
	expression = page_content.split("...")[-1].strip()
	result = int(m.floor(float(eval(expression))))
	resp = r.post(url, data={post_param: str(result)}, cookies=cookies)

	clean_response = cleanhtml(str(resp.content)).lower()
	if "flag" in clean_response:
		res = re.search(r'flag{.*}', clean_response)
		if res:
			print res.group()
		break
	else:
		if DEBUG_PRINTS:
			print clean_response
		
	i += 1

