import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os

def open_option1():
    subprocess.Popen([r'C:\ATS\xTotenGeneric.exe'])

def open_option2():
    webbrowser.open('https://seumotora.contatto.com.br/login')

def open_option3():
    webbrowser.open('https://seumotora.contatto.com.br/pesquisa')

def open_option4():
    messagebox.showinfo("Option 4", "Esta opção está em desenvolvimento")

def open_option5():
    messagebox.showinfo("Option 5", "Esta opção está em desenvolvimento")

def open_option6():
    messagebox.showinfo("Option 6", "Esta opção está em desenvolvimento")

def open_option7():
    messagebox.showinfo("Option 7", "Esta opção está em desenvolvimento")

def close_app():
    root.destroy()

def main():
    global root
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title("Kiosque")
    root.update_idletasks()  # Garantir que a janela esteja completamente inicializada

    # Carregar imagem de fundo
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    bg_image_path = r"C:\Users\kiosk\Pictures\imagens kiosque\background.png"
    
    print(f"Verificando o caminho: {bg_image_path}")
    if not os.path.exists(bg_image_path):
        print(f"Erro: O arquivo {bg_image_path} não foi encontrado.")
        return

    bg_image = Image.open(bg_image_path).resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(bg_image)

    # Criar um label para a imagem de fundo
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="", highlightthickness=0)
    frame.pack(expand=True)
    
    # Carregar e redimensionar imagens
    img1 = Image.open(r"C:\Users\kiosk\Pictures\imagens kiosque\ats.png").resize((350, 350), Image.Resampling.LANCZOS)
    img2 = Image.open(r"C:\Users\kiosk\Pictures\imagens kiosque\seu motora.png").resize((350, 350), Image.Resampling.LANCZOS)
    img3 = Image.open(r"C:\Users\kiosk\Pictures\imagens kiosque\CAM.png").resize((350, 350), Image.Resampling.LANCZOS)
    img4 = Image.open(r"C:\Users\kiosk\Pictures\imagens kiosque\CTE.png").resize((350, 350), Image.Resampling.LANCZOS)
    img5 = Image.open(r"C:\Users\kiosk\Pictures\imagens kiosque\Checklist.png").resize((350, 350), Image.Resampling.LANCZOS)
    img6 = Image.open(r"C:\Users\kiosk\Pictures\imagens kiosque\Onde.png").resize((350, 350), Image.Resampling.LANCZOS)
    img7 = Image.open(r"C:\Users\kiosk\Pictures\imagens kiosque\manual.png").resize((350, 350), Image.Resampling.LANCZOS)

    img1 = ImageTk.PhotoImage(img1)
    img2 = ImageTk.PhotoImage(img2)
    img3 = ImageTk.PhotoImage(img3)
    img4 = ImageTk.PhotoImage(img4)
    img5 = ImageTk.PhotoImage(img5)
    img6 = ImageTk.PhotoImage(img6)
    img7 = ImageTk.PhotoImage(img7)

    # Criar botões com imagens e ajustar tamanho
    btn1 = tk.Button(frame, command=open_option1, image=img1, bd=0, highlightthickness=0, relief="flat", bg="white", activebackground="white")
    btn1.grid(row=0, column=0)

    btn2 = tk.Button(frame, command=open_option2, image=img2, bd=0, highlightthickness=0, relief="flat", bg="white", activebackground="white")
    btn2.grid(row=0, column=1)

    btn3 = tk.Button(frame, command=open_option3, image=img3, bd=0, highlightthickness=0, relief="flat", bg="white", activebackground="white")
    btn3.grid(row=0, column=2)

    btn4 = tk.Button(frame, command=open_option4, image=img4, bd=0, highlightthickness=0, relief="flat", bg="white", activebackground="white")
    btn4.grid(row=1, column=0)

    btn5 = tk.Button(frame, command=open_option5, image=img5, bd=0, highlightthickness=0, relief="flat", bg="white", activebackground="white")
    btn5.grid(row=1, column=1)

    btn6 = tk.Button(frame, command=open_option6, image=img6, bd=0, highlightthickness=0, relief="flat", bg="white", activebackground="white")
    btn6.grid(row=1, column=2)

    btn7 = tk.Button(frame, command=open_option7, image=img7, bd=0, highlightthickness=0, relief="flat", bg="white", activebackground="white")
    btn7.grid(row=2, column=1)

    # Botão oculto para fechar o aplicativo
    hidden_btn = tk.Button(root, text="", command=close_app, width=1, height=1, bd=0, highlightthickness=0, relief="flat", bg="white", activebackground="white")
    hidden_btn.place(x=screen_width - 20, y=10)

    # Manter referências às imagens
    btn1.image = img1
    btn2.image = img2
    btn3.image = img3
    btn4.image = img4
    btn5.image = img5
    btn6.image = img6
    btn7.image = img7
    bg_label.image = bg_image

    root.mainloop()

if __name__ == "__main__":
    main()