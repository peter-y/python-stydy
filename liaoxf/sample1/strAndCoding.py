#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

print("中文字符编码")
# unicode 整数编码
num = ord('A')
num2 = ord('中')
print(num)
print(num2)
what = chr(num)
what2 = chr(num2)
print(what)
print(what2)
# 字节
x1 = b'abc'

# 字符转字节
encode1 = 'abc'.encode('ascii')
encode2 = '大家'.encode('utf-8')
print(encode1)
print(encode2)
# 字节转字符
print(x1.decode('ascii'))
# 字符长度
print(len('今天的天气'))
print(len('team is a very sneck'))

# 字符串格式化
print('亲爱的%s你好！你%s月的话费是%s，余额是%s' % ('张小亮', '5', '100', '54.9'))
print('亲爱的%s你好！你%d月的话费是%f，余额是%f' % ('张小亮', 6, 100.34, 60.00))
# .2f 表示精度控制
print('亲爱的%s你好！你%d月的话费是%.2f，余额是%.2f' % ('张小亮', 6, 100.34, 60.00))
# 四舍五入
print('亲爱的%s你好！你%d月的话费是%.2f，余额是%.2f' % ('张小亮', 6, 100.348, 60.008))
# %% 显示百分号
print('growth rate: %d %%' % 7)
