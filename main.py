from tkinter import *
import scripts.Entity as Entity

window = Tk()
entity = Entity.Entity()

if __name__ == "__main__":
    canvas = Canvas(window,height=500, width=500)
    # ---- START ----
    # everything you want to put inside the world
    # goes below this line

    entity.update(canvas)

    # ---- END ----
    canvas.pack()
    window.mainloop()