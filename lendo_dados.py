import csv
import numpy as np
from sklearn import svm, datasets
with open('dados.csv') as csv_file:
 csv_reader = csv.reader(csv_file)
 dados=[]
 total=0
 for row in csv_reader:
  total=total+1
  dados.append(row)
 mapeamento=[]
 sucesso=[]
 fracasso=[]
 for col in range (0,31):
  mapeamento.append([])
  fracasso.append([])
  sucesso.append([])
  for row in dados:
   if row[32]=="true":
    if row[col] in mapeamento[col]:
     sucesso[col][mapeamento[col].index(row[col])]=sucesso[col][mapeamento[col].index(row[col])]+1
    else:
     mapeamento[col].append(row[col])
     sucesso[col].append(1)
     fracasso[col].append(0)
   else:
    if row[col] in mapeamento[col]:
     fracasso[col][mapeamento[col].index(row[col])]=fracasso[col][mapeamento[col].index(row[col])]+1
    else:
     mapeamento[col].append(row[col])
     fracasso[col].append(1)
     sucesso[col].append(0)


with open('dog_hero.csv') as csv_file:
 csv_reader = csv.reader(csv_file)
 dados2=[]
 for row in csv_reader:
  dados2.append(row) 
 anfitrioes=[]
 parcial=[]
 coluna=-1
 coli=0
 for col in range (0,32):
  it=-1
  coluna=coluna+1
  prox=1000000
  proc=0
  for row in dados2:
   prox=1000000
   it=it+1
   if col==0:
    anfitrioes.append([])
    parcial.append(0)
   for elemento in row:
    proc=1
    if ( coluna==0 or coluna==1 or coluna==5 or coluna==6 or coluna==9 or coluna==11 or coluna==17 or coluna==26):
     anfitrioes[it].append("-")
    elif coluna!=4 :
     try:
      anfitrioes[it].append(float(elemento))
     except:
      proc=0
     if elemento in mapeamento[col]:
      coli=mapeamento[col].index(elemento)
      parcial[it]=parcial[it]+(sucesso[col][coli]/(sucesso[col][coli]+fracasso[col][coli]))
     elif proc==1:
      for i in mapeamento[col]:
       if proc==1:
        try:
         if prox>abs(float(elemento)-float(i)):
          prox=abs(float(elemento)-float(i))
          coli=mapeamento[col].index(i)
        except:
         coli=-1
      if(coli!=-1):
       parcial[it]=parcial[it]+(sucesso[col][coli]/(sucesso[col][coli]+fracasso[col][coli]))               
    else:
     anfitrioes[it].append(0)
   anfitrioes[it][4]=parcial[it]
with open("saida.csv", "w", newline=''):
 escrever=csv.writer(saida)
 for i in anfitrioes:
  escrever.writerow([i[4]])

