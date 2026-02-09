programa = input("Qual o exercício desejado? (1 a 11): ")
if programa == "1":
  operacao = input()
  num1 = int(input())
  num2 = int(input())

  if operacao == "+":
    saida = num1 + num2
    print(saida)
  elif operacao == "-":
    saida = num1 - num2
    print(saida)
  elif operacao == "*":
    saida = num1 * num2
    print(saida)
  elif operacao == "/":
    saida = float(num1 / num2)
    print('%.2f' % saida)
  elif operacao == "//":
    saida = num1 // num2
    print(saida)
  elif operacao == "%":
    saida = num1 % num2
    print(saida)
  elif operacao == "**":
    saida = num1 ** num2
    print(saida)
  else:
    print("Nenhuma operação reconhecida.")
  
elif programa == "2":
  total_conta = float(input())
  total_compra = float(input())

  if total_compra > total_conta:
    print("Saldo insuficiente.")
  else:
    print("Pode comprar tudo.")
    
elif programa == "3":
  total_conta = float(input())
  total_compra = float(input())

  if total_conta < total_compra:
    print("Seu saldo é insuficiente para essa compra.")
  else:
    restante = total_conta - total_compra
    print('%.2f' % restante)
    
elif programa == "4":
  tecla = input()

  if tecla == "w":
    print("UP")
  elif tecla == "W":
    print("UP")
  elif tecla == "s":
    print("DOWN")
  elif tecla == "S":
    print("DOWN")
  elif tecla == "a":
    print("LEFT")
  elif tecla == "A":
    print("LEFT")
  elif tecla == "d":
    print("RIGHT")
  elif tecla == "D":
    print("RIGHT")
  else:
    print("?")
  
elif programa == "5":
  idade = int(input())

  if idade >= 60:
    print(idade, "Melhor idade")

  print("Fim")
  
elif programa == "6":
  resposta1 = input()
  resposta2 = input()

  if resposta1 == "V":
    if resposta2 == "V":
      print("VV")
    else:
      print("?")
  elif resposta1 == "F":
    if resposta1 == "F":
      print("FF")
    else: 
      print("?")
  else:
    print("?")
    
elif programa == "7":
  hrs_sono = float(input())

  if hrs_sono < 8:
    print("Você precisa de mais tempo de sono, cuide-se!")
  elif hrs_sono > 8:
    print("Você dormiu muito bem, parabéns!")
  else:
    print("Você dormiu o suficiente, continue assim!")
    
elif programa == "8":
  valor1 = int(input())
  valor2 = int(input())

  if valor1 < valor2:
    print(valor2, "é maior que", valor1)
  else:
    print(valor2, "é menor ou igual a", valor1)
elif programa == "9":
  idade1 = int(input())
  idade2 = int(input())
  idade3 = int(input())

  if idade1 > idade2:
    if idade1 > idade3:
      print("A primeira irmã é a mais velha.")
    else:
      print("A terceira irmã é a mais velha.")
  elif idade2 > idade1:
    if idade2 > idade3:
      print("A segunda irmã é a mais velha.")
    else:
      print("A terceira irmã é a mais velha.")
  elif idade3 > idade1:
    if idade3 > idade2:
      print("A terceira irmã é a mais velha.")
    else:
      print("A segunda irmã é a mais velha.")
  elif idade1 > idade3:
    if idade1 > idade2:
      print("A primeira irmã é a mais velha.")
    else:
      print("A segunda irmã é a mais velha.")
  elif idade2 > idade3:
    if idade2 > idade1:
      print("A segunda irmã é a mais velha.")
    else:
      print("A primeira irmã é a mais velha.")
  else:
    print("As idades são iguais.")
    
elif programa == "10":
  idade1 = int(input())
  idade2 = int(input())
  idade3 = int(input())

  if idade1 > idade2:
    if idade1 > idade3:
      print("A primeira irmã é a mais velha.")
      if idade2 > idade3:
        print("A terceira irmã é a mais nova.")
      else:
        print("A segunda irmã é a mais nova.")
    else:
      print("A terceira irmã é a mais velha.")
      print("A segunda irmã é a mais nova.")
  elif idade2 > idade1:
    if idade2 > idade3:
      print("A segunda irmã é a mais velha.")
      if idade1 > idade3:
        print("A terceira irmã é a mais nova")
      else:
        print("A primeira irmã é a mais nova.")
    else:
      print("A terceira irmã é a mais velha.")
      print("A primeira irmã é a mais nova.")
  elif idade3 > idade1:
    if idade3 > idade2:
      print("A terceira irmã é a mais velha.")
      if idade1 > idade2:
        print("A segunda irmã é a mais nova.")
      else:
        print("A primeira irmã é a mais nova.")
    else:
      print("A segunda irmã é a mais velha.")
      print("A primeira irmã é a mais nova.")
  elif idade1 > idade3:
    if idade1 > idade2:
      print("A primeira irmã é a mais velha.")
      if idade2 > idade3:
        print("A terceira irmã é a mais nova.")
      else:
        print("A segunda irmã é a mais nova.")
    else:
      print("A segunda irmã é a mais velha.")
      print("A terceira irmã é a mais nova.")
  elif idade2 > idade3:
    if idade2 > idade1:
      print("A segunda irmã é a mais velha.")
      if idade1 > idade3:
        print("A terceira irmã é a mais nova.")
      else:
        print("A primeira irmã é a mais nova.")
    else:
      print("A primeira irmã é a mais velha.")
      print("A terceira irmã é a mais nova.")
  else:
    print("As idades são iguais.")
elif programa == "11":
  letra = input()

  if letra == "I":
    print("1")
  elif letra == "V":
    print("5")
  elif letra == "X":
    print("10")
  elif letra == "L":
    print("50")
  elif letra == "C":
    print("100")
  elif letra == "D":
    print("500")
  elif letra == "M":
    print("1000")
  else:
    print("Algarismo não identificado.")
    
else:
  print("Não existe. Tenha certeza de digitar um número entre 1 a 11, inclusive.")
