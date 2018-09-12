# -*- coding: utf-8 -*-
import hashlib

def md5_encrypt(text):
    md5 = hashlib.md5()
    md5.update(text)
    result = md5.hexdigest()
    return result
if __name__ == '__main__':
    print md5_encrypt('123')