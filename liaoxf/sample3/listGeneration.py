import os

l = []
for x in list(range(1, 11)):
    l.append(x * x)

print(l)

# 列表生成式
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([s + n for s in 'ABC' for n in 'FGH'])
# 获取当前目录下的文件名
print([d for d in os.listdir('.')])

di = {'x': 'A', 'y': 'B', 'z': 'C'}
print(['key ' + k + ' value ' + v for k, v in di.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])
