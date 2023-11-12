import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.input = tk.StringVar()
        self.resultado_var = tk.StringVar()
        self.input2 = tk.StringVar() 
        self.resultado_var2 = tk.StringVar() 
        self.window()
        self.interface()

    def window(self):
        self.root.title("Conversor")
        self.root.geometry("720x480")

    def interface(self):
        texto_label2 = tk.Label(self.root,
                                text="Digite um valor inteiro",
                                font=("Arial", 23, "bold"))
        texto_label2.pack(pady=10)
        entry = tk.Entry(self.root, textvariable=self.input)
        entry.pack(padx=10, pady=10)

        button = tk.Button(self.root,
                            text="Converter",
                            command=self.calculo
                            )
        button.pack(pady=10)

        resultado_label = tk.Label(self.root,
                                   textvariable=self.resultado_var,
                                   font=("Arial", 23, "bold"),
                                   )
        resultado_label.pack(pady=10)

        texto_label2 = tk.Label(self.root,
                                text="Digite um valor binário",
                                font=("Arial", 23, "bold"))
        texto_label2.pack(pady=10)
        entry2 = tk.Entry(self.root, textvariable=self.input2)
        entry2.pack(padx=10, pady=10)

        button2 = tk.Button(self.root,
                             text="Converter",
                             command=self.calculo2
                             )
        button2.pack(pady=10)

        resultado_label2 = tk.Label(self.root,
                                    textvariable=self.resultado_var2,
                                    font=("Arial", 23, "bold"),
                                    )
        resultado_label2.pack(pady=10)

    def calculo(self):
        try:
            valor = int(self.input.get())
            binario_convertido = bin(valor)[2:]
            self.resultado_var.set(f'{binario_convertido}')
        except ValueError:
            self.resultado_var.set('Digite um valor inteiro válido')

    def calculo2(self):
        try:
            valor_binario = self.input2.get()
            inteiro_convertido = int(valor_binario, 2)
            self.resultado_var2.set(f'{inteiro_convertido}')
        except ValueError:
            self.resultado_var2.set('Digite um valor binário válido')

if __name__ == "__main__":
    start = App()
    start.root.mainloop()
