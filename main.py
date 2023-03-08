from tkinter import *
import scripts.Entity as Entity

window = Tk()
entity = Entity.Entity()

if __name__ == "__main__":
    canvas = Canvas(window,height=500, width=500)
    entity.update(canvas)

    canvas.pack()
    window.mainloop()