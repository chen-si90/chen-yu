#8
a=int(input())
b=int(input())
c=int(input())
print(f'{a:02}:{b:02}:{c:02}')
e=(23-a)*3600+(59-b)*60+(60-c)
print(f'距离午夜还剩余{e}秒')