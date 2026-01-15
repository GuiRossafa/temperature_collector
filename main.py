from inputs import obter_leitura
from processor import analisar_temperatura
from processor import gerar_relatorio
from data_saving import salvar_dados

if __name__ == "__main__":

    registros = []#Guardar todas as leituras.
    registros_validos = []#Guarda apenas as leituras válidas para análise

    print("AUDITOR INICIADO".center(28, "-"))
    print("Para encerrar o programa, digite 'PARAR'")

    while True:

        temperatura, hora_leitura = obter_leitura()

        if temperatura.upper() == "PARAR":
            gerar_relatorio(registros_validos)
            break
        else:
            guarda_leitura = analisar_temperatura(temperatura, hora_leitura)

            if guarda_leitura is None:
                print("Valor não registrado")
            else:

                salvar_dados(guarda_leitura)

                if guarda_leitura["status"] == "OK":
                
                    registros.append(guarda_leitura)
                    registros_validos.append(guarda_leitura)

                else:

                    registros.append(guarda_leitura)