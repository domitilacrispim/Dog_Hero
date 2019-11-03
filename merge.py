import csv

class Anfitriao(object): 
  def __init__(self, nota, linha): 
    self.__nota = nota 
    self.__linha = linha 
  def get_valor(self): 
    return self.__nota
  def get_linha(self): 
    return self.__linha

with open('teste.csv') as csv_file:
 csv_reader = csv.reader(csv_file)
 anfitrioes=[]
 i=0
 for row in csv_reader: 
  i=i+1
  p = Anfitriao(float(row[0]), i)
  anfitrioes.append(p)
 anfitrioes = sorted(anfitrioes, key=Anfitriao.get_valor)

print("Escolha o tanto de anfitrioes que voce gostaria de visualizar:")
num=int(input())
for i in range (0, num):
 print(anfitrioes[i].get_valor(), anfitrioes[i].get_linha())
