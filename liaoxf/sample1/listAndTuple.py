# 说是list 像是数组和list结合
classname = ['33班', '32班', '31班']
print(classname)
print(classname[0])
classname.append('34班')
print(classname)
# 不存在就报错 ValueError: list.remove(x): x not in list
classname.remove('34班')
print(classname)
classname.insert(0, '34班')
print(classname)

# 删除末尾元素
classname.pop()
print(classname)

classname = ['37班', '36班', '35班', '34班', '33班', '32班', '31班']
print(classname)
classname.pop(1)
print(classname)

# 多维数组
arr1 = ['n1', 'n2']
arr2 = ['s1', 's2', arr1]
arr3 = ['o1', 'o2', arr2]
print(arr3)
print(arr3[1])
print(arr3[2][2][0])

# 有序列表 元祖 tuple 赋值后不可变 tuple 的不变 是表示指向不变
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
# list 中只有一个元素
daynum = ('z1',)
print(daynum)
# 可变 tuple
daynum = ('z1', 'z2', arr1)
print(daynum)
# arr1 重新赋值后 相关list 中的值并没有变化
arr1 = ['n10', 'n20', 'n30']
print(daynum)
# 这种赋值就能产生变化
daynum = ('z1', 'z2', arr1)
arr1[0] = 'm1'
print(daynum)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# -1 表示最后元素
print(L[0][0], L[1][1], L[-1][-1], sep='\n')
