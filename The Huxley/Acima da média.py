x = float(input())
y = float(input())
z = float(input())
ma = (x + y + z) / 3
l = [x,y,z]
c = 0
for i in l:
  if i > ma:
    c += 1
print(c) 