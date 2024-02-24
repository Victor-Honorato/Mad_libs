import tkinter as tk
import random


class MadLibsGame(tk.Toplevel):
    def __init__(self, master):
        # Inicialização da janela do jogo Mad Libs
        super().__init__(master)
        self.title("Mad Libs Game")
        self.geometry("500x400")

        # Listas de palavras para o jogo
        self.substantivos = ["cachorro", "gato", "elefante", "pássaro", "computador", "bolo"]
        self.verbos = ["corre", "pula", "come", "dorme", "dança", "canta"]
        self.adverbios = ["rapidamente", "silenciosamente", "felizmente", "tristemente", "constantemente"]
        self.adjetivos = ["grande", "pequeno", "colorido", "ruidoso", "alegre", "surpreso"]
        self.lugares = ["parque", "praia", "montanha", "cidade", "floresta", "escola"]

        # Variáveis para armazenar as palavras escolhidas
        self.substantivo_escolhido = tk.StringVar()
        self.verbo_escolhido = tk.StringVar()
        self.adverbio_escolhido = tk.StringVar()
        self.adjetivo_escolhido = tk.StringVar()
        self.lugar_escolhido = tk.StringVar()

        # Criação dos widgets da interface
        self.create_widgets()

    def create_widgets(self):
        # Criação dos rótulos e campos de entrada
        tk.Label(self, text="Complete a história:", font=("Arial", 16)).pack(pady=10)

        self.story_label = tk.Label(self, text="", font=("Arial", 14), wraplength=400)
        self.story_label.pack(pady=10)

        self.create_entry("Substantivo", self.substantivo_escolhido)
        self.create_entry("Verbo", self.verbo_escolhido)
        self.create_entry("Advérbio", self.adverbio_escolhido)
        self.create_entry("Adjetivo", self.adjetivo_escolhido)
        self.create_entry("Lugar", self.lugar_escolhido)

        # Botão para jogar
        tk.Button(self, text="Jogar", command=self.play_mad_libs, font=("Arial", 14)).pack(pady=10)

    def create_entry(self, label_text, text_variable):
        # Função auxiliar para criar rótulos e campos de entrada
        frame = tk.Frame(self)
        frame.pack(pady=5)

        tk.Label(frame, text=label_text, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
        tk.Entry(frame, textvariable=text_variable, font=("Arial", 12), width=20).pack(side=tk.LEFT)

    def play_mad_libs(self):
        # Função para gerar e exibir a história completada
        substantivo = random.choice(self.substantivos)
        verbo = random.choice(self.verbos)
        adverbio = random.choice(self.adverbios)
        adjetivo = random.choice(self.adjetivos)
        lugar = random.choice(self.lugares)

        historia = f"Num {adjetivo} dia, um {substantivo} {verbo} {adverbio} em um {lugar}."
        self.story_label.config(text=historia)

        resposta_substantivo = self.substantivo_escolhido.get()
        resposta_verbo = self.verbo_escolhido.get()
        resposta_adverbio = self.adverbio_escolhido.get()
        resposta_adjetivo = self.adjetivo_escolhido.get()
        resposta_lugar = self.lugar_escolhido.get()

        if resposta_substantivo and resposta_verbo and resposta_adverbio and resposta_adjetivo and resposta_lugar:
            historia_preenchida = f"Num {resposta_adjetivo} dia, um {resposta_substantivo} {resposta_verbo} {resposta_adverbio} em um {resposta_lugar}."
            self.story_label.config(text=f"\nHistória Completa:\n{historia_preenchida}")
        else:
            tk.messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")
