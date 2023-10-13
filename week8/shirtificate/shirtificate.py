from fpdf import FPDF

class PDF(FPDF):

    def header(self):
        #add image
        self.image("shirtificate.png", 10, 70, 180, 180)

        #add font
        self.set_font("helvetica", "B", 50)

        #add text
        self.text(45, 45, "CS50 Shirtificate")

    def footer(self):
        #set font
        self.set_font("helvetica", "B", 25)

        #set color to white
        self.set_text_color(255,255,255)

        #set text
        self.text(60, 120, name + " took CS50")


name = input("Name: ")
pdf = PDF() #original is orientation = portait and format = A4
pdf.add_page()
pdf.output("shirtificate.pdf")