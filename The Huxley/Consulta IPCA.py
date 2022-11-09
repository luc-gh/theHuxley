palavra = int(input())
d = {}

for _ in range(palavra):
    mes,n = input().split()
    d[mes] = float(n.replace(",","."))

while True:
    fr = input()
    if fr == "*": break
    if fr[0] == "M":
        mes,ano = fr.split()[1].split("/")
        nd = f"{ano}-" + (str(mes) if int(mes) >= 10 else f"0{mes}")
        if nd in d.keys(): 
            print(f"{d[nd]:.2f}")
        else: print("Dados indisponiveis para este periodo")
    else:
        mes,ano = [ int(i) for i in fr.split()[1].split("/")]
        r = int(fr.split()[2])
        t = 0
        cond = True
        for _ in range(r):
            nd = f"{ano}-" + (str(mes) if mes >= 10 else f"0{mes}")
            if nd not in d.keys(): 
                cond = False
                print("Dados indisponiveis para este periodo")
                break
            t += d[nd]
            mes += 1
            if mes > 12:
                mes = 1
                ano += 1
        if cond: print(f"{t:.2f}")