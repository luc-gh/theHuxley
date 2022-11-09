d = dict()
while True:
    n = input()
    if n == "SAIR" or len(d.keys()) == 100: break
    else:
        c = int(input())
        m = input()
        d.update({c:(n,m)})
l = []
while True:
    x = int(input())
    if x == -1: break
    else: 
        l.append(x)
for i in l:
    if i in d.keys() and d[i][1] == "P":
        print(f'{d[i][0]}, seja bem-vindo(a)!')
    elif i in d.keys() and d[i][1] == "F":
        print(f'Não está esquecendo de algo, {d[i][0]}? Procure a recepção!')
    else:
        print("Seja bem-vindo(a)! Procure a recepção!")