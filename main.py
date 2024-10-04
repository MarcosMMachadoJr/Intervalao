'''
Beecrowd: Problema 1037
06/02/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''
codigo,quantidade=input().split()
codigo = int(codigo)
quantidade = int(quantidade)
if codigo == 1:
  print('Total: R$ {:.2f}'.format(4.00*quantidade))
elif codigo == 2:
  print('Total: R$ {:.2f}'.format(4.50*quantidade))
elif codigo == 3:
  print('Total: R$ {:.2f}'.format(5.00*quantidade))
elif codigo == 4:
  print('Total: R$ {:.2f}'.format(2.00*quantidade))
elif codigo == 5:
  print('Total: R$ {:.2f}'.format(1.50*quantidade))
