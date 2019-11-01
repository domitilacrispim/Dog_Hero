import csv
import numpy as np
import matplotlib.pyplot as plt
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
   if row[32]=="false":
    if row[col] in mapeamento[col]:
     fracasso[col][mapeamento[col].index(row[col])]=fracasso[col][mapeamento[col].index(row[col])]+1
    else:
     mapeamento[col].append(row[col])
     fracasso[col].append(1)
     sucesso[col].append(0)
