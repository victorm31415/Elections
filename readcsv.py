from collections import Counter
codify = input("Escreva qual a sua codificação (ex: utf-8)").strip()
elec = []
candidates = []
try:
 with open("arquivo.csv", "r", encoding=codify) as f:
  data = f.readlines()
  for linha in data[1:]:
   elec = linha.split(";")
   if len(elec) >= 2:
    candidate = elec[1].strip()
    candidates.append(candidate)
except FileNotFoundError:
 print("arquivo.csv não encontrado")
 exit()
except UnicodeDecodeError:
 print(f"Erro ao codificar arquivo com {codify}")
 exit()
votes = Counter(candidates)
if votes:
 most_voted = max(votes, key=votes.get)
 print(f"O candidato mais votado foi {most_voted} com {votes[most_voted]} votos.")
else:
 print("Nenhum voto válido encontrado.")
print("\nResultado completo:")
for candidate, total in votes.most_common():
 print(f"{candidate}: {total} votos")

  
  
 