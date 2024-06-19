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

## Visualização de Dados:

- Calcula a média das avaliações para cada uma das marcas filtradas.
- Cria um gráfico de barras utilizando Matplotlib para mostrar as médias de avaliações das marcas AOC, Samsung e LG.

## Requisitos 

- Python
- Selenium: Para automação de navegação web.
- Pandas: Para manipulação e análise de dados.
- Matplotlib: Para geração de gráficos.

## Como Usar

## 1 Configuração do Ambiente:

Instale as bibliotecas necessárias executando o comando:
```
pip install -r requirements.txt
```
Certifique-se de ter o driver do navegador Chrome instalado e acessível no PATH (caso use Chrome).

## 2 Execução do selenium_script.py:

- Execute o script Python selenium_script.py para iniciar o scraping de dados da Amazon.
- Este script solicitará um termo de pesquisa (exemplo: "Monitor") para iniciar a busca no site da Amazon.
- Os resultados serão salvos em um arquivo amazon_products.csv.

## 3 Execução do show_graphic.py:

- Após executar selenium_script.py e gerar o arquivo CSV, execute o script Python show_graphic.py.
- Este script lerá os dados salvos no amazon_products.csv, calculará as médias de avaliações das marcas AOC, Samsung e LG (opcional) e gerará um gráfico de barras mostrando essas médias.
