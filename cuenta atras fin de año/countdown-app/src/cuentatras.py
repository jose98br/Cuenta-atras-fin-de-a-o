import time
from datetime import datetime
import tkinter as tk

def tiempo_restante():
    """Calcula el tiempo restante hasta el fin de año."""
    ahora = datetime.now()
    fin_de_año = datetime(ahora.year + 1, 1, 1)
    return fin_de_año - ahora

def actualizar_cuenta_atras():
    """Actualiza la cuenta atrás en la pantalla."""
    tiempo = tiempo_restante()
    dias, segundos = tiempo.days, tiempo.seconds
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    
    cuenta_atras.config(text=f"Faltan {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos para el fin de año.")
    root.after(1000, actualizar_cuenta_atras)

root = tk.Tk()
root.title("Cuenta Atrás para Fin de Año")

cuenta_atras = tk.Label(root, font=("Helvetica", 24))
cuenta_atras.pack()

actualizar_cuenta_atras()
root.mainloop()