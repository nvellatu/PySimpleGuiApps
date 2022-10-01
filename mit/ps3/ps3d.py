from string import *

from ps3b import subStringMatchExact
from ps3c import subStringMatchOneSub

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def subStringMatchExactlyOneSub(key, target):
    exacts = subStringMatchExact(target,key)
    # print(exacts)
    subs = subStringMatchOneSub(key, target)
    # print(subs)
    subs = [value for value in subs if value not in exacts]
    for exact in exacts:
        for value in subs:
            if value>=exact and value<exact+len(key):
                subs.remove(value)
    return tuple(subs)

print(subStringMatchExactlyOneSub(key12, target2))


