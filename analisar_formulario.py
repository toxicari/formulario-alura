import csv
from collections import Counter

# Substitua 'respostas.csv' pelo nome do seu arquivo exportado do Google Forms
ARQUIVO_CSV = 'SOS Chikinha (respostas) - Respostas ao formulário 1 (1).csv'

# Função para ler e analisar o CSV
def analisar_formulario(arquivo_csv):
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv(arquivo_csv)
    print(f'Total de respostas: {len(df)}')

    print('\nPerguntas encontradas:')
    for coluna in df.columns:
        print(f'- {coluna}')

    print('\nResumo das respostas:')
    for coluna in df.columns[1:]:  # Ignora o carimbo de data/hora
        print(f'\n{coluna}:')
        contagem = df[coluna].value_counts()
        for resposta, qtd in contagem.items():
            porcentagem = (qtd / len(df)) * 100
            print(f'  {resposta}: {qtd} respostas ({porcentagem:.1f}%)')

    # Sugestão de visualização: gráfico de recomendações
    if 'Você (como cliente) recomendaria o parquinho para conhecidos?' in df.columns:
        recomendacoes = df['Você (como cliente) recomendaria o parquinho para conhecidos?'].value_counts()
        recomendacoes.plot.pie(autopct='%1.1f%%', startangle=90, title='Recomendação do Parquinho')
        plt.ylabel('')
        plt.show()

if __name__ == '__main__':
    analisar_formulario(ARQUIVO_CSV)
