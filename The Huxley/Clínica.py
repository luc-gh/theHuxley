l = []
def op1():
    print("Digite codigo do medico:")
    c = input()
    print("Digite o nome do medico:")
    n = input()
    print(f'Codigo: {c} | Medico: {n}')
def op2():
    global l
    print("Digite o codigo da consulta:")
    c = input()
    print("Digite o dia da semana:")
    d = input()
    print("Digite a hora:")
    h = input()
    print("Digite o codigo do medico:")
    m = input()
    if [c,d,h,m] in l: 
        print("Horario n�o disponivel.")
        op2()
    else:
        l.append([c,d,h,m])
        print(f'Codigo: {c} | Semana: {d} | Hora: {h} | Cod. Medico: {m}')
def op3():
    global l
    print("Digite o codigo da consulta:")
    cod = input()
    for i in l:
        if i[0] == cod:
            print(f'Codigo: {i[0]} | Semana: {i[1]} | Hora: {i[2]} | Cod. Medico: {i[3]}')
while True:
    print("Digite a opcao desejada:\n1- Cadastrar m�dico.\n2- Cadastrar consulta.\n3- Pesquisar consulta.\n0- Sair do programa.")
    x = input()
    if x == "0": break
    else:
        if x == '1': op1()
        elif x == '2': op2()
        elif x == '3': op3()
        else: 
            print('Opcao invalida.')