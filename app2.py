
# Consolidated Python Script for Flask Application

# Imports from the standard library
import os

# Imports from installed packages
from flask import Flask, render_template, request, send_file
from fpdf import FPDF

# Core Application Logic from app.py
from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

# Function to perform calculations based on Excel data
def calculate_cost(consumo_kwh, valor_energia, techo, almacenamiento):
    # Data directly from Excel
    price_per_kwh = 1153.846154  # COP
    avg_monthly_consumption = 3000  # kWh/month
    equivalent_power_kwp = 23.529412  # kWp needed
    num_panels = 36  # panels
    required_area = 117.647059  # m²
    project_cost = 110300778  # COP
    estimated_savings = 41538461.54  # COP/year
    roi = "Entre 2 y 3 años"  # ROI based on project cost and savings
    co2_avoided = 20.524576  # tons/year
    trees_planted = 52.153475  # trees/year equivalent

    # Return the results as a dictionary
    return {
        "price_per_kwh": price_per_kwh,
        "avg_monthly_consumption": avg_monthly_consumption,
        "equivalent_power_kwp": equivalent_power_kwp,
        "num_panels": num_panels,
        "required_area": required_area,
        "project_cost": project_cost,
        "estimated_savings": estimated_savings,
        "roi": roi,
        "co2_avoided": co2_avoided,
        "trees_planted": trees_planted,
    }

# PDF generation class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'COLIBRI ', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 10, 'Propuesta Sistema Solar Offgrid', 0, 1, 'C')
        self.cell(0, 10, 'OFERTA:__________', 0, 1, 'C')
        self.ln(10)

    def footer(self):
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

    def add_costs(self, calculation_results):
        self.add_title('Detalle de costos')
        self.add_paragraph(f"Potencia del sistema: {calculation_results['equivalent_power_kwp']:.2f} kWp")
        self.add_paragraph(f"Costo total: ${calculation_results['project_cost']:,.2f}")
        self.add_paragraph(f"Ahorros anuales estimados: ${calculation_results['estimated_savings']:,.2f}")
        self.add_paragraph(f"Retorno de Inversión: {calculation_results['roi']}")
        self.add_paragraph(f"Ahorro Emisiones CO2: {calculation_results['co2_avoided']:.2f} toneladas")
        self.add_paragraph(f"Árboles equivalentes plantados: {calculation_results['trees_planted']:.2f} árboles/año")

def create_pdf(calculation_results):
    pdf = PDF()
    pdf.add_page()

    pdf.add_title('Detalles del Sisetma')
    pdf.add_paragraph(f"Número de Páneles solares: {calculation_results['num_panels']}")
    pdf.add_paragraph(f"Área requerida: {calculation_results['required_area']:.2f} m²")
    pdf.add_paragraph(f"Precio por kWh: {calculation_results['price_per_kwh']:.2f} COP")

    pdf.add_costs(calculation_results)

    pdf.output('Propuesta solar COLIBRI.pdf')
    print("PDF creado exitosamente!")

#@app.route('/Cotizador/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        consumo_kwh = float(request.form['consumo_kwh'])
        valor_energia = float(request.form['valor_energia'])
        techo = request.form['techo']
        almacenamiento = request.form['almacenamiento']

        # Perform calculations
        calculation_results = calculate_cost(consumo_kwh, valor_energia, techo, almacenamiento)
        
        # Create PDF
        create_pdf(calculation_results)
        return send_file('Propuesta solar COLIBRI.pdf', as_attachment=True)
    
    except KeyError as e:
        return f"Faltan datos para: {e.args[0]}", 400

if __name__ == '__main__':

    app.run(port=8000, debug=True)


# Utility Functions from calculator.py
def calculate_cost(kwh_per_month):
    # System size in kWp (this is a simple calculation based on kWh)
    system_size = kwh_per_month / 150  # Assuming 150 kWh per kWp

    # Cost per kWp
    cost_per_kwp = 6443000  # Example cost in your currency

    # Total cost
    total_cost = system_size * cost_per_kwp

    # Add VAT (12%)
    vat = total_cost * 0.12

    # Final total
    final_total = total_cost + vat

    return system_size, total_cost, vat, final_total

# Example usage
kwh_per_month = float(input("Ingrese su consumo total en kWh: "))
system_size, total_cost, vat, final_total = calculate_cost(kwh_per_month)

print(f"System Size: {system_size:.2f} kWp")
print(f"Total Cost: {total_cost:.2f}")
print(f"VAT: {vat:.2f}")
print(f"Final Total: {final_total:.2f}")


# PDF Generation Logic from create_proposal.py
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



# Running the Flask Application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
