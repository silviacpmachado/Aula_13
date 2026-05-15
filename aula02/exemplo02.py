import pandas as pd

#Visão geral dos dados da planilha
df_roupas = pd.read_excel('vendas_roupas.xlsx')
print(df_roupas)

#Quantidade Total de peças vendidas
print('\n Quantidade Total de pecas vendidas')
print(45 * '=')
print(df_roupas['Unidades Vendidas'].sum())

# Média dos Preços dos produtos
media = df_roupas['Faturamento Total (R$)'].mean()

#Produto com Maior Faturamento
print('\ Maior Faturamento')
print(45 * '=')
print(df_roupas['Faturamento Total (R$)'].max())

#Produto com Menor Faturamento
print('\ Menor Faturamento')
print(45 * '=')
print(df_roupas['Faturamento Total (R$)'].min())

#Produto com Nível de Satisfação Baixo
print('\ Nível de Satisfação Baixo')
print(45 * '=')
print(df_roupas[df_roupas['Satisfação'] == 'Baixo'])

#Produtos com faturamento acima da média
print('\ Produto acima da Média')
print(45 * '=')
media = df_roupas['Faturamento Total (R$)'].mean()
print(df_roupas[df_roupas['Faturamento Total (R$)'] >= media])




