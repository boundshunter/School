#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import shelve
sh = shelve.open('aaa.conf')
sh['a'] = 'a'
sh['c'] = [11, 234, 'a']
sh['t'] = ('1', '2', '3')
sh['d'] = {'a':'2', 'name':'Hongte' }
sh['b'] = 'b'
sh['i'] = 23


print(sh['a'])

# del sh['a']
print(sh['a'])
for item in sh.items():
    # print(item,item[0])
    print("键{%s} = 值{%s}" % (item[0], sh[item[0]]))
    # print("键{} = 值{}".format(item[0],sh[item[0]])) # 格式化输出，.format 可以去除结果中的{}
sh.close()
