# coding: utf-8


def makeNGram(n, seq):
    return [seq[i:i+n] for i in range(len(seq)-n+1)]


str1 = "paraparaparadise"
str2 = "paragraph"

X = set(makeNGram(2, str1))
Y = set(makeNGram(2, str2))

unionXY = X.union(Y)
insecXY = X.intersection(Y)
diffXY = X.difference(Y)

print("X: ", X)
print("Y: ", Y)

print(unionXY)
print(insecXY)
print(diffXY)

if "se" in X:
    print("se is inclued in X")
else:
    print("se is not included in X")

if "se" in Y:
    print("se is inclued in Y")
else:
    print("se is not included in Y")