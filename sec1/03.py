# coding: utf-8

input = u"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = input.split(' ')
counts = list(map((lambda s: len(s) - s.count(',') - s.count('.')), words))

print(counts)