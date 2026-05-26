#dado
import tkinter as tk
import random

def jogar_dado():
    numero = random.randint(1, 7)
    label_resultado.config(text=f"🎲 Você tirou: {numero}")

# Criar janela principal
janela = tk.Tk()
janela.title("Jogo do Dado")

# Botão para jogar
botao = tk.Button(janela, text="Jogar Dado", command=jogar_dado, font=("Arial", 14))
botao.pack(pady=20)

# Label para mostrar resultado
label_resultado = tk.Label(janela, text="Clique para jogar!", font=("Arial", 16))
label_resultado.pack(pady=20)

# Loop da interface
janela.mainloop()

