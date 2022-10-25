# Version:  0.1
# Author:   Rougga
# Time:     2022-10-20 19:06

import math

print('-----------1、水仙花数--------------')

for i in range(100, 1000):
    low = i % 10
    mid = i // 10 % 10
    high = i // 100
    if i == low ** 3 + mid ** 3 + high ** 3:
        print('水仙花:%d' % i)

num = int(input('num ='))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num * 10 + num % 10
    num //= 10
print('reverse_num:%d' % reverse_num)

'''
**说明**：斐波那契数列（Fibonacci sequence），又称黄金分割数列，是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）
在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，
所以这个数列也被戏称为&quot;兔子数列&quot;。斐波那契数列的特点是数列的前两个数都是1，
从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用
'''

print('-----------2、斐波那契数列--------------')

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
'''
**说明**：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。
'''

print('\n-----------3、10000以内完美数--------------')

sums = 0
for _ in range(1, 10000):
    for _in in range(1, _):
        if _ % _in == 0:
            sums += _in
            # if _in > 1:
            #     sums += _in
    if sums == _:
        print('完美数:%d' % _)
    sums = 0

for num in range(2, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if 1 < factor != num // factor:
                result += num // factor
    if result == num:
        print(num)
