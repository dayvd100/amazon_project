from tkinter import *

def search_product(entry, status_label):
    produto = entry.get()
    if produto:
        status_label.config(text=f"Produto pesquisado: {produto}")
        return produto
    else:
        status_label.config(text="Nenhum produto inserido")
        return None

def main():
    root = Tk()
    root.title("Busca por produtos na Amazon")
    root.geometry("400x700")

    Label(root, text="Pesquisar por produtos na Amazon", font=("Helvetica", 18)).pack(pady=10)

    entry = Entry(root, width=30)
    entry.pack(pady=30)

    status_label = Label(root, text="", font=("Helvetica", 12))
    status_label.pack(pady=20)

    def on_search():
        produto_pesquisado = search_product(entry, status_label)
        if produto_pesquisado:
            print(produto_pesquisado)

    btn_search = Button(root, text="Pesquisar", command=on_search)
    btn_search.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
