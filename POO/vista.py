import tkinter as tk


class Vista:
    """
    Entorno gráfico del juego.
    Solo se encarga de la ventana, el canvas y el fondo (cielo, pasto, carretera).
    No sabe nada del carro ni de la lógica de juego.
    """

    ANCHO = 800
    ALTO = 400

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Carro POO")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=self.ANCHO,
            height=self.ALTO,
            bg="#87CEEB"
        )
        self.canvas.pack()

        self._dibujar_fondo()

    # ------------------------------------------------------------------ fondo
    def _dibujar_fondo(self):
        # Pasto
        self.canvas.create_rectangle(
            0, 320, self.ANCHO, self.ALTO,
            fill="#4CAF50", outline=""
        )
        # Carretera
        self.canvas.create_rectangle(
            0, 300, self.ANCHO, 340,
            fill="#555555", outline=""
        )
        # Línea central de la carretera
        for i in range(0, self.ANCHO, 60):
            self.canvas.create_rectangle(
                i, 318, i + 35, 323,
                fill="white", outline=""
            )

    # --------------------------------------------------------- utilidades
    def bind_tecla(self, tecla, callback):
        self.root.bind(tecla, callback)

    def iniciar(self):
        self.root.mainloop()
