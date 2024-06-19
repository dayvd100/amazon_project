import tkinter as tk
from gui_script import create_gui_and_search
from selenium_script import search_amazon_product

def main():
    root = tk.Tk()
    root.title("Pesquisa de Produtos na Amazon")
    root.geometry("600x700")

    create_gui_and_search(root, search_amazon_product)

    root.mainloop()

if __name__ == "__main__":
    main()
