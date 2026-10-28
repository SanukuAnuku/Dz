from tkinter import *
import math

root = Tk()
root.title("Круг")
root.geometry("400x400")

# переменная кнопок
a = 0

while a < 12:
    angle = a * 30 * math.pi / 180

    # координаты
    x = 170 + 130 * math.cos(angle)
    y = 170 + 130 * math.sin(angle)

    # енопка
    Button(root, text=a + 1, width=4, height=2).place(x=x, y=y)

    a = a + 1

root.mainloop()