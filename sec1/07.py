# coding: utf-8


def makeString(x, y, z):
    return "{0}時の{1}は{2}".format(x, y, z)


x = 12
y = "気温"
z = 22.4

print(makeString(x, y, z))