codify = input().strip()
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
votos = {
 "C1": el1,
 "C2": el2,
 "C3": el3,
 "C4": el4,
 "C5": el5,
 "C6": el6,
 "C7": el7,
 "C8": el8,
 "C9": el9
}
most_voted = max(votos, key=votos.get)
print(f"O candidato mais votado foi {mais_votado} com {votos[mais_votado]} votos.")
except FileNotFoundError:
 print("arquivo.csv não encontrado")
 exit()
except UnicodeDecodeError:
 print("Erro ao codificar arquivo com {codify}")
 exit()
 

  
  
 