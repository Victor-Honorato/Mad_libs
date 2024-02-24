import tkinter as tk

class InstructionsPage(tk.Toplevel):
    def __init__(self, master):
        # Inicialização da janela de instruções
        super().__init__(master)
        self.title("Instruções")
        self.geometry("400x300")

        # Texto de instruções
        instructions_text = (
            "Bem-vindo ao jogo Mad Libs!\n\n"
            "Instruções:\n"
            "1. Clique em 'Jogar' para começar a preencher a história.\n"
            "2. Preencha os campos com palavras solicitadas (substantivo, verbo, etc.).\n"
            "3. Clique em 'Jogar' para gerar a história completada.\n\n"
            "Divirta-se!"
        )

        # Rótulo para exibir as instruções
        tk.Label(self, text=instructions_text, font=("Arial", 14), justify=tk.LEFT).pack(pady=20)

        # Botão para fechar a janela de instruções
        tk.Button(self, text="Fechar", command=self.destroy, font=("Arial", 12)).pack()

# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    InstructionsPage(root).mainloop()
