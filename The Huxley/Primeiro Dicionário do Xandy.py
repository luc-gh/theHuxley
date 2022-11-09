def remover_especiais(palavra:str):
    s = palavra.replace(".","")
    t = s.replace(":","")
    u = t.replace('\"',"")
    v = u.replace("(","")
    w = v.replace("$","")
    x = w.replace("#","")
    y = x.replace("*","")
    z = y.replace(".","")
    return z

d = dict()
l = []
while True:
    c = input()
    if c == '-1': break
    else: 
        for i in c.split():
            l.append(i)
    for j in l:
        if remover_especiais(j).lower() not in d:
            d.update({remover_especiais(j).lower(): 1})
        else:
            d.update({remover_especiais(j).lower(): d[remover_especiais(j).lower()]+1})
    l.clear()
for i in sorted(d):
    print(f'{i} - {d[i]}')