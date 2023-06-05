import tkinter as tk
from tkinter import messagebox
import random
import turtle

def enviar_pedido(resposta):
    if resposta == "Sim":
        messagebox.showinfo("Pedido de Namoro - VPDev", "Pedido aceito! Eu te amo!")
        janela.destroy()

        pen = turtle.Turtle()

        def curve():
            for i in range(200):
                pen.right(1)
                pen.forward(1)

        def heart():
            pen.fillcolor('red')
            pen.begin_fill()
            pen.left(140)
            pen.forward(113)
            curve()
            pen.left(120)
            curve()
            pen.forward(112)
            pen.end_fill()

        def txt():
            pen.up()
            pen.setpos(-68, 95)
            pen.down()
            pen.color('white')
            pen.write("Eu te amo, meu amor!", font=("Verdana", 8, "bold"))

        window = turtle.Screen()
        window.bgcolor("white")
        pen.color('red')
        pen.begin_fill()
        heart()
        pen.end_fill()
        txt()
        pen.ht()
        turtle.done()


def mover_botao_nao(event):
    x1 = botao_nao.winfo_width() // 2
    y1 = botao_nao.winfo_height() // 2
    x2 = janela.winfo_width() - botao_nao.winfo_width() // 2
    y2 = janela.winfo_height() - botao_nao.winfo_height() // 2
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    botao_nao.place(x=x, y=y)

# Criar a janela principal
janela = tk.Tk()
janela.title("Pedido de Namoro")
janela.resizable(False, False)

# Criar canvas
canvas = tk.Canvas(janela, width=400, height=300)
canvas.pack()

# Criar degradê rosa
cor_inicio = "#FFB6C1"
cor_fim = "#FF69B4"
canvas.create_rectangle(0, 0, 400, 150, fill=cor_inicio, width=0)
for i in range(150, 300):
    cor = '#{:02x}{:02x}{:02x}'.format(int((1 - (i - 150) / 150) * int(cor_inicio[1:3], 16) + (i - 150) / 150 * int(cor_fim[1:3], 16)),
                                       int((1 - (i - 150) / 150) * int(cor_inicio[3:5], 16) + (i - 150) / 150 * int(cor_fim[3:5], 16)),
                                       int((1 - (i - 150) / 150) * int(cor_inicio[5:7], 16) + (i - 150) / 150 * int(cor_fim[5:7], 16)))
    canvas.create_line(0, i, 400, i, fill=cor)

# Criar rótulo
rotulo = tk.Label(janela, text="Você aceita namorar comigo?", font=("Arial", 16, "bold"), fg="white", bg=cor_fim)
rotulo.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Criar botões
botao_sim = tk.Button(janela, text="Sim", font=("Arial", 12, "bold"), bg=cor_inicio, fg="white", command=lambda: enviar_pedido("Sim"))
botao_sim.place(relx=0.35, rely=0.6, anchor=tk.CENTER)

botao_nao = tk.Button(janela, text="Não", font=("Arial", 12, "bold"), bg=cor_inicio, fg="white")
botao_nao.place(relx=0.65, rely=0.6, anchor=tk.CENTER)
botao_nao.bind("<Enter>", mover_botao_nao)

# Executar janela principal
janela.mainloop()
