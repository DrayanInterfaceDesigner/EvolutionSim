from tkinter import *
import scripts.Entity as Entity

# Instale o pip na máquina e use
# pip install tkinter

window = Tk()
# Não ta funcionando direito ainda pq não entendi como funciona
# o Tkinter ainda. Tipo, namoral, pra que um retangulo precisa 
# de 4 coordenadas num plano 2D? mas enfim, talvez mude pra turtle
entity = Entity.Entity({"x": 25, "y": 25}, 10.0)

if __name__ == "__main__":
    canvas = Canvas(window,height=500, width=500)
    # ---- START ----
    # everything you want to put inside the world
    # goes below this line

    entity.update(canvas)

    # ---- END ----
    canvas.pack()
    window.mainloop()