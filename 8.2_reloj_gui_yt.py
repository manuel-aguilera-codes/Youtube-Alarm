import tkinter as tk
from datetime import datetime
import time
import random
import webbrowser
from pathlib import Path
import sys

def leer_enlaces():
    if hasattr(sys, '_MEIPASS'):
        ruta_base = Path(sys._MEIPASS)
    else:
        ruta_base = Path(__file__).parent

    ruta_archivo = ruta_base / "8_links_youtube.txt"

    with open(ruta_archivo, "r") as archivo:
        enlaces = archivo.readlines()

    enlaces_limpios = [linea.strip() for linea in enlaces if linea.strip() != ""]
    return enlaces_limpios

# ACTIVAR ALARMA
def activar_alarma():
    hora_ingresada = entry_hora.get()

    try:
        alarma = datetime.strptime(hora_ingresada, "%H:%M").time()
    except ValueError:
        etiqueta_estado.config(text="Formato inválido. Usa HH:MM")
        return

    etiqueta_estado.config(text="Alarma activada")
    revisar_alarma(alarma)

# REVISAR LA HORA
def revisar_alarma(alarma):
    ahora = datetime.now().time()

    if ahora.hour == alarma.hour and ahora.minute == alarma.minute:
        etiqueta_estado.config(text="¡ALARMA!")

        enlaces = leer_enlaces()
        enlace_aleatorio = random.choice(enlaces)

        webbrowser.open(enlace_aleatorio)
        return

    ventana.after(1000, lambda: revisar_alarma(alarma))


# INTERFAZ GRÁFICA
ventana = tk.Tk()
ventana.title("Reloj Despertador YouTube")
ventana.geometry("350x200")

etiqueta = tk.Label(ventana, text="Ingresa la hora (HH:MM)")
etiqueta.pack(pady=10)

entry_hora = tk.Entry(ventana, font=("Arial", 14))
entry_hora.pack()

boton = tk.Button(ventana, text="Activar alarma", command=activar_alarma)
boton.pack(pady=10)

etiqueta_estado = tk.Label(ventana, text="")
etiqueta_estado.pack()

ventana.mainloop()
