# coding: utf-8

input = u"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
fstNums = {1, 5, 6, 7, 8, 9, 15, 16, 19}
words = input.split(' ')
res = {}
for (i, s) in enumerate(words):
    if (i+1) in fstNums:
        sub = s[:1]
    else:
        sub = s[:2]
    res[sub] = (i+1)
print(res)  

