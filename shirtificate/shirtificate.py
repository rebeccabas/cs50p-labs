from fpdf import FPDF
import sys

class PDF(FPDF):
    def container(self,name):
        self.set_font("helvetica", "B", 20)
        self.cell(0, 20, "CS50 Shirtificate", align = "C")
        self.ln(20)
        self.image("shirtificate.png", x = 5, y = 70, w =200)
        self.set_font("helvetica", "B", 30)
        self.set_text_color(250,250,250)
        self.cell(0, 230, f"{name} took CS50", align = "C")


name = input("Name: ")
pdf = PDF()
pdf.add_page()
pdf.container(name)
pdf.output("shirtificate.pdf")
sys.exit()


