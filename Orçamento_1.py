from tkinter import *
from fpdf import FPDF
import webbrowser

def gerar_orcamento():
    descricao = entry_descricao.get()
    horas_previstas = entry_horas.get()
    valor_hora = entry_valor_hora.get().replace(",", ".")  # Substituir vírgulas por pontos
    prazo = entry_prazo.get()

    valor_total = float(horas_previstas) * float(valor_hora)

    # Gerando PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial")

    # coordenadas/ caminho do pdf
    pdf.image("template.png", x=0, y=0)
    pdf.text(115, 145, descricao)
    pdf.text(115, 160, horas_previstas)
    pdf.text(115, 175, valor_hora)
    pdf.text(115, 190, prazo)
    pdf.text(115, 205, str(valor_total))

    pdf_file_path = "Orçamento.pdf"
    pdf.output(pdf_file_path)
    print("Orçamento gerado com sucesso")

    # Abrir o arquivo no navegador
    webbrowser.open(pdf_file_path)

# Configurando a interface gráfica
root = Tk()
root.title("Gerador de Orçamento")

# Aumentando o tamanho da janela
root.geometry("600x400")

label_descricao = Label(root, text="Descrição do projeto:", font=("Arial", 12))
label_descricao.grid(row=0, column=0, pady=10, padx=10)
entry_descricao = Entry(root, font=("Arial", 12))
entry_descricao.grid(row=0, column=1, pady=10, padx=10)

label_horas = Label(root, text="Horas previstas:", font=("Arial", 12))
label_horas.grid(row=1, column=0, pady=10, padx=10)
entry_horas = Entry(root, font=("Arial", 12))
entry_horas.grid(row=1, column=1, pady=10, padx=10)

label_valor_hora = Label(root, text="Valor da hora trabalhada:", font=("Arial", 12))
label_valor_hora.grid(row=2, column=0, pady=10, padx=10)
entry_valor_hora = Entry(root, font=("Arial", 12))
entry_valor_hora.grid(row=2, column=1, pady=10, padx=10)

label_prazo = Label(root, text="Prazo estimado em dias:", font=("Arial", 12))
label_prazo.grid(row=3, column=0, pady=10, padx=10)
entry_prazo = Entry(root, font=("Arial", 12))
entry_prazo.grid(row=3, column=1, pady=10, padx=10)

button_gerar = Button(root, text="Gerar Orçamento", command=gerar_orcamento, font=("Arial", 12))
button_gerar.grid(row=4, columnspan=2, pady=20)

root.mainloop()
