import tkinter as tk
from instructions_page import InstructionsPage

class MainMenu(tk.Frame):
    def __init__(self, master, play_callback, instructions_callback):
        # Inicialização do menu principal
        super().__init__(master)
        self.master = master
        self.play_callback = play_callback
        self.instructions_callback = instructions_callback

        # Configuração do estilo do menu
        self.configure(bg="#f0f0f0")
        self.pack(fill=tk.BOTH, expand=True)

        # Adição de widgets ao menu
        self.create_widgets()

    def create_widgets(self):
        # Título do jogo
        title_label = tk.Label(self, text="Mad Libs", font=("Arial", 24), bg="#f0f0f0")
        title_label.pack(pady=30)

        # Botão para jogar
        play_button = tk.Button(self, text="Jogar", command=self.play_callback, font=("Arial", 16))
        play_button.pack(pady=10)

        # Botão para ver as instruções
        instructions_button = tk.Button(self, text="Instruções", command=self.show_instructions, font=("Arial", 16))
        instructions_button.pack(pady=10)

        # Botão para sair
        quit_button = tk.Button(self, text="Sair", command=self.master.destroy, font=("Arial", 16))
        quit_button.pack(pady=10)

    def show_instructions(self):
        # Função para exibir a janela de instruções
        self.instructions_callback()
