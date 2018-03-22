from collections import Iterable
from collections import Iterator

# Iterable 类型的 都可作用于 for 循环
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('', Iterable))
print(isinstance((x for x in range(1, 10)), Iterable))
print(isinstance(100, Iterable))
print('割了-------------------------------------------')
# Iterator 类型的 都是 迭代器 生成器都是Iterator类型
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('', Iterator))
print(isinstance((x for x in range(1, 10)), Iterator))
print(isinstance(100, Iterator))

# Iterable 转 Iterator
# Iterator表示一个流，事先不能确定长度
print(isinstance(iter([]), Iterator))
