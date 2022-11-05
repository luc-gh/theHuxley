r = float(input())
if r > 170.0:
  print(f'Colesterol total {r} mg/dl (ALTO)')
elif r < 150.0:
  print(f'Colesterol total {r} mg/dl (DESEJAVEL)')
else:
  print(f'Colesterol total {r} mg/dl (LIMITROFE)')