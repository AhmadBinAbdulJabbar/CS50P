from fpdf import FPDF



def main():
    name = input("Enter name: ").strip()


    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=30)
    pdf.cell(w=0, h=20, text='CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')

    pdf.image("./shirtificate.png", x="C", y=50, w= pdf.epw)

    pdf.set_font("helvetica", style="B", size=20)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(w=0, h=180, text=f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")




if __name__ == "__main__":
    main()

