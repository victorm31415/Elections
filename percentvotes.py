import csv
from collections import defaultdict, Counter
codify = input("Digite a codificação:")
votes_per_city = defaultdict(list)
try:
 with open("arquivo.csv", "r", encoding=codify) as f:
  dados = csv.reader(f, delimitar=";")
  next(dados, None)
  for elec in dados:
   if len(elec) >=2:
    city = elec[0].strip.title()
    candidate = elec[1].strip.upper()
