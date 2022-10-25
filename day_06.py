# Version:  0.1
# Author:   Rougga
# Time:     2022-10-22 17:45

"""
最大公约数函数模块
"""


def common_divisor(x, y):
    if x > y:
        (x, y) = (y, x)
    for fal in range(x, 0, -1):
        if x % fal == 0 and y % fal == 0:
            return fal


"""
最小公倍数函数模块
"""


def lcm(x, y):
    return x * y // common_divisor(x, y)


def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False


"""
a:全局作用域
b:嵌套作用域
c:局部作用域
"""


def foo():
    global a
    a = 0x01
    b = 'hello'
    print(a)

    def bar():
        nonlocal b
        b = 'world'
        c = 'bar'
        print(a)
        print(b)
        print(c)

    bar()
    print(b)


print('common_divisor Test:%d' % common_divisor(81, 27))
print('lcm Test:%d' % lcm(81, 27))
print('is_prime Test:%d' % is_prime(7))
a = 0x00
foo()
print(a)
