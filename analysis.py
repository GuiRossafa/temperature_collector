import pandas as pd
import matplotlib.pyplot as plt

def analises_registros(arquivo):
    df = pd.read_csv(arquivo)

    df['data'] = pd.to_datetime(df['data'], errors= 'coerce')
    df = df.dropna(subset= 'data')

    df['valor'] = pd.to_numeric(df['valor'], errors= 'coerce')
    df = df.dropna(subset= 'valor')

    est_valor = df['valor'].describe()
    contagem = df['status'].value_counts()

    qtd_v = contagem['OK']
    qtd_sup = contagem.get('Superaquecimento', 0)
    qtd_inv = contagem.get('Leitura inválida', 0)

    print(f"O número de leituras válidas foram de: {qtd_v}. \nO número de leituras inválidas e/ou ignoradas foi de: {qtd_sup + qtd_inv}")

    return df


def visualização_leituras(df):
    
    x = df['data']
    y = df['valor']

    fig, ax = plt.subplots()

    ax.plot(x, y)

    ax.set_title("Monitoramento de Temperatura")
    ax.set_xlabel("Hora da Leitura")
    ax.set_ylabel("Temperatura (ºC)")

    plt.show()



df = analises_registros('log_registros.csv')
visualização_leituras(df)

