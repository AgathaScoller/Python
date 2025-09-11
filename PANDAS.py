import pandas as pd

# Criar dados da planilha
dados = {
    "Nome": ["João", "Maria", "Pedro", "Ana", "Lucas"],
    "Idade": [25, 30, 22, 28, 35],
    "Cidade": ["SP", "RJ", "BH", "SP", "RJ"],
    "Salário": [3500, 4200, 3100, 3900, 5000]
}

# Criar a planilha (DataFrame)
df = pd.DataFrame(dados)

# Mostrar no terminal
print(" Planilha criada:")
print(df)

# Salvar como CSV
df.to_csv("funcionarios.csv", index=False)
print("\n Arquivo 'funcionarios.csv' salvo com sucesso!")

# Ler de novo o arquivo
df_lido = pd.read_csv("funcionarios.csv")
print("\n Lendo o CSV salvo:")
print(df_lido)

# Fazer uma análise simples
print("\n Média salarial:")
print(df_lido["Salário"].mean())

print("\n Salário médio por cidade:")
print(df_lido.groupby("Cidade")["Salário"].mean())
