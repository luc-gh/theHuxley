frase = input()
a = e = i = o = u = 0
for c in frase:
  if c.lower() == 'a': a += 1
  elif c.lower() == 'e': e += 1
  elif c.lower() == 'i': i += 1
  elif c.lower() == 'o': o += 1
  elif c.lower() == 'u': u += 1
print('a %d'%a)
print('e %d'%e)
print('i %d'%i)
print('o %d'%o)
print('u %d'%u)
print('%.2f%%'%(((a+e+i+o+u)/len(frase))*100))