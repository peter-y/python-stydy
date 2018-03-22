# dict key value 键值对 相当于map
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Tracy'])
# 直接key 赋值
d['Tracy'] = 100
# 取不存在的key 会报异常
print(d['Tracy'])
# 检查key 是否存在
print('Tracy' in d)
# 或者给默认值
print(d.get('Tracy1', 0))
# 不存在的返回一个 None
print(d.get('Tracy1'))
# 删除key
d.pop('Tracy')
print(d)

# set 并不是一个有序集合 没有重复key
set1 = {1, 2, 3}
print(set1)
set1 = {1, 2, 3, 123, 123, 1, 2, 3, 4, 5, 6, 7, '1t', '2t'}
print(set1)
set1.add(10)
set1.remove(5)
print(set1)
set2 = {1001, 1002, 1, 1004, 1003}
# 两个 set 直接处理并集
print(set1 | set2)
# 交集
print(set1 & set2)

strArr = ['alone', 'yuan', 'simple']
# 数组 可变对象 方法的操作会直接影响 也就是在不改变指向的情况下 改变值
strArr.sort()
print(strArr)

# 字符串是不可变对象 还有number
a = 'abc'
print(a)
# 这个就是重新产生新的内容 并 生成新的指向
b = a.replace('a', 'A')
print(a)
print(b)
