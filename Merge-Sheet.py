import pandas as pd
import sys  
import warnings


def ler_planilha(caminho):
    df = pd.read_excel(caminho)
    df['Data do Negócio'] = pd.to_datetime(df['Data do Negócio'], format='%d/%m/%Y')
    return df

def unir_planilhas(lista_dfs):
    df_unido = pd.concat(lista_dfs, ignore_index=True)
    return df_unido


def ordenar_por_data(df):
    df_ordenado = df.sort_values('Data do Negócio')
    return df_ordenado

if __name__ == '__main__':
    caminhos_planilhas = sys.argv[1:]
    lista_planilhas = [ler_planilha(caminho) for caminho in caminhos_planilhas]
    df_unido = unir_planilhas(lista_planilhas)
    df_ordenado = ordenar_por_data(df_unido)

    df_ordenado.to_excel("planilha_unida.xlsx", index=False)

    print("Planilha unida e ordenada salva como 'planilha_unida.xlsx'.")
