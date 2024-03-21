import tkinter as tk
from tkinter import ttk, messagebox
import ctypes


def abrir_janela_calculo():
    # Obter as dimensões do monitor
    largura_monitor = ctypes.windll.user32.GetSystemMetrics(0)
    altura_monitor = ctypes.windll.user32.GetSystemMetrics(1)

    # Calcular as coordenadas para a próxima janela
    largura_janela_calculo = 400
    altura_janela_calculo = 500
    margem_deslocamento = 50  # Ajuste a margem de deslocamento conforme necessário
    x_janela_calculo = (largura_monitor - largura_janela_calculo) // 2 + margem_deslocamento
    y_janela_calculo = (altura_monitor - altura_janela_calculo) // 2 + margem_deslocamento

    janela_calculo = tk.Toplevel(root)
    janela_calculo.title("Calcular porcentagem - Pirestech")
    janela_calculo.geometry(f"{largura_janela_calculo}x{altura_janela_calculo}+{x_janela_calculo}+{y_janela_calculo}")
    janela_calculo.grab_set()  # Definir janela de cálculo como modal
        
    def formatar_dinheiro(event):
        campo = event.widget
        valor = campo.get()
        if valor.isdigit():
            valor = f"R$ {int(valor):,},00"
        campo.delete(0, tk.END)
        campo.insert(0, valor)

    def calcular_planilha():
        # Forçar a perda de foco dos campos de entrada para garantir a formatação
        root.focus()

        try:
            custo_total = float(entrada_custo_total.get().replace('R$ ', '').replace('.', '').replace(',', '.'))
            quantidade_produtos = int(entrada_quantidade_produtos.get())
            valor_venda = float(entrada_valor_venda.get().replace('R$ ', '').replace('.', '').replace(',', '.'))
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
            return

        valor_unitario = custo_total / quantidade_produtos
        lucro_por_produto = valor_venda - valor_unitario
        lucro_total = lucro_por_produto * quantidade_produtos
        lucro_percentual = (lucro_total / custo_total) * 100

        # Formatando os valores em dinheiro com ","
        valor_unitario_formatado = f"{valor_unitario:,.2f}".replace('.', ',')
        lucro_por_produto_formatado = f"{lucro_por_produto:,.2f}".replace('.', ',')
        lucro_total_formatado = f"{lucro_total:,.2f}".replace('.', ',')
        lucro_percentual_formatado = f"{lucro_percentual:,.2f}".replace('.', ',')

        custo_por_produto_label.config(text=f"Valor de Custo por Produto: R$ {valor_unitario_formatado}")
        lucro_por_produto_label.config(text=f"Lucro por Produto: R$ {lucro_por_produto_formatado}")
        lucro_total_label.config(text=f"Lucro Total: R$ {lucro_total_formatado}")
        lucro_percentual_label.config(text=f"Lucro Total (%): {lucro_percentual_formatado}%")

    # Criar e posicionar os rótulos e entradas de texto
    tk.Label(janela_calculo, text="Custo Total (R$):").place(x=30, y=50)
    entrada_custo_total = ttk.Entry(janela_calculo)
    entrada_custo_total.place(x=240, y=50)
    entrada_custo_total.bind("<FocusOut>", formatar_dinheiro)  # vincular evento de saída do campo

    tk.Label(janela_calculo, text="Quantidade de Produtos:").place(x=30, y=80)
    entrada_quantidade_produtos = tk.Entry(janela_calculo)
    entrada_quantidade_produtos.place(x=240, y=80)

    tk.Label(janela_calculo, text="Valor de Venda por Produto (R$):").place(x=30, y=110)
    entrada_valor_venda = ttk.Entry(janela_calculo)
    entrada_valor_venda.place(x=240, y=110)
    entrada_valor_venda.bind("<FocusOut>", formatar_dinheiro)  # vincular evento de saída do campo

    custo_por_produto_label = tk.Label(janela_calculo, text="")
    custo_por_produto_label.place(x=30, y=210)

    lucro_por_produto_label = tk.Label(janela_calculo, text="")
    lucro_por_produto_label.place(x=30, y=240)

    lucro_total_label = tk.Label(janela_calculo, text="")
    lucro_total_label.place(x=30, y=270)

    lucro_percentual_label = tk.Label(janela_calculo, text="")
    lucro_percentual_label.place(x=30, y=300)

    # Criar botão para calcular a planilha
    botao_calcular = tk.Button(janela_calculo, text="Calcular Lucro", command=calcular_planilha)
    botao_calcular.place(x=155, y=150)

def abrir_janela_calculo_qtd():
    # Obter as dimensões do monitor
    largura_monitor = ctypes.windll.user32.GetSystemMetrics(0)
    altura_monitor = ctypes.windll.user32.GetSystemMetrics(1)

    # Calcular as coordenadas para a próxima janela
    largura_janela_calculo_qtd = 450
    altura_janela_calculo_qtd = 350
    margem_deslocamento = 50  # Ajuste a margem de deslocamento conforme necessário
    x_janela_calculo_qtd = (largura_monitor - largura_janela_calculo_qtd) // 2 + margem_deslocamento
    y_janela_calculo_qtd = (altura_monitor - altura_janela_calculo_qtd) // 2 + margem_deslocamento

    janela_calculo_qtd = tk.Toplevel(root)
    janela_calculo_qtd.title("Calcular Valor - Pirestech")
    janela_calculo_qtd.geometry(f"{largura_janela_calculo_qtd}x{altura_janela_calculo_qtd}+{x_janela_calculo_qtd}+{y_janela_calculo_qtd}")
    janela_calculo_qtd.grab_set()  # Definir janela de cálculo como modal

    def formatar_dinheiro(event):
        campo = event.widget
        valor = campo.get()
        if valor.isdigit():
            valor = f"R$ {int(valor):,},00"
        campo.delete(0, tk.END)
        campo.insert(0, valor)

    def calcular_valor_venda():
        # Forçar a perda de foco dos campos de entrada para garantir a formatação
        root.focus()

        try:
            custo_total = float(entrada_custo_total.get().replace('R$ ', '').replace('.', '').replace(',', '.'))
            quantidade_produtos = int(entrada_quantidade_produtos.get())
            custo_unitario = custo_total / quantidade_produtos
            lucro_percentual = float(entrada_lucro_percentual.get())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
            return

        valor_venda = custo_unitario * (1 + lucro_percentual / 100)

        resultado_label.config(text=f"Para receber o lucro de {lucro_percentual}% você deverá vender seu produto a R$ {valor_venda:,.2f}")

    # Criar e posicionar os rótulos e entradas de texto
    tk.Label(janela_calculo_qtd, text="Custo Total (R$):").place(x=60, y=50)
    entrada_custo_total = ttk.Entry(janela_calculo_qtd)
    entrada_custo_total.place(x=260, y=50)
    entrada_custo_total.bind("<FocusOut>", formatar_dinheiro)  # vincular evento de saída do campo

    tk.Label(janela_calculo_qtd, text="Quantidade de Produtos:").place(x=60, y=80)
    entrada_quantidade_produtos = tk.Entry(janela_calculo_qtd)
    entrada_quantidade_produtos.place(x=260, y=80)

    tk.Label(janela_calculo_qtd, text="Porcentagem de Lucro (%):").place(x=60, y=110)
    entrada_lucro_percentual = tk.Entry(janela_calculo_qtd)
    entrada_lucro_percentual.place(x=260, y=110)

    resultado_label = tk.Label(janela_calculo_qtd, text="")
    resultado_label.place(x=25, y=250)

    # Criar botão para calcular o valor de venda
    botao_calcular = tk.Button(janela_calculo_qtd, text="Calcular Valor de Venda", command=calcular_valor_venda)
    botao_calcular.place(x=160, y=170)

# Obter as dimensões do monitor
largura_monitor = ctypes.windll.user32.GetSystemMetrics(0)
altura_monitor = ctypes.windll.user32.GetSystemMetrics(1)

# Calcular as coordenadas para centralizar a janela principal
largura_janela = 400
altura_janela = 300
x_janela = (largura_monitor - largura_janela) // 2
y_janela = (altura_monitor - altura_janela) // 2

# Criar a interface gráfica principal
root = tk.Tk()
root.title("Janela Principal - Pirestech")
root.geometry(f"{largura_janela}x{altura_janela}+{x_janela}+{y_janela}")  # Definir o tamanho e posição da janela


# Criar botões centralizados
botao_calcular_percentual = ttk.Button(root, text="Calcular porcentagem", command=abrir_janela_calculo)
botao_calcular_percentual.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

botao_calcular_quantidade = ttk.Button(root, text="Calcular Valor", command=abrir_janela_calculo_qtd)
botao_calcular_quantidade.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

root.mainloop()
