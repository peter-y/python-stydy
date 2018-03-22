# 生成器 generator 以某种设定 依次按需要创建list中的内容，而不是一次创建完整的list 比如range

# <generator object <genexpr> at 0x0000000001E2B830> 这个貌似就是生成器
print(x for x in range(20))
# 生成器可指向一个变量
gen1 = (x for x in range(10))
# 这种方式 适用于list需要很长的时候
print(next(gen1))

# generator 是可迭代对象
for n in gen1:
    print(n)


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# a, b = b, a + b相当于 如下
# t是一个tuple
# t = (b, a + b)
# a = t[0]
# b = t[1]

fib(10)


# 函数中包含 yield 就不是普通函数 而是一个 generator
def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib_g(6))
# 遇到yield 的时候返回，下次从yield的地方继续 generator 循环的时候拿不到返回值 done 需要捕获异常才可以
for fg in fib_g(6):
    print(fg)


# 普通函数 能够return 结果，generator 不能
# 杨辉三角
def ygsj():
    L = [1]
    n = 0
    while n < 11:
        yield L
        L.append(0)
        print('before list value = %s ' % L)
        # 这儿是个重新赋值的动作
        L = [1] + [L[i - 1] + L[i] for i in range(1, len(L))]
        print('after list value = %s ' % L)
        n = n + 1


for ysj in ygsj():
    print(ysj)

L = [1, 2, 1, 0]
print(L)
L = [1] + [5, 12, 31, 80]
print(L)
