class Entity:
    def __init__(self, pos = {"x": 0, "y": 0} , scale = float(1.0) ) -> None:
        # Posição no plano cartesiano
        self.pos = pos
        # Multiplicador do tamanho base. 2.0 dobra o tamanho
        self.scale = scale
        # Tamanho base, não deve ser mudado fora da classe
        self._base_size = 10
        # O tamanho calculado. 
        self.size = {"width": self._base_size * self.scale, 
                     "height": self._base_size * self.scale}
        self.color = "#000000"
    
    # Tudo aqui atualiza por frame
    def update(self, canvas):
        self.render(canvas)
        
    # Desenha a entidade (criatura)
    def render(self, canvas):
        canvas.create_rectangle(self.size["width"], self.size["height"],
                                self.pos["x"], self.pos["y"], fill=self.color)