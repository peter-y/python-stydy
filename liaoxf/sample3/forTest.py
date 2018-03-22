from collections import Iterable

dict = {'a': 1, 'b': 2, 'c': 3}
for d in dict:
    print(d)
for d in dict.values():
    print(d)
for k, v in dict.items():
    print('key %s value %d' % (k, v))

for s in '中国人':
    print(s)

# 是否可迭代
print(isinstance('abc', Iterable))

for i, s in enumerate(['a', 'b', 'c']):
    print(i, s)

# enumerate 中 只要是 可迭代类型的就可以
for i, s in enumerate('abc'):
    print(i, s)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 生成一个最大最小数变量，循环比较list 中的所有值，把比较结果 暂存至变量
def findMinAndMax(L):
    if L == []:
        return None, None
    max = min = L[0]
    for m1 in L:
        if m1 > max:
            max = m1
    for m2 in L:
        if m2 < min:
            min = m2
    return (min, max)
