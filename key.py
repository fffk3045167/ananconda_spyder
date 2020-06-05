# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:45:29 2020

@author: Administrator
"""

import string
import random

key_len = 10
key_all = 20

def base_str():
    return (string.ascii_letters + string.digits)

def base_str1():
    return string.printable

def key_gen():
    keylist = [random.choice(base_str()) for i in range(key_len)]
    return ("".join(keylist))

if __name__ == "__main__":
    print(key_gen())