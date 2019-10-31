
import csv
with open('dados.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    cabecalho = True
    mapeamento=[]
    tamanho=[]
    legenda=[]
    aux=[]
    flag=0
    probabilidade = []
    for coluna in range(0,33):
        tamanho.append(0)
        for row in csv_reader:
            flag=0
            if row[4]=="true":
                for elemento in aux:
                    if row[coluna]==elemento:
                        probabilidade[aux.index(elemento)]=probabilidade[aux.index(elemento)]+1
                        flag=1
                if flag==0:
                    aux.append(row[coluna])
                    probabilidade.append(1)
                    tamanho[coluna]=tamanho[coluna]+1
        legenda.append(aux)
        aux=[]
        mapeamento.append(probabilidade)
        probabilidade=[]
        flag=0
print (legenda)
print (probabilidade)
