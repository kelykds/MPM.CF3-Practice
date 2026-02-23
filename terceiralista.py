indice = int(input("Qual o exercício desejado? (1 a 8): "))

if indice == 1:
  num_palavras = 0

  while input() != 'final feliz':
    num_palavras = num_palavras + 1
  print(num_palavras)

elif indice == 2:
  pares = 0
  impares = 0
  num = int(input())

  while num >= 0:
    if num % 2 == 0:
      pares = pares + 1
    else:
      impares = impares + 1

    num = int(input())

  print("pares: ", pares)
  print("ímpares: ", impares)

elif indice == 3:
  capacidade = int(input())
  valorfeira = 0

  while valorfeira < capacidade:
    peso = int(input())
    valorfeira = valorfeira + peso
  if valorfeira > capacidade:
    print("Fim de feira: levo tudo menos o último item.")
    valorfeira = valorfeira - peso
  elif valorfeira == capacidade:
    print("Fim de feira: levo tudo mas não cabe mais nada")

elif indice == 4:
  positivos = 0
  num = int(input())

  while num >= 0:
    if num != 0:
      positivos = positivos + 1
    num = int(input())

  print(positivos)
  
elif indice == 5:
  nomealvo = input()
  qtdenomes = 0
  nome = input()

  while nome != nomealvo:
    qtdenomes = qtdenomes + 1
    nome = input()

  print (qtdenomes)
  
elif indice == 6:
  num_pares = 0
  par1 = int(input())
  par2 = int(input())
  
  while par1 != -1 and par2 != -1:
    if par1 == par2:
      num_pares = num_pares + 1
  
    par1 = int(input())
    par2 = int(input())

  print(num_pares)

elif indice == 7:
  qtdepao = 0
  p = input()

  while p != 'fim':
    if p == 'pao':
      qtdepao = qtdepao + 1
    p = input()

  print(qtdepao)

elif indice == 8:
  total = 0
  valor = int(input())

  while valor > 0 or valor < 0:
    total = total + valor
    valor = int(input())

  print(total)

else:
  print("Command not found")
