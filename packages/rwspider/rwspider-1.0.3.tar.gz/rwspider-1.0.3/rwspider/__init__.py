#!/usr/bin/env python
# encoding=utf-8

def get_ua():
    import requests
    url = "http://ruiwencloud.xyz/fake_ua"
    req = requests.get(url).text
    req = str(req)
    return req

def rw_ua():
    ua = get_ua()
    return ua

def print_ua():
    ua = get_ua()
    print(ua)


