voroodi = input('expression:')
x, y, z = voroodi.split(" ")
xj = float(x)
zj = float(z)

if y=='+':
    print("{:.1f}".format(xj+zj))
elif y=='*':
    print("{:.1f}".format(xj*zj))
elif y=='/':
    print("{:.1f}".format(xj/zj))
elif y=='-':
    print("{:.1f}".format(xj-zj))
else:
    print('not valid')