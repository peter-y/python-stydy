print(1 + 2 + 3 + 4)
classnames = ['11班', '12班', '13班']
for classname in classnames:
    print(classname)

# 生成 0-9 总数10 的序列
print(list(range(10)))
sum = 0
allnum = list(range(11))
for num in allnum:
    sum = sum + num
print(sum)

whilesum = 0
# 循环99次
whilenum = 99
while whilenum > 0:
    whilesum = whilesum + whilenum
    whilenum = whilenum - 1
    print('sum %s num %s ' % (whilesum, whilenum))
print('有限次数 while 循环结束')
whilesum = 0
# 循环99次 并使用 break 中断本次的以及后面的循环
whilenum = 99
while whilenum > 0:
    if whilenum == 40:
        print('while break循环结束')
        break
    whilesum = whilesum + whilenum
    whilenum = whilenum - 1
    print('sum %s num %s ' % (whilesum, whilenum))

# continue 跳过本次循环 继续执行后面的循环
whilenum = 0
while whilenum < 100:
    whilenum = whilenum + 1
    if whilenum % 2 == 0:
        continue
    print(whilenum)
print('while continue 循环结束')

classnames = ['11班', '12班', '13班']
n = 1
m = 0
while n == 1:
    m = m + n
    print(classnames[m % 3])
