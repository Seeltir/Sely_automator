import pandas as pd
from fpdf import FPDF
import customtkinter as ctk
from tkinter import filedialog
import os

def procesar_datos(archivo_excel):
    df = pd.read_excel(archivo_excel)
    df['Total'] = df['Cantidad'] * df['Precio']
    reporte = df.groupby('Cliente')['Total'].sum().reset_index()
    return reporte

class Factura(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 15)
        self.cell(0, 10, 'FACTURA COMERCIAL', 0, 1, 'C')

def generar_pdf(nombre_cliente, total):
    pdf = Factura()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.cell(200, 10, txt=f"Cliente: {nombre_cliente}", ln=1)
    pdf.cell(200, 10, txt=f"Monto Total a Pagar: ${total:.2f}", ln=2)
    pdf.output(f"Factura_{nombre_cliente}.pdf")

def iniciar_automatizacion():
    ruta = filedialog.askopenfilename(filetypes=[("Archivos de Excel", "*.xlsx *.xls")])
    
    if ruta:
        print(f"Leyendo el archivo: {ruta}")
        try:
            reporte = procesar_datos(ruta)
            
            for index, fila in reporte.iterrows():
                generar_pdf(fila['Cliente'], fila['Total'])
                
            print("¡Todas las facturas fueron creadas con éxito!")
        except Exception as e:
            print(f"Ups, algo salió mal al procesar: {e}")

app = ctk.CTk()
app.title("Sely-Automator v1.0")
app.geometry("400x200")

btn = ctk.CTkButton(app, text="Cargar Excel y Generar", command=iniciar_automatizacion)
btn.pack(pady=50)

app.mainloop()