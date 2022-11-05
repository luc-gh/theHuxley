def verifica(x: float) -> str:
  if x >= 0 and x <= 25:
    return "Intervalo [0,25]"
  elif x > 25 and x <= 50:
    return "Intervalo (25,50]"
  elif x > 50 and x <= 75:
    return "Intervalo (50,75]"
  elif x > 75 and x <= 100:
    return "Intervalo (75,100]"
  else:
    return "Fora de intervalo"

n = float(input())
print(verifica(n))