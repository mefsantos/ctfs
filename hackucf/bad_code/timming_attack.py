!# /bin/python 

# http://ctf.hackucf.org:4000/bad_code/bad_code.php?passwd=1337


url    = 'https://httpbin.org/robots.txt'
result = wget(url, timeout=60)
#'User-agent: *\nDisallow: /deny\n'
result2 = wget(url, True, timeout=60)
result == file('robots.txt').read()
True