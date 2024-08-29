from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Add company header
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'COLIBRI ENERGIA SOLAR', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 10, 'Propuesta Sistema Solar Offgrid', 0, 1, 'C')
        self.cell(0, 10, 'OFERTA: ', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        # Add a footer with contact details
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Contacto: Germán Ballesteros | +57 301 5816474', 0, 0, 'C')

    def add_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def add_paragraph(self, text):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, text)
        self.ln(4)

    def add_costs(self, system_size, total_cost, vat, final_total):
        self.add_title('Cost Breakdown')
        self.add_paragraph(f"System Size: {system_size:.2f} kWp")
        self.add_paragraph(f"Total Cost: ${total_cost:,.2f}")
        self.add_paragraph(f"VAT: ${vat:,.2f}")
        self.add_paragraph(f"Final Total: ${final_total:,.2f}")

def create_pdf(system_size, total_cost, vat, final_total):
    pdf = PDF()
    pdf.add_page()

    # System Information
    pdf.add_title('System Details')
    pdf.add_paragraph(f"Tamaño del sistema: {system_size:.2f} kWp")
    pdf.add_paragraph(f"Producción total de energía: 2,031 kWh/mes")

    # Cost Breakdown
    pdf.add_costs(system_size, total_cost, vat, final_total)

    # Warranties and ROI
    pdf.add_title('Warranties')
    pdf.add_paragraph('Paneles solares: Garantía de producto de 15 años.')
    pdf.add_paragraph('Retorno de Inversión: 4 años')

    # Save the PDF
    pdf.output('Propuesta Energia solar COLIBRI.pdf')
    print("pdf Creado exitosamente!")

# Example usage:
system_size = 15.93
total_cost = 103092360
vat = 12180368
final_total = 115273328

create_pdf(system_size, total_cost, vat, final_total)

