"""
试编程实现分两行输入两个非零整数，并在4 行中按顺序输出两个数的加、减、乘、除的计算结果。
要求输出与如下示例格式相同，符号前后各有一个空格。
"""

#输入整数变量a和b，定义输入函数
##############Begin##################
a = int(input())
b = int(input())
##############End####################

#a和b之间进行四则运算并输出
##############Begin##################
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')


##############End####################