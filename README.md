# Binance Preço Médio
Script em python que calcula o preço médio da criptomoeda desejada através das planilhas de histórico da binance

[![python](https://img.shields.io/badge/python-3.8-blue)](https://github.com/barbixxxa/binance-preco-medio/)

Baixar histórico de ordens de compra, venda e conversão na Binance [Gerar histórico](https://www.binance.com/pt-BR/support/faq/como-gerar-o-hist%C3%B3rico-de-transa%C3%A7%C3%B5es-990afa0a0a9341f78e7a9298a9575163)

## Dependências

1. [Pandas](https://pypi.org/project/pandas/) - `pip install pandas` ou `conda install pandas`
2. [Argparse](https://pypi.org/project/argparse/) - `pip install argparse`

## Como executar
1. Baixe as planilhas de histórico de compra,venda,conversão do site da binance
2. Insira os dados das planilhas de histórico baixadas na [planilha exemplo](https://github.com/barbixxxa/binance-preco-medio/blob/main/planilha_exemplo.csv). Tal planilha já possui todas as colunas necessárias para a execução do script, deve-se preencher com os dados de compra, venda, conversão de apenas uma única criptomoeda
3. Caso a moeda que deseja calcular o PM tenha sido comprada (convertida) com outra criptomoeda:
   - Deve-se primeiro calcular o PM da criptomoeda utilizada para adquirir. Por exemplo: Quero calcular o PM das minhas transações para BTC, que comprei com BRL e convertendo USDT -> BTC. Para poder calcular o PM em BTC, preciso primeiro calcular o PM de USDT para que o script acesse esses dados e gere a planilha completa do BTC
4. Coloque a planilha gerada no passo nº 2, e as demais necessárias caso o passo nº seja verdadeiro, na mesma pasta do [script](https://github.com/barbixxxa/binance-preco-medio/blob/main/binance-PM.py)
5. Execute o seguinte comando informando o nome da criptomoeda que deseja calcular o PM e as planilhas necessárias:

`python3 binance-PM.py eth planilha_ETH.csv --planilhaUSDT planilha_USDT.csv --planilhaBTC planilha_BTC.csv`


### `python3 binance-PM.py -h`
```
usage: binance-PM.py [-h] [--planilhaUSDT PLANILHAUSDT] [--planilhaLTC PLANILHALTC] [--planilhaBTC PLANILHABTC] cripto planilha_cripto

positional arguments:
  cripto                Nome da criptomoeda a ser calculada. Ex: BTC
  planilha_cripto       Nome da planilha contendo os dados de histórico de transações da criptomoeda. Ex: historico_btc.csv

optional arguments:
  -h, --help            show this help message and exit
  --planilhaUSDT PLANILHAUSDT
                        Nome da planilha contendo os dados de histórico de transações USDT. Ex: historico_usdt.csv
  --planilhaLTC PLANILHALTC
                        Nome da planilha contendo os dados de histórico de transações LTC. Ex: historico_ltc.csv
  --planilhaBTC PLANILHABTC
                        Nome da planilha contendo os dados de histórico de transações BTC. Ex: historico_btc.csv
```




## Melhorias a serem feitas

- [ ] Inserir dados do binance earn
- [ ] Puxar automaticamente moedas dependentes


## Bugs

- [ ] 
