# 递归函数 。。。完全不懂公式
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# 进入方法压栈 退出方法 出栈
print(fact(5))


# 函数调用 通过栈stack来完成 循环层级过多 会造成栈溢出 RecursionError: maximum recursion depth exceeded in comparison
# 函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧


# 什么尾递归优化... 据说这样就不压栈帧 艹 说什么没做优化 不支持。。。
def fact_n(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 汉诺塔移动。。。抄的
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)  # 把a上的n-1块移动到b
        move(1, a, b, c)  # 把a上的最后一块移动到c
        move(n - 1, b, a, c)  # 把b上的n-1块移动到c


print(move(3, 'A', 'B', 'C'))
