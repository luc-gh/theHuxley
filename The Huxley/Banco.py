contas = []
quantContas = 0
x = 0
def menu():
  global x
  print('Digite a opcao desejada:')
  print('1- Cadastrar cliente e conta.')
  print('2- Mostrar todas as contas cadastradas.')
  print('3- Mostrar contas de determinado cliente.')
  print('4- Mostre o ativo bancario.')
  print('5- Atualizar saldo.')
  print('0- Sair do programa.')
  op = int(input())
  
  if op == 0: x = 1
  elif op == 1: op1()
  elif op == 2: op2()
  elif op == 3: op3()
  elif op == 4: op4()
  elif op == 5: op5()


def op1():
  global quantContas
  global contas
  quantContas += 1
  nome = input('Digite o nome do cliente:')
  print()
  saldo = float(input('Digite o saldo:'))
  print()
  contas.append({'Conta': quantContas, 'Cliente': nome, 'Saldo': saldo})
  print('Conta: %d | Cliente: %s | Saldo: R$ %.2f'%(contas[quantContas-1]['Conta'], contas[quantContas-1]['Cliente'], contas[quantContas-1]['Saldo']))

def op2():
  global quantContas 
  global contas
  for i in range(quantContas):
    print('Conta: %d | Cliente: %s | Saldo: R$ %.2f'%(contas[i]['Conta'], contas[i]['Cliente'], contas[i]['Saldo']))

def op3():
  global quantContas
  global contas
  con = input('Digite o nome do cliente:')
  print()
  for i in contas:
    if i['Cliente'] == con:
      print('Conta: %d | Cliente: %s | Saldo: R$ %.2f'%(i['Conta']-1, i['Cliente'], i['Saldo']))

def op4():
  global contas
  ativo = 0.0
  for i in range(len(contas)):
    ativo += contas[i]['Saldo']
  print('Ativo Bancario: R$ %.2f'%ativo)

def op5():
  global contas
  conta = int(input('Digite o numero da conta:'))
  print()
  novoSaldo = float(input('Digite o novo saldo:'))
  print()
  contas[conta-1].update({'Saldo': novoSaldo})

while x == 0: menu()