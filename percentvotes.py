import csv
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
except UnicodeDecodeError:
  print(f"Erro ao decodificar arquivo com {codify}")
for city, candidates in votes_per_city.items():
  total_votes = len(candidates)
  counter = Counter(candidates)
  print(f"Cidade: {city}")
  for candidate, count in counter.items():
      percentage = (count / total_votes) * 100
      print(candidate, f"{percentage:.2f}%")
  print("-"*30)


