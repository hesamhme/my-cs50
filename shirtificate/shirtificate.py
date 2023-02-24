from fpdf import FPDF

esm= input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(False)
pdf.add_page()
pdf.set_font("Times", "B", 30)
pdf.cell(w=0, h=30, txt="CS50 shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.image("./shirtificate.png", 15, 50, 180, 200)
pdf.set_font("Times", "B", 25)
pdf.set_text_color(255)
pdf.cell(w=0, h=150, txt=esm+" took CS50", align="C")

pdf.output("shirtificate.pdf")