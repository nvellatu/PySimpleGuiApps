from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

# print(str.find(target2[5:],"atgc"))

def countSubStringMatch(target,key):
    counter = 0
    while key in target:
        counter+=1
        keyIndex = str.find(target, key)
        target = target[keyIndex+1:]
    return counter


def countSubStringMatchRecursive(target,key):
    counter = 0
    if key in target:
        keyIndex = str.find(target,key)
        counter+=1+countSubStringMatchRecursive(target[keyIndex+1:], key)
    return counter




print(countSubStringMatch("atgacatgcacaagtatgcat","atgc"))
print(countSubStringMatchRecursive("atgacatgcacaagtatgcat","atgc"))