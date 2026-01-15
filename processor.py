def analisar_temperatura(valor_entrada, hora_leitura):
    leitura = {#Recebe e armazena todas as entradas
        "sensor": "S-01",
        "data": "",
        "valor": "",
        "status": ""

    }  

    try:

        temperatura = float(valor_entrada)#Transforma a entrada em um valor float

        if temperatura <=0:

            update = {"data": hora_leitura, "valor": temperatura, "status": "Leitura inválida"}
            leitura.update(update)
            print("Erro: leitura inválida (valor = ou > que 0)")
        
        elif temperatura >=1000:

            update = {"data": hora_leitura, "valor": temperatura, "status": "Superaquecimento"}
            leitura.update(update)
            print("!Aviso: Superaquecimento ignorado no cálculo!")

        else:

            update = {"data": hora_leitura, "valor": temperatura, "status": "OK"}
            leitura.update(update)
            print(f"Entrada Registrada com sucesso!\n{hora_leitura}")

        return leitura
        
    except ValueError as e:

        print(f"Entrada{e} ínvalida. Por favor, digite um número ou PARAR, para receber o relatório")

        return None

def gerar_relatorio(lista):

    if len(lista) > 0:

        media = sum(valor["valor"] for valor in lista) / len(lista)
        print(f"SEU RELATÓRIO".center(28, "-"))
        print(f"LEITURAS VÁLIDAS: {len(lista)}")
        print(f"A MÉDIA DE TEMPERATURA FOI: {media}")
    
    else:
        print("Nenhuma leitura válida foi registrada")
