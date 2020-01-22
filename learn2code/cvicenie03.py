## Úloha 1
#
# Nakresli 9 pretínajúcich sa kruhov tak ako je to na obrázku spýtaj sa
# používateľa na veľkosť kruhu.  Definuj si najprv súradnice stredného kruhu
# a ostatné odvoď od týchto súradníc
#
# použi nasledujúcu konštrukciu

#import tkinter

#canvas_width=600
#canvas_height=480
#canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
#canvas.pack()

#oval_size=int(input('Set the size of circle: '))
#center_x=canvas_width/2
#center_y=canvas_height/2

#cx, cy, r = center_x, center_y, oval_size/2

#canvas.create_oval(cx-r, cy-r, cx+r, cy+r)
#canvas.create_oval(cx-(r*2), cy-r, cx, cy+r)
#canvas.create_oval(cx, cy-r, cx+(r*2), cy+r)
#canvas.create_oval(cx-r, cy-(r*2), cx+r, cy)
#canvas.create_oval(cx-r, cy, cx+r, cy+(r*2))
#canvas.create_oval(cx-(r*2), cy, cx, cy+(r*2))
#canvas.create_oval(cx, cy, cx+(r*2), cy+(r*2))
#canvas.create_oval(cx-(r*2), cy-(r*2), cx, cy)
#canvas.create_oval(cx, cy-(r*2), cx+(r*2), cy)

#canvas.mainloop()


## Úloha 2
#
# Nakresli olympíjske kruhy. Opýtaj sa používateľa na polomer kruhov a na
# súradnice prvého kruhu. pomocou výpočtov potom zisti súradnice všetkých
# ostatných kruhov. Všimni si, že kruhy sa na X-ovej osi nedotýkajú. Je tam
# istý offset. Offset nastav ako 2% z veľkosti polomeru.

import tkinter
canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

r = int(input("Zadaj polomer kruhu:"))
x = int(input("Zadaj suradnice x, y stredu prvého kruhu:"))
y = x

canvas.create_oval(x-r, y-r, x+r, y+r, width=3, outline="blue")
canvas.create_oval(x+1.1*r, y-r, x+3.1*r, y+r, width=3, outline="black")
canvas.create_oval(x+3.2*r, y-r, x+5.2*r, y+r, width=3, outline="red")
canvas.create_oval(x, y, x+2*r, y+2*r, width=3, outline="yellow")
canvas.create_oval(x+2.1*r, y, x+4.1*r, y+2*r, width=3, outline="green")

#canvas.mainloop()

