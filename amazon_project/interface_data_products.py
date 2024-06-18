from tkinter import *

def search_product():
    produto = entry.get()
    if produto:
        status_label.config(text=f"Produto pesquisado: {produto}")
        return produto
    else:
        status_label.config(text="Nenhum produto inserido")
        return None

root = Tk()
root.title("Busca por produtos na Amazon")
root.geometry("400x700")

Label(root, text="Pesquisar por produtos na Amazon", font=("Helvetica", 14)).pack(pady=10)

entry = Entry(root, width=30)
entry.pack(pady=30)

btn_search = Button(root, text="Pesquisar", command=search_product)
btn_search.pack()

status_label = Label(root, text="", font=("Helvetica", 12))
status_label.pack(pady=20)

root.mainloop()
