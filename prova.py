indice = int(input("Escolha um número de 1 até 4: "))

if indice == 1:
  print("O tempo todo a equipe do projeto MPM.PPM precisa mostrar o impacto de suas ações voluntárias para que")
  print("o projeto posso continuar.")
  print("Para compreender melhor a escala desse esforço, considere o número total de voluntárias, o número de")
  print("monitorias que cada uma ofertou, e o número médio de alunas que participou cada monitoria.")
  
  n_voluntarias = int(input())
  n_monitorias = int(input()) 
  n_medio_alunas = int(input())

  n_total_atend = n_voluntarias * n_monitorias * n_medio_alunas 


  print(n_total_atend)

elif indice == 2:
  print("As alunas que fazem o MPM.CF2 sabem que devem participar de pelo menos 3h de monitoria por semana, e")
  print("você quer ajudar! Dado o número de minutos que uma aluna participou de monitoria em uma semana, você")
  print("deve fazer um programa verifica se a aluna fez o suficiente, ficou devendo ou fez a mais.")
  
  n_min = int(input())

  if n_min == 180:
    print("Suficiente.")
  elif n_min < 180:
    print("Ficou devendo.")
  else:
    print("Fez a mais.")

elif indice == 3:
  print("A cada momento, a coordenação pode precisar consultar quantas alunas estiveram presentes em")
  print("cada aula, por exemplo, para informar aos orgãoes competentes. Para ajudar a equipe de voluntárias, você")
  print("deve fazer um programa que, dado o número de semanas já ocorridas, leia o número de alunas presentes")
  print("em cada aula e informe o número total de presenças.")

  n_aulas = int(input()) # Pega o número de aulas
  total_presencas = 0 # Define a variável para ser utilizada posteriormente

  for i in range(n_aulas):
    n_alunas_presentes = int(input())
    total_presencas = total_presencas + n_alunas_presentes 

  print(total_presencas, "presenças em", n_aulas, "aulas.")

elif indice == 4:
  print("Cada vez que uma aluna acerta um exercício, as voluntárias ficam muito muito muito felizes: as voluntárias")
  print("corrigem os exercícios e comemoram a cada acerto.")
  print("Seu programa deve ler o número de exercicios corretos que cada monitora vai corrigindo")
  print("e, no final, verificar quantas vezes elas comemoraram.")
  
  ex_corretos = int(input())
  ndecom = 0 

  while ex_corretos >= 0:
    ndecom = ndecom + ex_corretos 
    ex_corretos = int(input()) 

  print("Corretos:", ndecom)
