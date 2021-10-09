import pandas as pd

file = "../Operacao_Datasets/Arquivo_csv.csv"
df = pd.read_csv(file)
print(df.head())