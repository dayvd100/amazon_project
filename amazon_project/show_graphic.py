import pandas as pd
import matplotlib.pyplot as plt

def read_and_filter_csv(filename):
    try:
        df = pd.read_csv(filename, encoding='utf-8')
        brands = ["AOC", "Samsung", "LG"]
        pattern = '|'.join(brands)
        filtered_df = df[df['Product Name'].str.contains(pattern, case=False, na=False)]
        return filtered_df
    except FileNotFoundError:
        print(f"O arquivo {filename} não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler ou filtrar o arquivo: {str(e)}")
        return None

def calculate_and_plot_mean_ratings(df):
    try:
        df['Rating'] = pd.to_numeric(df['Rating'].str.replace(',', '.'), errors='coerce')

        df = df.dropna(subset=['Rating'])

        df['Brand'] = df['Product Name'].apply(lambda x: 'Samsung' if 'Samsung' in x else 'LG' if 'LG' in x else 'AOC')

        mean_ratings = df.groupby('Brand')['Rating'].mean().reset_index()

        plt.figure(figsize=(10, 6))
        bars = plt.bar(mean_ratings['Brand'], mean_ratings['Rating'], color=['red', 'gray', 'blue'])
        plt.xlabel('Marcas')
        plt.ylabel('Média de avaliações')
        plt.title('Média de avaliações de Monitores AOC, Samsung e LG')

        plt.ylim(0, 5)

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 2), ha='center', va='bottom')

        plt.show()
    except Exception as e:
        print(f"Ocorreu um erro ao calcular as médias ou criar o gráfico: {str(e)}")

filtered_df = read_and_filter_csv("amazon_products.csv")

if filtered_df is not None:
    calculate_and_plot_mean_ratings(filtered_df)
