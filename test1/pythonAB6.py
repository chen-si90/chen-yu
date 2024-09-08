#6
import math
pi=math.pi
ab=eval(input())
cd=eval(input())

ad=ab/2

oa=(ad**2+cd**2)/(2*cd)
aob=2*math.asin(ad/oa)

sector=(aob/(2*pi))*pi*oa**2
if ab>cd:
    triangle=1/2*ab*(oa-cd)
else:
    triangle=1/2*ab*(cd-oa)

arch=sector-triangle
print(f'{arch:.2f}')
