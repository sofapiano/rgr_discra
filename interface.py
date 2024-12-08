import tkinter as tk
from main import intersection
from tkinter import simpledialog


def init_gui():
    root = tk.Tk()
    root.title("пересечение множеств")
    root.geometry("736x736")
    return root


def init_canvas(root):
    bg_image = tk.PhotoImage(file="image.png")
    canvas = tk.Canvas(root, width=900, height=500)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.bg_image = bg_image
    return canvas


def display_key(canvas, text):
    lbl_key = tk.Label(
        canvas,
        text=text,
        font=("Roboto", 14))
        # background='#92c2f2')
    canvas.create_window(450, 320, window=lbl_key)


def init_input(canvas):
    lbl_text = tk.Label(
        canvas,
        text="введите множества в консоли. результат будет выведен здесь",
        font=("Roboto", 12),
        anchor="n")
    btn_generate = tk.Button(canvas, text='ввести множества', font=("Roboto", 12), command=lambda: display_key(canvas, intersection()))
    canvas.create_window(450, 280, window=btn_generate)
    canvas.create_window(450, 250, window=lbl_text)


if __name__ == '__main__':
    root = init_gui()
    canvas = init_canvas(root)
    init_input(canvas)
    root.mainloop()