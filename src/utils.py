# -*- coding: utf-8 -*-

# print format vector to string
def sprint(vector):
    return '[' + ', '.join('%1.3f' % v for v in vector) + ']'

# print format vector to stdout
def pprint(vector):
    print('[' + ', '.join('%1.3f' % v for v in vector) + ']')
    return
