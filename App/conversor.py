import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.input = tk.StringVar()
        self.resultado_var = tk.StringVar()
        self.window()
        self.interface()

    def window(self):
        self.root.title("Conversor")
        self.root.geometry("720x480")

    def interface(self):
        entry = tk.Entry(self.root, textvariable=self.input)
        entry.pack(padx=10, pady=60)

        button = tk.Button(self.root,
                            text="Converter",
                              command=self.calculo
                              )
        button.pack(pady=20)

        resultado_label = tk.Label(self.root,
                                    textvariable=self.resultado_var,
                                    font=("Arial",23,"bold"),
                                    )
        resultado_label.pack(pady=10)

    def calculo(self):
        try:
            valor = int(self.input.get())
            binario_convertido = bin(valor)[2:]
            self.resultado_var.set(f'{binario_convertido}')
        except ValueError:
            self.resultado_var.set('Digite um valor inteiro válido')

if __name__ == "__main__":
    start = App()
    start.root.mainloop()
else:
    print("Algo está errado")