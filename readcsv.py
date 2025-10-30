codify = input().strip()
best_candidate = []
elec = []
el1=0
el2=0
el3=0
el4=0
el5=0
el6=0
el7=0
el8=0
with open("arquivo.csv", "r", encoding=codify) as f:
 data = f.readlines()
 except FileNotFoundError:
  print("arquivo.csv não encontrado")
 except UnicodeDecodeError:
  print("Erro ao codificar arquivo com {codify}")
 for linha in data:
  elec = linha.split(";")
  if elec[1] == "C1":
   el1 += 1
  if elec[1] == "C2":
   el2 += 1
  if elec[1] == "C3":
   el3 += 1 
  if elec[1] == "C4":
   el4 += 1
  if elec[1] == "C5":
   el5 += 1
  if elec[1] == "C6":
   el6 += 1
  if elec[1] == "C7":
   el7 += 1 
  if elec[1] == "C8":
   el8 += 1

  
  
 