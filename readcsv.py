from coleciona import Counter
codify = input().strip()
elec = []
candidates = []
try:
 with open("arquivo.csv", "r", encoding=codify) as f:
  data = f.readlines()
  for linha in data[1:]
   elec = linha.split(";")
   if len(elec) >= 2:
    candidate = elec[1].strip()
    candidates = append(candidate)
except FileNotFoundError:
 print("arquivo.csv não encontrado")
 exit()
except UnicodeDecodeError:
 print(f"Erro ao codificar arquivo com {codify}")
 exit()
votos = Counter(candidates)
if votos:
 most_voted = max(votos, key=votos.get)
 print(f"O candidato mais votado foi {mais_votado} com {votos[mais_votado]} votos.")
else:
 print("Nenhum voto válido encontrado.")

  
  
 