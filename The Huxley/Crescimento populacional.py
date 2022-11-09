popi = int(input())
anoi = int(input())
q = float(input())
anof = int(input())
fator = 1 + q/100
for i in range(anof-anoi+1):
  print(f'{i+anoi} {int(popi * fator ** i)}')