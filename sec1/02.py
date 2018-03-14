# coding: utf-8

patcar = u"パトカー"
taxi = u"タクシー"

concatList = []
for (a, b) in zip(patcar, taxi):
    concatList.append(a + b)

res = "".join(concatList)
print(res)