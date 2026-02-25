indice = int(input("Qual o exercício desejado? (1 a 8): "))

if indice == 1:
  n = int(input())

  for i in range(n):
    print (i)

elif indice == 2:
  n = int(input())

  for i in range(1, n + 1):
    print (i)

elif indice == 3:
  n = int(input())

  for i in range(1, 12):
    tabuada = n * i
    print(tabuada)

elif indice == 4:
  ntabuada = int(input())
  iniciotabuada = int(input())
  fimtabuada = int(input())

  for i in range(iniciotabuada, fimtabuada + 1):
    tabuada = ntabuada * i
    print(ntabuada, "x", i, "=", tabuada)
  
elif indice == 5:
  coisa = input()
  qtdeenrol = int(input())

  for i in range (1, qtdeenrol + 1):
    print("enrolando", coisa, i)
  
elif indice == 6:
  n = int(input())
  s = ''

  for i in range(n):
    s = ''
    for j in range(n):
      if j == i or j + i == n - 1:
        s = s + '+ '
      else:
        s = s + '* '
    print(s)

elif indice == 7:
  nmoedas = int(input())
  total = 0

  for i in range(nmoedas):
    valor = float(input())
    total = total + valor
  print('%.2f' % total)
  
elif indice == 8:
  napostas = int(input())
  total = 0

  for i in range(napostas):
    valor = float(input())
    total = total + valor
  print('%.2f' % total)

else:
  print("Command not found")
