import csv
from pathlib import Path
file_path = Path("Files/sample_data.csv")
lista : list = []
with open(file=file_path, mode='r',encoding='utf-8',newline='') as f:
    reader = csv.DictReader(f)

    for line in reader:
        lista.append(line)
        


print(lista)



from algoritmo import ordenar_numeros_lista
lista