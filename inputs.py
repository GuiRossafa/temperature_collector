#IMPORTS#
from datetime import datetime
#IMPORTS/#

def obter_leitura():
    entrada = input("Informe a temperatura:").strip()
    ler_tempo = datetime.now()
    tempo_formatado = ler_tempo.strftime("%H:%M:%S %d-%m")

    return entrada, tempo_formatado #Retornar ambos valores para a função obter_leitura()