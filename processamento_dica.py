import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_excel("planilha-lucas.xlsx")
df = pd.DataFrame(data)

dica = 0
for item in df["Ação do Museu Dica (Sim/Não)"]:
    dica += 1 if item == "Sim" else 0

print(f"Total de ações do Museu Dica: {dica}")

nao_dica = len(df) - dica
print(f"Total de ações que não são do Museu Dica: {nao_dica}")