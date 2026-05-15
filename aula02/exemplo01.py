#pip install openpyxl ----- P/ ler planilhas do excel
import pandas as pd

df_eletricos = pd.read_excel('vendas_eletronicos.xlsx')

#Primeiras
print(df_eletricos.head(10))

# 
print('\n Maior valor do Faturamento')
print(45 * '=')
print(df_eletricos.loc[df_eletricos['Faturamento Total (R$)'].idxmax(), 'Produto'])
print(df_eletricos['Faturamento Total (R$)'].max())

print('\n Menor valor do Faturamento')
print(45 * '=')
print(df_eletricos.loc[df_eletricos['Faturamento Total (R$)'].idxmin(), 'Produto'])
print(df_eletricos['Faturamento Total (R$)'].min())

print('\n Total de unidades vendidas')
print(45 * '=')
print(df_eletricos['Unidades Vendidas'].sum())

print('\n Preço médio dos produtos')
print(45 * '=')
print(df_eletricos['Preço por Unidade (R$)'].mean())

print('\n Produto acima da média')
print(45 * '=')
media = df_eletricos['Faturamento Total (R$)'].mean()
print(df_eletricos[df_eletricos['Faturamento Total (R$)'] >= media])
