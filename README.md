# Sely-Automator v1.0 🚀

**Sely-Automator** es una herramienta de escritorio desarrollada en Python diseñada para optimizar y automatizar la gestión de facturación comercial a partir de archivos de datos en Excel. 

El programa procesa de forma automática los listados de ventas, calcula los montos totales pendientes por cada cliente y genera facturas individuales personalizadas en formato PDF, todo a través de una interfaz gráfica intuitiva y limpia.

---

## ✨ Características

* **Procesamiento Inteligente:** Calcula automáticamente el total por fila (Cantidad × Precio) y agrupa los montos acumulados por cliente.
* **Generación de PDFs Automática:** Crea documentos PDF comerciales limpios y estandarizados para cada cliente procesado.
* **Interfaz Gráfica (GUI) Moderna:** Diseñada con `CustomTkinter`, ofreciendo una experiencia de usuario oscura, minimalista y directa (un solo clic para operar).
* **Compilación Portable:** Configurado para empaquetarse en un único archivo ejecutable (`.exe`) independiente sin necesidad de instalar Python en la máquina final.

---

## 🛠️ Tecnologías Utilizadas

* **Python 3** (Lenguaje principal)
* **Pandas:** Para la manipulación, lectura y agrupación eficiente de los datos de Excel.
* **FPDF2 / FPDF:** Para la estructura, diseño y exportación de las facturas en PDF.
* **CustomTkinter:** Para la creación de la interfaz gráfica de usuario moderna.
* **PyInstaller:** Para el empaquetado del proyecto en un archivo ejecutable portable.

---

## 📂 Estructura del Repositorio

* `main.py`: Código fuente principal que contiene la lógica del negocio, el diseño del PDF y la interfaz gráfica.
* `main.spec`: Archivo de configuración de PyInstaller para compilar el ejecutable de manera exacta.

---

## 🚀 Instalación y Uso (Desarrolladores)

Si deseas ejecutar o modificar el código fuente, sigue estos pasos:

1. **Clona el repositorio:**
```bash
   git clone [https://github.com/Seeltir/Sely_automator.git](https://github.com/Seeltir/Sely_automator.git)
   cd Sely_automator
2. **Instala las dependencias necesarias:**
   pip install pandas fpdf2 customtkinter openpyxl
3. **Ejecuta la aplicación**
   python main.py

---

## 📥 Descargar la Aplicación (Usuarios)
Si solo deseas utilizar la herramienta sin necesidad de programar, ve a la sección de Releases en la barra lateral derecha de este repositorio y descarga el archivo main.exe de la versión más reciente. ¡Listo para usar!
