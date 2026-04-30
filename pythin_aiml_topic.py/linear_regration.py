import numpy as np
x=[1,2,3,4]
y=[2,4,6,8]
cx =0
cy =0
cx2 = 0
cxy =0
n=len(x)
for i in range(n):
    cx += x[i]
    cy += y[i]
    cx2 += x[i]*x[i]
    cxy += x[i]*y[i]
b = (n * cxy- cx * cy) / (n * cx2 - cx * cx)
a= cy -b *cx
print(f"a={a}")
print(f"b={b}")