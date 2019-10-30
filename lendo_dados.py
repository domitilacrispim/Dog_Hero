import csv
with open('dados.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    cabecalho = True
    for row in csv_reader:
        print(row[0])
