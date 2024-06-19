## Scraping e análise, coletando dados automaticamente


## descrição

Este projeto consiste em um web scraper desenvolvido em Python 
usando Selenium para buscar informações de produtos de monitores no site da Amazon Brasil 
e analisar as avaliações médias de três marcas específicas (AOC, Samsung e LG), você pode pesquisar por qualquer produto e marca, 
basta fazer algumas modificações no código. Além disso, 
gera um gráfico de barras das médias de avaliações dessas marcas.

## Funcionalidades 

- Utiliza Selenium para automatizar a busca de produtos no site da Amazon Brasil.
- Procura por produtos usando um termo de pesquisa especificado pelo usuário (exemplo: "Monitor").
- Extrai informações como nome do produto, preço e avaliação de cada produto encontrado.

## Análise de Dados:

- Salva os resultados do scraping em um arquivo CSV (amazon_products.csv), formatado com colunas para nome do produto, preço e avaliação.
- Utiliza Pandas para ler e filtrar os dados do arquivo CSV, focando apenas nos produtos das marcas AOC, Samsung e LG.
