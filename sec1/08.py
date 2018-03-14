#coding: utf-8


def mapper(c):
    if c.isalpha() and c.islower():
        return chr(219 - ord(c))
    else:
        return c


def chpher(str):
    return "".join(list(map(mapper, str)))


input = "The pen is mightier than the sword."

encrypted = chpher(input)
decrypted = chpher(encrypted)

print(input)
print(encrypted)
print(decrypted)
