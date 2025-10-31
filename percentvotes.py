import csv
import sys
from collections import defaultdict, Counter
codify = input("Digite a codificação:")
votes_per_city = defaultdict(list)
try:
  with open("arquivo.csv", "r", encoding=codify) as f:
   dados = csv.reader(f, delimiter=";")
   next(dados, None)
   for elec in dados:
    if len(elec) >=2:
     city = elec[0].strip().title()
     candidate = elec[1].strip().upper()
     votes_per_city[city].append(candidate)
except FileNotFoundError:
  print(f"Não foi possível encontrar o arquivo")
  sys.exit()
except UnicodeDecodeError:
  print(f"Erro ao decodificar arquivo com {codify}")
  sys.exit()
arq_final = "resultado.csv"
with open("resultado.csv", "w",encoding="utf-8") as out:
  dados_finais = csv.writer(out, delimiter=";")
   dados_finais.writerow(["Cidade","Candidato","Porcent agem"])
  
for city, candidates in votes_per_city.items():
  total_votes = len(candidates)
  counter = Counter(candidates)
  print(f"Cidade: {city}")
  for candidate, count in counter.most_common():
      percentage = (count / total_votes) * 100
      print(candidate, f"{percentage:.2f}%")
  print("-"*30)


