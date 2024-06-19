from tkinter import *
from tkinter import messagebox

def create_gui_and_search(root, search_function):
    frame_input = Frame(root)
    frame_input.pack(pady=20)

    label_product = Label(frame_input, text="Nome do Produto:")
    label_product.pack(side=LEFT, padx=10)

    entry_product = Entry(frame_input, width=50)
    entry_product.pack(side=LEFT)

    def on_search():
        produto = entry_product.get().strip()
        if produto:
            results = search_function(produto)
            display_results(results)

    btn_search = Button(root, text="Pesquisar", command=on_search)
    btn_search.pack(pady=10)

    frame_results = Frame(root)
    frame_results.pack(pady=20)

    results_label = Label(frame_results, text="Resultados:")
    results_label.pack()

    results_text = Text(frame_results, width=80, height=15)
    results_text.pack()

    def clear_results():
        results_text.delete('1.0', END)

    btn_clear = Button(root, text="Limpar Resultados", command=clear_results)
    btn_clear.pack(pady=10)

    def display_results(results):
        clear_results()
        if results:
            for result in results:
                results_text.insert(END, result)

