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
    for coluna in range(0,1):
        tamanho.append(0)
        for row in csv_reader:
            if row[4]=="true":
                for elemento in legenda:
                    if row[coluna]==legenda[elemento]:
                        probabilidade[elemento]=probabilidade[elemento]+1
                        flag=1
                if flag==0:
                    aux.append(row[coluna])
                    probabilidade.append(1)
                    tamanho[coluna]=tamanho[coluna]+1
        legenda.append(aux)
        mapeamento.append(probabilidade)
        flag=0
print (legenda)

