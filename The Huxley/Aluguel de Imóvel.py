tipo = input()
aluguel = int(input())
cabo = int(input())
net = int(input())
diaria = 150 if tipo == 'STANDARD' else 200
print('%.2f'%(aluguel*diaria + cabo*10 + net*15))