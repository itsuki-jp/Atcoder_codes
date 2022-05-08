import random


def eval():
    res = 0
    return res


def playout():
    return


def monte( pos, d ):
    if d == DEPTH:
        return


DEPTH = 2
METHODS = 4
LIMIT = 10
data = dict()
data[0] = {"parent": 1, "total": 2, "visited": 3}
monte(0, 0)
print(data[0]["parent"])
while data[0]["visited"] < LIMIT:
    break
