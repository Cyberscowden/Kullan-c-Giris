from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# Tkinter penceresini oluştur
screen = Tk()
screen.title("Kullanıcı Giriş Ekranı")

screen.geometry("390x220")
screen.resizable(width=False, height=False)

# Resim ekleme




# Hata mesajı
L3 = Label(screen, text="")
L3.place(x=148, y=200)

def giris():

    if (E1.get() == "admin") and (E2.get() == "1234"):
        L3['text'] = "Giriş Başarılı..."
        messagebox.showinfo("Başlık", "Giriş Başarılı")
        print("Başarılı")
    else:
        L3['text'] = "Hatalı Giriş!"
        messagebox.showerror("Hata Başlık", "Hatalı Giriş")

# Kullanıcı Adı ve Şifre giriş alanları
L1 = Label(screen, text="Kullanıcı Adı")
L1.place(x=75, y=15)

E1 = Entry(screen, width=25)
E1.place(x=77, y=45)

L2 = Label(screen, text="Şifre")
L2.place(x=75, y=80)

E2 = Entry(screen, show='*', width=25)
E2.place(x=77, y=110)

# Giriş yap butonu
bt = Button(screen, text="Giriş Yap", padx="20", pady="5", command=giris)
bt.place(x=75, y=150)

# Pencereyi görüntüle
screen.mainloop()
