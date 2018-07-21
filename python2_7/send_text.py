# !/usr/bin/env python
import urllib


def sendsms(to, message, myhash):
    params = urllib.urlencode({'to': to, 'message': message, 'hash': myhash})
    f = urllib.urlopen('http://www.smspi.co.uk/send/', params)
    return f.read(), f.code


resp, code = sendsms('0031627652529', 'Testing', '34d7baa8713936f8cbe8419d508f8257')
print
resp
