import tkinter as tk
from tkinter import messagebox 
from tkinter import StringVar
from tkinter import *
from tkinter import ttk
import os

#WELCOME TO PENTAS (PENJUALAN TANAMAN HIAS)

def ksg():
    if len(nama.get()) == 0:
        messagebox.showerror("PERHATIAN!!!","Mohon nama tidak boleh dikosongkan")
        return
    if len(handphone.get()) == 0:
        messagebox.showerror("PERHATIAN!!!","Anda belum mengisi nomor handphone")
        return
    try:
        int(handphone.get())
    except ValueError:
        messagebox.showerror("PERHATIAN","MASUKAN HURUF UNTUK NAMA, DAN MASUKKAN ANGKA UNTUK NOMOR HANDPHONE")
        return

    
    def totalharga():
        if len(jumlah.get()) == 0:
            messagebox.showerror("PERHATIAN!!!","Anda belum mengisi Jumlah yang anda inginkan")
            return
        try:
            int(jumlah.get())
        except ValueError:
            messagebox.showerror("PERHATIAN","Harap mengisi jumlah dengan ANGKA")
            return
        
        tjumlah = int(jumlah.get())
        Aglonema = 150000
        Mawar = 120000
        Melati = 100000
        Kaktus = 50000
        Anggrek  = 200000

        if tanaman.get() == "Aglonema":
            total = tjumlah * Aglonema   
        elif tanaman.get() == "Mawar":
            total = tjumlah * Mawar   
        elif tanaman.get() == "Melati":
            total = tjumlah * Melati       
        elif tanaman.get() == "Kaktus":
            total = tjumlah* Kaktus          
        elif tanaman.get() == "Anggrek":
            total = tjumlah* Anggrek
            
        Label(root, text= str(nama.get()), bg="#6ab2ca").place(x=128, y=395)
        Label(root, text="Anda telah memesan " + str(tjumlah) + " " +(tanaman.get()), bg="#6ab2ca").place(x=130, y=425)
        Label(root, text="dengan total harga : Rp" + str(total) + ".00" , bg="#6ab2ca").place(x=132, y=455)
        Label(root, text = "Masukkan Alamat Anda:",bg="#6ab2ca", font=("Times new roman", 9)).place(x=157, y=485)

        alamat.place(x=126, y=505)

        Button(root, text="PESAN", command=root.destroy).place(x=200, y=570)


        
    def tanamanpilihan():
        if tanaman.get() == 'Aglonema':
            response = messagebox.askokcancel("PESANAN", "Apakah anda ingin membeli Aglonema dengan harga Rp150.000.00?")
    
            if response == 1:
                jumlah.place(x=230, y=260)
                
                Label(root,bg="#6ab2ca", text="yang akan dibeli:", font=("Times new roman", 10)).place(x=133, y=260)
                Label(root,bg="#6ab2ca", text="jumlah Aglonema ", font=("Times new roman", 10)).place(x=133,y=240)
                tombolT1 = Button(root, text="SUBMIT", command=totalharga).place(x=188, y=283)
            else:
                Label(root, text="Anda tidak membeli aglonema",bg="#6ab2ca").place(x=137, y=410)
                
        elif tanaman.get() == 'Mawar':
            response = messagebox.askokcancel("PESANAN", "Apakah anda ingin membeli Mawar dengan harga Rp120.000.00?")
            
            if response == 1:
                jumlah.place(x=230, y=260)
                Label(root,bg="#6ab2ca", text="yang akan dibeli:", font=("Times new roman", 10)).place(x=133, y=260)
                Label(root,bg="#6ab2ca", text="jumlah Mawar ", font=("Times new roman", 10)).place(x=133,y=240)
                tombolT1 = Button(root, text="SUBMIT", command=totalharga).place(x=188, y=283)
            else:
                Label(root, text="Anda tidak membeli Mawar",bg="#6ab2ca").place(x=137, y=410)
                
        elif tanaman.get() == 'Melati':
            response = messagebox.askokcancel("PESANAN", "Apakah anda ingin membeli Melati dengan harga Rp100.000.00?")
            
            if response == 1:
                jumlah.place(x=230, y=260)
                Label(root,bg="#6ab2ca", text="yang akan dibeli:", font=("Times new roman", 10)).place(x=133, y=260)
                Label(root,bg="#6ab2ca", text="jumlah Melati ", font=("Times new roman", 10)).place(x=133,y=240)
                tombolT1 = Button(root, text="SUBMIT", command=totalharga).place(x=188, y=283)
            else:
                Label(root, text="Anda tidak membeli Melati",bg="#6ab2ca").place(x=137, y=410)
                
        elif tanaman.get() == 'Kaktus':
            response = messagebox.askokcancel("PESANAN", "Apakah anda ingin membeli Kaktus dengan harga Rp50.000.00?")
            
            if response == 1:
                jumlah.place(x=230, y=260)
                Label(root,bg="#6ab2ca", text="yang akan dibeli:", font=("Times new roman", 10)).place(x=133, y=260)
                Label(root,bg="#6ab2ca", text="jumlah Kaktus ", font=("Times new roman", 10)).place(x=133,y=240)
                tombolT1 = Button(root, text="SUBMIT", command=totalharga).place(x=188, y=283)
            else:
                Label(root, text="Anda tidak membeli Kaktus",bg="#6ab2ca").place(x=137, y=410)

        elif tanaman.get() == 'Anggrek':
            response = messagebox.askokcancel("PESANAN", "Apakah anda ingin membeli Kaktus dengan harga Rp200.000.00?")
            
            if response == 1:
                jumlah.place(x=230, y=260)
                Label(root,bg="#6ab2ca", text="yang akan dibeli:", font=("Times new roman", 10)).place(x=133, y=260)
                Label(root,bg="#6ab2ca", text="jumlah Anggrek ", font=("Times new roman", 10)).place(x=133,y=240)
                tombolT1 = Button(root, text="SUBMIT", command=totalharga).place(x=188, y=283)
            else:
                Label(root, text="Anda tidak membeli Anggrek",bg="#6ab2ca").place(x=137, y=410)

    
    #Setting
    pilihan = [
        "Aglonema",
        "Mawar",
        "Melati",
        "Kaktus",
        "Anggrek",
    ]

    tanaman = StringVar()
    tanaman.set(pilihan[0])
    drop = OptionMenu(root, tanaman, *pilihan)
    drop.pack(pady=170)

    #label
    labelT1 = tk.Label(bg="#6ab2ca", text = "Pilih tanaman yang akan dibeli:").place(x=130,y=150)

    #tombol
    tombolT1 = Button(root, text="SUBMIT", command=tanamanpilihan).place(x=188, y=200)
    
    
#Setting
root = tk.Tk()   
root.title("KEBUN KAROMAH")
root.geometry("432x650")
root.iconbitmap('D:\KebunKaromah.ico')

bg = PhotoImage(file=r"D:\bg\bg.png")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)


#label
label1 = tk.Label(bg="#6d6d6d", text="SELAMAT DATANG DI KEBUN KAROMAH", font=("Futuristic", 12)).place(x=75, y=12)
label2 = tk.Label(bg="#6d6d6d",fg="white", text = "Masukkan Nama  :", font=("Times new roman", 9)).place(x=0, y=60)
label3 = tk.Label(bg="#6d6d6d",fg="white", text = "Masukkan No HP:", font=("Times new roman", 9)).place(x=0, y=80)


#Input
nama = StringVar()
inama = tk.Entry(root, width=35, textvariable = nama, font=("Times new roman", 9)).place(x=110, y=60)
handphone = StringVar()
ihp = tk.Entry(root, width=35, textvariable = handphone).place(x=110, y=80)
jumlah = Entry(root, width=10, justify='center')
alamat = Text(root, width=32, height=4,font=("Times new roman", 9))


#tombol
tombol1 = Button (command = ksg, text="SUBMIT").place(x=112, y=118)
