from fpdf import FPDF


def creoPDF():
    pdf=FPDF()
    pdf.add_page()
    pdf.set_margins(10,10)
    pdf.set_font("Arial","B",20)
    pdf.cell(50,50,"Cotización",align="center")


    pdf.set_xy(0, 0)                                                    # define abscisa y  ordinate, posicion actual. Si el valor es nagativo empieza por abajo

    pdf.set_font('arial', 'B', 12)                                      # arial 12 en negrita

    pdf.cell(60)                                                        # posicion texto

    pdf.cell(90, 10, " ", 0, 2, 'C')  
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')                                  # celda vacia, como salto de linea

    pdf.image('cotizacion.png', x=50, y=50, w=100, h=100, type = '', link = '') # imagen 

    pdf.output("Proyecto.pdf","F")                                          # guardado del pdf
