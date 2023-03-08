class Entity:
    def __init__(self) -> None:
        self.pos = {"x": 0, "y": 0}
        self.scale = float(1.0)
        self.base_size = 10
        self.size = {"width": self.base_size * self.scale, 
                     "height": self.base_size * self.scale}
        self.color = "#000000"
    

    def update(self, canvas):
        self.draw(canvas)
    def draw(self, canvas):
        canvas.create_rectangle(self.size["width"], self.size["height"],
                                 2,2, fill=self.color)