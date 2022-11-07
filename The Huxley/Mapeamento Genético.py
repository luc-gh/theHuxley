seq = input()
base = input()
v = ""
for c in seq:
  if c != base: v += " "
  else: v += c
if base not in v: print("ERRO")
else:
  print(seq.find(base*(len(max(v.split())))))
  print(len(max(v.split())))