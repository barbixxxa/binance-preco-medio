# Binance Preço Médio
Script em python que calcula o preço médio da criptomoeda desejada através das planilhas de histórico da binance

[![python](https://img.shields.io/badge/python-3.8-blue)](https://github.com/barbixxxa/binance-preco-medio/)

Baixar histórico de ordens de compra, venda e conversão na Binance [Gerar histórico](https://www.binance.com/pt-BR/support/faq/como-gerar-o-hist%C3%B3rico-de-transa%C3%A7%C3%B5es-990afa0a0a9341f78e7a9298a9575163)

## Dependências

1. [Pandas](https://pypi.org/project/pandas/) - `pip install pandas` or `conda install pandas`
2. [Argparse](https://pypi.org/project/argparse/) - `pip install argparse`

## Como executar
1. Baixe as planilhas de histórico de compra,venda,conversão do site da binance
2. Insira os dados das planilhas de histórico baixadas na [planilha exemplo](https://github.com/barbixxxa/binance-preco-medio/blob/main/planilha_exemplo.csv). Tal planilha já possui todas as colunas necessárias para a execução do script, deve-se preencher com os dados de compra, venda, conversão de apenas uma única criptomoeda
3. Caso a moeda que deseja calcular o PM tenha sido comprada (convertida) com outra criptomoeda:
   - Deve-se primeiro calcular o PM da criptomoeda utilizada para adquirir. Por exemplo: Quero calcular o PM das minhas transações para BTC, que comprei com BRL e convertendo USDT -> BTC. Para poder calcular o PM em BTC, preciso primeiro calcular o PM de USDT para que o script acesse esses dados e gere a planilha completa do BTC
   - Modifique no script as linhas (9:11) para inserir
4. Coloque a planilha gerada no passo nº 2 na mesma pasta do [script](https://github.com/barbixxxa/binance-preco-medio/blob/main/binance-PM.py)
5. Execute o seguinte comando informando o nome da criptomoeda que deseja calcular o PM

`./binance-PM.py [-h] nomeCriptoMoeda`

Exemplo: `./binance-PM.py btc`

## Melhorias a serem feitas

- [ ] Inserir dados do binance earn


## Bugs

- [ ] 
