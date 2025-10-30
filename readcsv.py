codify = input().strip()
with open("arquivo.csv", "r", encoding=codify) as f:
 data = f.read()
 except FileNotFoundError