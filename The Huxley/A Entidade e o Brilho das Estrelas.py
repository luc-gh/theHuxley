n = int(input())
valores = []
for i in range(n):
  valores.append(input())
for j in valores:
  um = dois = tres = quatro = cinco = seis = sete = oito = nove = 0
  for s in list(j): 
    if s == '1': um += 1
  for s in list(j): 
    if s == '2': dois += 1
  for s in list(j): 
    if s == '3': tres += 1
  for s in list(j): 
    if s == '4': quatro += 1
  for s in list(j): 
    if s == '5': cinco += 1
  for s in list(j): 
    if s == '6': seis += 1
  for s in list(j): 
    if s == '7': sete += 1
  for s in list(j): 
    if s == '8': oito += 1
  for s in list(j): 
    if s == '9': nove += 1
  print('Path %i:'%(valores.index(j)+1))
  print('    Brightness 1: %d'%(um))
  print('    Brightness 2: %d'%(dois))
  print('    Brightness 3: %d'%(tres))
  print('    Brightness 4: %d'%(quatro))
  print('    Brightness 5: %d'%(cinco))
  print('    Brightness 6: %d'%(seis))
  print('    Brightness 7: %d'%(sete))
  print('    Brightness 8: %d'%(oito))
  print('    Brightness 9: %d'%(nove))