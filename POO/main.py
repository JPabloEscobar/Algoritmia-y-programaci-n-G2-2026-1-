import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from vista import Vista
from carrito import Carro


METROS_POR_PIXEL  = 1          # escala: 1 px = 1 m  →  1 000 px = 1 km
ARCHIVO_RECORRIDO = "recorrido.txt"


def main():
    # ── 1. Entorno y carro ───────────────────────────────────────────────────
    vista = Vista()
    carro = Carro(vista.canvas)

    metros_recorridos = 0.0     # acumulador de distancia

    # ── 2. Lógica de movimiento ──────────────────────────────────────────────
    def mover_izquierda(evento=None):
        nonlocal metros_recorridos
        d = carro.mover(-carro.VELOCIDAD)
        metros_recorridos += abs(d) * METROS_POR_PIXEL

    def mover_derecha(evento=None):
        nonlocal metros_recorridos
        d = carro.mover(carro.VELOCIDAD)
        metros_recorridos += abs(d) * METROS_POR_PIXEL

    # ── 3. Teclas ────────────────────────────────────────────────────────────
    for tecla in ("<Left>", "a", "A"):
        vista.bind_tecla(tecla, mover_izquierda)
    for tecla in ("<Right>", "d", "D"):
        vista.bind_tecla(tecla, mover_derecha)

    # ── 4. Botón y guardado de recorrido ─────────────────────────────────────
    def guardar_recorrido():
        km   = metros_recorridos / 1000
        ruta = os.path.join(os.path.dirname(__file__), ARCHIVO_RECORRIDO)
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ruta, "a", encoding="utf-8") as f:
            f.write("=== Registro de Recorrido ===\n")
            f.write(f"Fecha y hora  : {ahora}\n")
            f.write(f"Distancia     : {km:.3f} km  ({metros_recorridos:.1f} m)\n")
            f.write("=" * 30 + "\n\n")

        messagebox.showinfo(
            "Recorrido guardado",
            f"Distancia total recorrida: {km:.3f} km\n\nDatos guardados en:\n{ruta}"
        )

    btn_recorrido = tk.Button(
        vista.root,
        text="Recorrido",
        bg="#1565C0", fg="white",
        font=("Arial", 10, "bold"),
        relief="flat", padx=8, pady=4,
        cursor="hand2",
        command=guardar_recorrido
    )
    vista.canvas.create_window(
        Vista.ANCHO - 8, 8,
        anchor="ne",
        window=btn_recorrido
    )

    # ── 5. Arrancar ──────────────────────────────────────────────────────────
    vista.iniciar()


if __name__ == "__main__":
    main()
