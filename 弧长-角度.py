# encoding: utf-8
import math
r=eval(raw_input('请输入您的半径:'))
l=eval(raw_input('请输入您的弧长毫米:'))
a=180*l
b=math.pi*r
c=a/b
print '您要的角度是', '%.2f'%c,'C'
