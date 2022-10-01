from dill.source import getsource

list = []

for i in range(0, 5):
    list.append((i, lambda x: x*i))
    # print(list[i](2))
# print(list)
for i in range(0, 5):    # print(item(2))
    print(list[i][1](list[i][0]))
    # print()

for item in list:
    print((item[0]))