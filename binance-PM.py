import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "cripto", help="Nome da criptomoeda a ser calculada. Ex: BTC")
parser.add_argument(
    "planilha_cripto", help="Nome da planilha contendo os dados de histórico de transações da criptomoeda. Ex: historico_btc.csv")
parser.add_argument("--planilhaUSDT", dest="planilhaUSDT",
                    help="Nome da planilha contendo os dados de histórico de transações USDT. Ex: historico_usdt.csv")
parser.add_argument("--planilhaLTC", dest="planilhaLTC",
                    help="Nome da planilha contendo os dados de histórico de transações LTC. Ex: historico_ltc.csv")
parser.add_argument("--planilhaBTC", dest="planilhaBTC",
                    help="Nome da planilha contendo os dados de histórico de transações BTC. Ex: historico_btc.csv")

args = parser.parse_args()

if args.planilhaUSDT:
    planilha_USDT = pd.read_csv(args.planilhaUSDT)
if args.planilhaLTC:
    planilha_LTC = pd.read_csv(args.planilhaLTC)
if args.planilhaBTC:
    planilha_BTC = pd.read_csv(args.planilhaBTC)
planilha_cripto_analisada = pd.read_csv(args.planilha_cripto)


class criptomoeda:  # classe cripto para iniciar com PM e QTD como 0
    def __init__(self, nome, precoMedio=0, quantidade=0):
        self.precoMedio = precoMedio
        self.quantidade = quantidade
        self.nome = nome

    def __str__(self) -> str:
        return self.nome + ' --- (' + str(self.precoMedio) + ', ' + str(self.quantidade) + ')'


# funcao para calcular o preço médio de duas compras
def calcularPrecoMedio(cripto, precoComprado, quantidadeComprada):
    quantidadeTotal = abs(cripto.quantidade) + abs(quantidadeComprada)
    precoMedio = ((abs(cripto.precoMedio) * (abs(cripto.quantidade))) +
                  (abs(precoComprado) * (abs(quantidadeComprada)))) / quantidadeTotal
    atualizaPlanilha(cripto, precoMedio, quantidadeTotal)


# funcao para atualizar na planilha os novos valores de PM e QTD
def atualizaPlanilha(cripto, precoMedio, quantidade):
    planilha_cripto_analisada.at[idx,
                                 'Preço Médio'] = cripto.precoMedio = precoMedio
    planilha_cripto_analisada.at[idx,
                                 'Quantidade'] = cripto.quantidade = quantidade
    # print(cripto)


def calculaPMConversao(moeda, planilha_historicoPM, linha):
    # pega a quantidade da moeda a ser convertida
    qtd_moeda_original = float(linha['Sell'].split()[0])
    # busca a cotação da moeda no dia da conversão na planilha com o historico
    cotacao_moeda_original = float(
        planilha_historicoPM[planilha_historicoPM['Date'] == linha['Date']]['Preço Médio'].unique()[0])
    # obtem o valor em R$(BRL) da conversão
    valorBrl = qtd_moeda_original * cotacao_moeda_original
    # pega a quantidade de cripto convertida
    qtd_moeda_obtida = float(linha['Buy'].split()[0])
    # calcula a cotação da cripto em R$(BRL)
    cotacao_moeda_obtida = valorBrl / qtd_moeda_obtida
    # calcula o novo PM e QTD
    calcularPrecoMedio(cripto, cotacao_moeda_obtida,
                       float(linha['Buy'].split()[0]))
    # atualiza na planilha o PM da moeda original
    planilha_cripto_analisada.at[idx, 'PM Cripto Original'] = str(
        cotacao_moeda_original) + ' ' + moeda


cripto = criptomoeda(args.cripto.upper())

# print(cripto)

for idx, row in planilha_cripto_analisada.iterrows():  # varre a tabela para atualizar o PM e QTD
    if row['Type'] == 'Compra':  # verifica se eh uma compra
        # calcula o novo PM, nova QTD e atualiza a planilha
        calcularPrecoMedio(cripto, float(
            row['Price'].split()[0]), float(row['Final Amount'].split()[0]))

    elif row['Type'] == 'Venda':  # verifica se eh uma venda

        # subtrai a QTD vendida
        cripto.quantidade -= float(row['Amount'].split()[0])

        atualizaPlanilha(cripto, cripto.precoMedio,
                         cripto.quantidade)  # atualiza a planilha

    elif row['Type'] == 'Conversao':  # verifica se eh uma conversao
        # verifica se esta convertendo BRL na cripto desejada
        if row['Sell'].split()[1] == 'BRL' and row['Buy'].split()[1] == cripto.nome:
            # calcula o novo PM, nova QTD e atualiza a planilha
            calcularPrecoMedio(cripto, float(
                row['Inverse Price'].split()[3]), float(row['Buy'].split()[0]))

        # verifica se está convertendo de USDT para a cripto desejada
        elif row['Sell'].split()[1] == 'USDT' and row['Buy'].split()[1] == cripto.nome:
            calculaPMConversao('USDT', planilha_USDT, row)

            # verifica se está convertendo de LTC para a cripto desejada
        elif row['Sell'].split()[1] == 'LTC' and row['Buy'].split()[1] == cripto.nome:
            calculaPMConversao('LTC', planilha_LTC, row)

        # verifica se está convertendo de BTC para a cripto desejada
        elif row['Sell'].split()[1] == 'BTC' and row['Buy'].split()[1] == cripto.nome:
            calculaPMConversao('BTC', planilha_BTC, row)

        # caso seja uma conversao da cripto analisada para outro moeda
        elif row['Sell'].split()[1] == cripto:
            # subtrai a QTD vendida
            cripto.quantidade -= float(row['Sell'].split()[0])
            atualizaPlanilha(cripto, cripto.precoMedio,
                             cripto.quantidade)  # atualiza a planilha
        else:
            print('Faltam dados para o caso: ' + str(idx))
    else:
        print('Tipo de transação não identificada no ID: ' + str(idx))

planilha_output_nome = 'output-' + cripto.nome.upper() + '-PM.csv'

planilha_cripto_analisada.to_csv(planilha_output_nome)
