ky = vi = 0 

def jogo(k,v):
  global ky
  global vi
  if k.lower() == 'pedra' and v.lower() == 'papel': vi += 1
  elif k.lower() == 'pedra' and v.lower() == 'tesoura': ky += 1
  elif k.lower() == 'tesoura' and v.lower() == 'papel': ky += 1
  elif k.lower() == 'tesoura' and v.lower() == 'pedra': vi += 1
  elif k.lower() == 'papel' and v.lower() == 'tesoura': vi += 1
  elif k.lower() == 'papel' and v.lower() == 'pedra': ky += 1

n = int(input())
while n > 0:
  k = input()
  v = input()
  jogo(k,v)
  n -= 1

if ky > vi: print("VINICIUS VAI LAVAR A LOUÇA!")
elif vi > ky: print("KYARA VAI LAVAR A LOUÇA!")
else: print("OS DOIS VÃO LAVAR A LOUÇA JUNTOS!")