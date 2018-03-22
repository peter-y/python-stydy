import math


# 方法名貌似是建议小写
def my_abs(x):
    # isinstance 可用于检查 类型
    if not isinstance(x, (int, float)):
        raise TypeError('错误的请求参数类型')
    print('this is my def function')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-19))


# 定义一个空方法
def my_function1():
    pass


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r1, r2 = move(100, 100, 60, math.pi / 6)
print(r1, r2)
# 多个值返回的时候 实际是返回一个 tuple 不可变元祖 按照位置赋值
print(move(100, 100, 60, math.pi / 6))


# 计算 次方 n=2 是默认参数 可不填写，不是2 的话 可传值
def power(x, n=2):
    s = 1
    while n > 1:
        n = n - 1
        s = s * x
    return s


print(power(10))
print(power(10, 3))


def enroll(name, gender, age=6, city='北京'):
    print('姓名 %s 性别 %s 年龄 %d 住址 %s' % (name, gender, age, city))


print(enroll('张小亮', '男'))
print(enroll('张一名', '男', city='上海'))
print(enroll('张一名', '男', 8))


def c_add(list=[]):
    list.append('end')
    return list


print(c_add(['大衣', '裤子', '衬衣']))
print(c_add(['手机', '钱包']))
# list本身是可变对象 参数l指向了[] 传默认值的时候 并不会改变这个指向本身 所以多次调用之后 l 会出现叠加的情况
print(c_add())
print(c_add())


# None 是不可变对象 参数一定要设置成不可变对象
def c_add2(l=None):
    if l is None:
        l = []
    l.append('end')
    return l


print(c_add2())
print(c_add2())


# 不定量 参数 内部接收是一个tuple
def calc(*num):
    sum = 0
    for n in num:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
nums = [1, 2, 3]
# 可以这么直接传数组
print(calc(*nums))


# 关键字参数 内容是一个dict
def person(name, age, **kwargs):
    # kwargs拿不到引用 是参数的复本
    print('person 姓名 %s 年龄 %d 其他信息 %s' % (name, age, kwargs))


person('周晓光', 24)
person('周晓光', 24, city='北京')
person('周晓光', 24, city='北京', job='销售')

extinfo = {'city': '北京', 'job': '销售', 'nickname': 'JOJO_zhou', 'des': '个人介绍'}
# 这样可以直接传个 dict
person('周晓光', 24, **extinfo)


# 命名关键字参数
def person2(name, age, *, city, job):
    # kwargs拿不到引用 是参数的复本
    print('person2 姓名 %s 年龄 %d 城市 %s 工作 %s' % (name, age, city, job))


# 命名参数 必须 写 key=value
person2('周晓光', 24, city='北京', job='销售')


def person3(name, age, *args, city, job):
    # kwargs拿不到引用 是参数的复本
    print('person2 姓名 %s 年龄 %d 城市 %s 工作 %s 其他 %s' % (name, age, city, job, args))


# 传单个值 会 输出 ('努力学习',)
person3('周晓光', 24, '努力学习', '天天向上', city='北京', job='销售')


def person4(name, age, *args, city='北京', job='销售'):
    # kwargs拿不到引用 是参数的复本
    print('person2 姓名 %s 年龄 %d 城市 %s 工作 %s 其他 %s' % (name, age, city, job, args))


person4('周晓光', 24, '努力学习', '天天向上')


# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f2(1, 2, 3, d=5, kw1='v1', kw2='v2')

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)