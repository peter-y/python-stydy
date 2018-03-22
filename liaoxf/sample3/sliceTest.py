L = ['中国', '美国', '泰国', '韩国', '法国']


def show(list=[]):
    for i in list:
        print(L[i])


show(range(3))

r = []
n = 3
for i in range(n):
    r.append(L[i])

print(r)

# 切片
# 0 1 2
print('L[0:3] %s ' % L[0:3])
print('L[1:3] %s ' % L[1:3])
print('L[:3] %s ' % L[:3])
# - 就是倒数
print('L[-1] %s ' % L[-1])
print('L[-3:-1] %s ' % L[-3:-1])
print('L[-3:0] %s ' % L[-3:-0])
print('L[-3:] %s ' % L[-3:])

# 0-99
list = list(range(100))
print(list[:20])
print(list[:20:2])
print(list[::5])
# 复制
list2 = list[:]

# tuple
print((0, 1, 2, 3, 4, 5)[:3])

print('zhang xiao guang'[:-5])


def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
