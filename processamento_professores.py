import pandas as pd
import numpy as np

data = pd.read_excel("planilha-lucas.xlsx")

df = pd.DataFrame(data)

professores = df["Professor/Equipe (Coordenador)"]

def count_professor(name):
    c = 0
    for item in professores:
        if item == name : c += 1

    return c

mariana = count_professor("MARIANA MIEKO ODASHIMA")
lucio = count_professor("LUCIO PEREIRA NEVES")
diego = count_professor("DIEGO MERIGUE DA CUNHA")
silvia = count_professor("SILVIA MARTINS DOS SANTOS")
joao = count_professor("JOAO CARLOS DE OLIVEIRA GUERRA")
adevalton = count_professor("ADEVAILTON BERNARDO DOS SANTOS")
marco = count_professor("MARCO AURELIO BOSELLI")
ricardo = count_professor("RICARDO KAGIMURA")
alessandra = count_professor("ALESSANDRA RIPOSATI ARANTES")
raimundo = count_professor("RAIMUNDO LORA SERRANO")
liliana = count_professor("LILIANA SANZ DE LA TORRE")
gustavo = count_professor("GUSTAVO FORESTO BRITO DE ALMEIDA")
ana = count_professor("ANA PAULA PERINI")
tome = count_professor("TOME MAURO SCHMIDT")
adilmar = count_professor("ADILMAR COELHO")
altair = count_professor("ALTAIR RAMOS GOMES JÚNIOR")
sorandra = count_professor("SORANDRA CORRÊA DE LIMA")
mauricio = count_professor("MAURICIO FOSCHINI")
ricardo_avila = count_professor("RICARDO RIBEIRO DE ÁVILA")
debora = count_professor("DEBORA COIMBRA")
gabriela = count_professor("GABRIELA VIEIRA LIMA")
anielle = count_professor("ANIELLE CHRISTINE ALMEIDA SILVA")

dados_profs = {
    "M. M. Odashima": mariana,
    "L. P. NEVES": lucio,
    "D. M. CUNHA": diego,
    "S. M. DOS SANTOS": silvia,
    "J. C. DE OLIVEIRA GUERRA": joao,
    "A. B. DOS SANTOS": adevalton,
    "M. A. BOSELLI": marco,
    "R. KAGIMURA": ricardo,
    "A. R. ARANTES": alessandra,
    "R. L. SERRANO": raimundo,
    "L. S. DE LA TORRE": liliana,
    "G. F. BRITO DE ALMEIDA": gustavo,
    "A. P. PERINI": ana,
    "T. M. SCHMIDT": tome,
    "A. C. COELHO": adilmar,
    "A. R. GOMES JÚNIOR": altair,
    "S. C. DE LIMA": sorandra,
    "M. FOSCHINI": mauricio,
    "R. R. DE ÁVILA": ricardo_avila,
    "D. COIMBRA": debora,
    "G. V. LIMA": gabriela,
    "A. C. ALMEIDA SILVA": anielle
}

dados_profs = dict(sorted(dados_profs.items(), key=lambda item: item[1], reverse=True))
print(dados_profs)

print(f"média de ações por professor: {sum(dados_profs.values())/len(dados_profs):.2f}")
