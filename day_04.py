# Version:  0.1
# Author:   Rougga
# Time:     2022-10-19 18:35


from math import sqrt

print('-----------1:素数练习------------')

num = int(input('请输入素数:'))
end = int(sqrt(num))
is_prime = True
print('end :%f' % end)
print(type(is_prime))
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

print('-----------2:最大公因数最小公倍数练习------------')

x = int(input('x = '))
y = int(input('y = '))
# 如果x > y,值交换
if x > y:
    x, y = y, x
# x,y选出最小的做递减运算
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公因数:%d' % (x, y, factor))
        print('%d和%d的最小公倍数:%d' % (x, y, x * y // factor))
        break

print('-----------3:打印三角形图案------------')

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')  # 告诉print将默认的换行符使用end指定的替代
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
