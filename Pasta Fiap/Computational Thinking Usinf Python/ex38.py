a = 0
b = 1
f = a+b
for i in range(1,31,1):
   b = a
   a = f
   f = a+b