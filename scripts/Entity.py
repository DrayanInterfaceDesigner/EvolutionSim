class Entity:
    def __init__(self) -> None:
        # position in cartesian stage
        self.pos = {"x": 0, "y": 0}
        # scale, the size of the entity scales with it
        self.scale = float(1.0)
        # the base size to scale by self.scale
        self.base_size = 10
        # the size to be used in calculations
        self.size = {"width": self.base_size * self.scale, 
                     "height": self.base_size * self.scale}
        self.color = "#000000"
    
    # everything inside here updates every frame
    def update(self, canvas):
        self.render(canvas)
        
    # to draw the entity
    def render(self, canvas):
        canvas.create_rectangle(self.size["width"], self.size["height"],
                                 2,2, fill=self.color)