# coding: utf-8


def makeNGram(n, seq):
    return [seq[i:i+n] for i in range(len(seq)-n+1)]


input = "I am an NLPer"
words = input.split(' ')

wordBiGram = makeNGram(2, words)
charBiGram = makeNGram(2, input)

print(wordBiGram)
print(charBiGram)
