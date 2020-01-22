import random
import tkinter
import randomcolor

canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()


for n in range(100):
    x = random.randrange(800)
    y = random.randrange(600)
    x2 = random.randrange(800)
    y2 = random.randrange(600)
    rand_color = randomcolor.RandomColor()
    width = random.randrange(3)
    canvas.create_rectangle(x, y, x2, y2, fill = rand_color.generate(), width = width)

canvas.mainloop()
