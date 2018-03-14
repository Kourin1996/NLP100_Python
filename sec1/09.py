# coding: utf-8
import random


def arrange(str):
    length = len(str)
    if length <= 4:
        return str
    else:
        prefix = str[0]
        radix = list(str[1:length-1])
        suffix = str[-1]
        random.shuffle(radix)
        return prefix + "".join(radix) + suffix


input = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = input.split(' ')

res = " ".join(list(map(arrange, words)))
print(res)