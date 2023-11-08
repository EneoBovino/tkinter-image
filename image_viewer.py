from tkinter import *
from PIL import ImageTk, Image, ImageOps
import os

# Define a janela principal
root = Tk()
root.title("Image Viewer")
root.iconbitmap("app.ico")

img_list = []

img_num = 0

for img_file in os.listdir("images"):
    # Carrega a imagem
    img = Image.open("images/" + img_file)    
    # Redimensiona a imagem
    img = ImageOps.contain(img, (150, 150))
    # Converte a imagem para o formato do tkinter
    img_tk = ImageTk.PhotoImage(img)
    # Adiciona a imagem na lista
    img_list.append(img_tk)

# Carrega a primeira imagem da lista
img_label = Label(image=img_list[0])

# Empacota o label da imagem
img_label.grid(row=0, column=0, columnspan=3)

def prev_image():
    global img_label
    global img_list
    global img_num

    # Remove a imagem atual
    img_label.grid_forget()

    # Atualiza o número da imagem
    img_num -= 1

    # Verifica se o número da imagem é válido
    if img_num < 0:
        img_num = len(img_list) - 1

    # Atualiza a imagem
    img_label = Label(image=img_list[img_num])
    img_label.grid(row=0, column=0, columnspan=3)

def next_image():
    global img_label
    global img_list
    global img_num

    # Remove a imagem atual
    img_label.grid_forget()

    # Atualiza o número da imagem
    img_num += 1

    # Verifica se o número da imagem é válido
    if img_num >= len(img_list):
        img_num = 0

    # Atualiza a imagem
    img_label = Label(image=img_list[img_num])
    img_label.grid(row=0, column=0, columnspan=3)

btn_prev = Button(root, text="<<", command=prev_image)
btn_next = Button(root, text=">>", command=next_image)
btn_exit = Button(root, text="Exit Program", command=root.quit)

btn_prev.grid(row=1, column=0)
btn_next.grid(row=1, column=2)
btn_exit.grid(row=1, column=1)

# Define o loop principal
root.mainloop()
