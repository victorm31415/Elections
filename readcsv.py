codify = input().strip()
candidates = []
elec = []

with open("arquivo.csv", "r", encoding=codify) as f:
 data = f.readlines()
 except FileNotFoundError:
  print("arquivo.csv não encontrado")
 except UnicodeDecodeError:
  print("Erro ao codificar arquivo com {codify}")
 for linha in data:
  elec = linha.split(";")
  
  
 