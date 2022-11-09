s = input()
c = s.replace(' ', '')
m = c.upper()
i = m[::-1]
cond = 0
for j in zip(i,m): 
  if j[0] != j[1]:
    cond = 0
    break
  else: cond = 1
if cond == 1: print('SIM')
else: print('NAO')