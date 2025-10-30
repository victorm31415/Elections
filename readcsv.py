codify = input().strip()
with open("arquivo.csv", "r", encoding=codify) as f:
 data = f.read()
 except FileNotFoundError:
  print("arquivo.csv não encontrado")
 except UnicodeDecodeError:
  print("Erro ao codificar arquivo com {codify}")
 