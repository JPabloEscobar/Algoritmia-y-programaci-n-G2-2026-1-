class Carro:
    """
    Representa el carro dentro del canvas.
    Solo se encarga de dibujarse y de moverse sobre el eje X.
    No conoce la ventana, las teclas ni la lógica de juego.
    """

    VELOCIDAD  = 15
    LIMITE_IZQ = 0
    LIMITE_DER = 700

    def __init__(self, canvas, x=50, y=260):
        self._canvas = canvas
        self._x = x
        self._y = y
        self._partes = []
        self._dibujar()

    # ------------------------------------------------------------------ dibujo
    def _dibujar(self):
        x = self._x
        y = self._y
        c = self._canvas

        # Carrocería inferior
        self._partes.append(c.create_rectangle(
            x, y + 20, x + 110, y + 60,
            fill="#D32F2F", outline="#B71C1C", width=2
        ))
        # Techo / cabina
        self._partes.append(c.create_rectangle(
            x + 18, y, x + 88, y + 25,
            fill="#E53935", outline="#B71C1C", width=2
        ))
        # Ventana delantera
        self._partes.append(c.create_rectangle(
            x + 62, y + 3, x + 85, y + 22,
            fill="#B3E5FC", outline="#0288D1", width=1
        ))
        # Ventana trasera
        self._partes.append(c.create_rectangle(
            x + 20, y + 3, x + 58, y + 22,
            fill="#B3E5FC", outline="#0288D1", width=1
        ))
        # Rueda trasera
        self._partes.append(c.create_oval(
            x + 10, y + 48, x + 46, y + 76,
            fill="#212121", outline="#424242", width=2
        ))
        self._partes.append(c.create_oval(
            x + 18, y + 56, x + 38, y + 68,
            fill="#757575", outline=""
        ))
        # Rueda delantera
        self._partes.append(c.create_oval(
            x + 65, y + 48, x + 101, y + 76,
            fill="#212121", outline="#424242", width=2
        ))
        self._partes.append(c.create_oval(
            x + 73, y + 56, x + 93, y + 68,
            fill="#757575", outline=""
        ))
        # Faro delantero
        self._partes.append(c.create_rectangle(
            x + 98, y + 28, x + 112, y + 38,
            fill="#FFEE58", outline="#F9A825", width=1
        ))
        # Faro trasero
        self._partes.append(c.create_rectangle(
            x - 2, y + 28, x + 10, y + 38,
            fill="#EF9A9A", outline="#C62828", width=1
        ))

    # --------------------------------------------------------- API pública
    def mover(self, dx):
        """Desplaza el carro dx píxeles. Retorna el desplazamiento real aplicado."""
        nueva_x = self._x + dx
        nueva_x = max(self.LIMITE_IZQ, min(nueva_x, self.LIMITE_DER))

        desplazamiento = nueva_x - self._x
        if desplazamiento != 0:
            for parte in self._partes:
                self._canvas.move(parte, desplazamiento, 0)
            self._x = nueva_x
        return desplazamiento
