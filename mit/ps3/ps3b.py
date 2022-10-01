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


def subStringMatchExact(target, key):
    if key == "":
        return ()
    indexList = []
    while key in target:
        indexList.append(str.find(target, key))
        replacement = ""
        for i in range(0, len(key)):
            replacement += chr(00)
        target = target.replace(key, replacement, 1)
    # print("asdf")
    return tuple(indexList)



# print(subStringMatchExact(key11, target2))
