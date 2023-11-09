from fpdf import FPDF

descricao = input("Digite a descrição do projeto: ")
horas_previstas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado em dias: ")

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

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso")