from tkinter import *
import tkinter
import numpy as np
import math
from tkinter import colorchooser
from tkinter.colorchooser import askcolor

from numpy.lib.function_base import append

class Paint(object):

    WIDTH = 600
    HEIGHT = 600
    center = [WIDTH/2,HEIGHT/2]
    DEFAULT_COLOR = 'white'
    DEFAULT_COLOR_OUTLINE = 'black'
    CLICKED_BUTTON = ''
    titik = []
    arah_translasi = ["Kiri Atas","Atas","Kanan Atas","Kanan","Kanan Bawah","Bawah","Kiri Bawah","Kiri"]
    
    def __init__(self):
        self.root = Tk()
        
        icon_oval = PhotoImage(file = "D:\RS KULIAH\SEMESTER 6\GRAFKOM\ProjectGrafikaKomputer\images\oval.png")
        icon_kotak = PhotoImage(file = "D:\RS KULIAH\SEMESTER 6\GRAFKOM\ProjectGrafikaKomputer\images\persegi.png")
        icon_segitiga = PhotoImage(file = "D:\RS KULIAH\SEMESTER 6\GRAFKOM\ProjectGrafikaKomputer\images\segitiga.png")

        icon_oval = icon_oval.subsample(3,3)
        icon_kotak = icon_kotak.subsample(3,3)
        icon_segitiga = icon_segitiga.subsample(3,3)
        
        #setting ukuran canvas sebesar 600px x 600px
        self.c = Canvas(self.root,bg='white',width=self.WIDTH,height=self.HEIGHT)
        self.c.grid(row=0)

        #Tombol Shape
        self.oval_button = Button(self.root, text="Oval", image=icon_oval ,command=self.use_oval, compound=LEFT)
        self.oval_button.grid(row=1,column=0,sticky=NW,padx=30)
        
        self.kotak_button = Button(self.root, text="Persegi", image=icon_kotak, command=self.use_kotak, compound=LEFT)
        self.kotak_button.grid(row=1,column=0,sticky=W,padx=30)

        self.segitiga_button = Button(self.root, text="Segitiga", image=icon_segitiga, command=self.use_segitiga, compound=LEFT)
        self.segitiga_button.grid(row=1,column=0,sticky=SW,padx=30)

        #Tombol Warna
        self.pick_color_button = Button(self.root, text="Warna Fill",command=self.pick_color)
        self.pick_color_button.grid(row=0,column=1,sticky=N,padx=30)
        
        self.pick_color_hasil = Button(self.root,background=self.DEFAULT_COLOR)
        self.pick_color_hasil.grid(row=0,column=1,sticky=N,pady=30,ipadx=10)

        self.pick_color_outline_button = Button(self.root,text="Warna Outline",command=self.pick_color_outline)
        self.pick_color_outline_button.grid(row=0,column=1,sticky=N,padx=50,pady=60)

        self.pick_color_outline_hasil = Button(self.root,background=self.DEFAULT_COLOR)
        self.pick_color_outline_hasil.grid(row=0,column=1,sticky=N,pady=90,ipadx=10)
        #Tombol Translasi
        self.arah_button = StringVar(self.root)
        self.arah_button.set(self.arah_translasi[0])

        self.arah_isi = OptionMenu(self.root,self.arah_button,*self.arah_translasi)
        self.arah_isi.grid(row=0,column=1,sticky=W,padx=100)

        self.arah_value = Spinbox(self.root,width=5,from_=0,to=100,increment=5)
        self.arah_value.grid(column=1,padx=140,row=0,sticky=E)

        self.arah_submit = Button(self.root, text="Apply",command=self.translasi)
        self.arah_submit.grid(column=1,row=0,pady=250,sticky=S)

        #Tombol Rotasi
        self.rotasi_button = Button(self.root, text="Rotate",command=self.rotasi)
        self.rotasi_button.grid(column=0,row=1,sticky=NE,padx=300,pady=10)

        self.rotasi_value = Spinbox(self.root,width=5,from_=-100,to=100,increment=5)
        self.rotasi_value.grid(column=0,padx=240,row=1,sticky=NE,pady=13)

        #Tombol Output Koordinat
        self.print_titik_kotak = Text(self.root, height=10, width=50)
        self.print_titik_kotak.grid(row=1,column=1)
        
        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None

        self.use_oval()
        # self.c.bind('<B1-Motion>', self.paint)
        # self.c.bind('<ButtonRelease-1>', self.reset)

#Pembuatan Oval
    def use_oval(self,titik = None):
        #(x1,y1,x2,y2)
        self.c.delete("all")

        #variabel titik di cek, jika tidak ada isinya, maka menggunakan variabel yang ada
        if(titik == None):
            self.titik = [[200,200],[400,400]]
        else:
            self.titik = titik
        self.c.create_oval(self.titik,fill= self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR_OUTLINE,width=2)
        self.CLICKED_BUTTON = "oval"
        self.print_titik()

#Pembuatan Persegi
    def use_kotak(self,titik = None):
        #(x1,y1,x2,y2)
        self.c.delete("all")
        if(titik == None):
            self.titik = [[200,200],[200,400],[400,400],[400,200],]
        else:
            self.titik = titik
        self.c.create_polygon(self.titik,fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR_OUTLINE,width=2)
        self.CLICKED_BUTTON = "kotak"
        self.print_titik()

#Pembuatan Segitiga
    def use_segitiga(self,titik = None):
        #(x1,y1,x2,y2,x3,y3)
        # titik 0 dari kiri atas
        # x = 0 kiri, x = 10 kanan
        # y = 0 atas, y = 10 kebawah
        self.c.delete("all")
        if(titik == None):
            self.titik = [[200,400],[400,400],[300,200]]
        else:
            self.titik = titik
        self.c.create_polygon(self.titik, fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR_OUTLINE)
        self.CLICKED_BUTTON = "segitiga"
        self.print_titik()

# Untuk memilih warna
    def pick_color(self):
        self.DEFAULT_COLOR = colorchooser.askcolor(title = "Choose color")[1]
        self.onCLick(self.titik)

    def pick_color_outline(self):
        self.DEFAULT_COLOR_OUTLINE = colorchooser.askcolor(title = "Choose color")[1]
        self.onCLick(self.titik)

# Untuk menyimpan button apa yang telah ditekan antara bangun datar
    def onCLick(self,titik):
        if self.CLICKED_BUTTON == 'oval':
            self.c.create_oval(titik,fill= self.DEFAULT_COLOR,width=2,outline=self.DEFAULT_COLOR_OUTLINE)
        elif self.CLICKED_BUTTON == 'kotak':
            self.c.create_polygon(titik,fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR_OUTLINE,width=2)
        elif self.CLICKED_BUTTON == 'segitiga':
            self.c.create_polygon(titik, fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR_OUTLINE)
        self.pick_color_hasil.configure(bg=self.DEFAULT_COLOR)
        self.pick_color_outline_hasil.configure(bg=self.DEFAULT_COLOR_OUTLINE)

# Untuk menulis output koordinat
    def print_titik(self):
        self.print_titik_kotak.delete("1.0",END)
        self.print_titik_kotak.insert(END,self.titik)

# Fungsi pergeseran
# 0 dalam koordinat x berarti kiri,
# 0 dalam koordinat y berarti atas

    def translasi(self):
        if(self.arah_button.get() == "Kiri"):
            titik = []
            # perulangan untuk mengecek index
            # jika index nya genap, maka dikurangi
            # index genap = koordinat x
            # index ganjil = koordinat y
            for i in range(0, len(self.titik)):
                var_titik =[]
                for j in range(0,len(self.titik[i])):
                    if j%2 == 0:
                        var_titik.append(self.titik[i][j] - int(self.arah_value.get()))
                    else:
                        var_titik.append(self.titik[i][j])
                titik.append(var_titik)        
            
            # Untuk mengaplikasikan pergeseran sesuai bentuk
            if(self.CLICKED_BUTTON == "oval"):
                self.use_oval(titik)
            elif(self.CLICKED_BUTTON == "kotak"):
                self.use_kotak(titik)    
            elif(self.CLICKED_BUTTON == "segitiga"):    
                self.use_segitiga(titik)

        elif(self.arah_button.get() == "Kiri Atas"):
            titik =[]
            for i in range(0,len(self.titik)):
                var_titik = []
                for j in range(0,len(self.titik[i])):
                    var_titik.append(self.titik[i][j] - int(self.arah_value.get()))  
                titik.append(var_titik)

            if(self.CLICKED_BUTTON == "oval"):
                self.use_oval(titik)
            elif(self.CLICKED_BUTTON == "kotak"):
                self.use_kotak(titik)    
            elif(self.CLICKED_BUTTON == "segitiga"):    
                self.use_segitiga(titik)

        elif(self.arah_button.get() == "Atas"):
            titik = []
            
            for i in range(0, len(self.titik)):
                var_titik =[]
                for j in range(0,len(self.titik[i])):
                    if j%2 == 1:
                        var_titik.append(self.titik[i][j] - int(self.arah_value.get()))
                    else:
                        var_titik.append(self.titik[i][j])
                titik.append(var_titik)
            
            # Untuk mengaplikasikan pergeseran sesuai bentuk
            if(self.CLICKED_BUTTON == "oval"):
                self.use_oval(titik)
            elif(self.CLICKED_BUTTON == "kotak"):
                self.use_kotak(titik)    
            elif(self.CLICKED_BUTTON == "segitiga"):    
                self.use_segitiga(titik)

        elif(self.arah_button.get() == "Kanan Atas"):
            titik = []
            for i in range(0, len(self.titik)):
                var_titik =[]
                for j in range(0,len(self.titik[i])):
                    if j%2 == 1:
                        var_titik.append(self.titik[i][j] - int(self.arah_value.get()))
                    elif j%2 == 0:
                        var_titik.append(self.titik[i][j] + int(self.arah_value.get()))
                titik.append(var_titik)
            
            # Untuk mengaplikasikan pergeseran sesuai bentuk
            if(self.CLICKED_BUTTON == "oval"):
                self.use_oval(titik)
            elif(self.CLICKED_BUTTON == "kotak"):
                self.use_kotak(titik)    
            elif(self.CLICKED_BUTTON == "segitiga"):    
                self.use_segitiga(titik)
        
        elif(self.arah_button.get() == "Kanan"):
            titik = []
            
            for i in range(0, len(self.titik)):
                var_titik =[]
                for j in range(0,len(self.titik[i])):
                    if j%2 == 0:
                        var_titik.append(self.titik[i][j] + int(self.arah_value.get()))
                    else:
                        var_titik.append(self.titik[i][j])
                titik.append(var_titik)
            
            # Untuk mengaplikasikan pergeseran sesuai bentuk
            if(self.CLICKED_BUTTON == "oval"):
                self.use_oval(titik)
            elif(self.CLICKED_BUTTON == "kotak"):
                self.use_kotak(titik)    
            elif(self.CLICKED_BUTTON == "segitiga"):    
                self.use_segitiga(titik) 
        
        elif(self.arah_button.get() == "Kanan Bawah"):
            titik =[]
            for i in range(0,len(self.titik)):
                var_titik = []
                for j in range(0,len(self.titik[i])):
                    var_titik.append(self.titik[i][j] + int(self.arah_value.get()))

                titik.append(var_titik)
            
            if(self.CLICKED_BUTTON == "oval"):
                self.use_oval(titik)
            elif(self.CLICKED_BUTTON == "kotak"):
                self.use_kotak(titik)    
            elif(self.CLICKED_BUTTON == "segitiga"):    
                self.use_segitiga(titik)
        
        elif(self.arah_button.get() == "Bawah"):
            titik = []
            
            for i in range(0, len(self.titik)):
                var_titik =[]
                for j in range(0,len(self.titik[i])):
                    if j%2 == 1:
                        var_titik.append(self.titik[i][j] + int(self.arah_value.get()))
                    else:
                        var_titik.append(self.titik[i][j])
                titik.append(var_titik)
            
            # Untuk mengaplikasikan pergeseran sesuai bentuk
            if(self.CLICKED_BUTTON == "oval"):
                self.use_oval(titik)
            elif(self.CLICKED_BUTTON == "kotak"):
                self.use_kotak(titik)    
            elif(self.CLICKED_BUTTON == "segitiga"):    
                self.use_segitiga(titik)
        
        elif(self.arah_button.get() == "Kiri Bawah"):
            titik = []
            for i in range(0, len(self.titik)):
                var_titik =[]
                for j in range(0,len(self.titik[i])):
                    if j%2 == 1:
                        var_titik.append(self.titik[i][j] + int(self.arah_value.get()))
                    elif j%2 == 0:
                        var_titik.append(self.titik[i][j] - int(self.arah_value.get()))
                titik.append(var_titik)
            
            # Untuk mengaplikasikan pergeseran sesuai bentuk
            if(self.CLICKED_BUTTON == "oval"):
                self.use_oval(titik)
            elif(self.CLICKED_BUTTON == "kotak"):
                self.use_kotak(titik)    
            elif(self.CLICKED_BUTTON == "segitiga"):    
                self.use_segitiga(titik)
        
        self.print_titik()

# OTW Fungsi :
# Perubahan tebal shape
# Rotasi shape
    def rotasi(self):
        sudut = math.radians(int(self.rotasi_value.get()))
        cos_val = math.cos(sudut)
        sin_val = math.sin(sudut)
        cx ,cy = self.center
        titik = []

        for x_lama , y_lama in self.titik:
            x_lama -= cx
            y_lama -= cy
            x_baru = x_lama * cos_val - y_lama * sin_val
            y_baru = x_lama * sin_val + y_lama * cos_val
            titik.append([x_baru + cx, y_baru + cy])
        
        if(self.CLICKED_BUTTON == "oval"):
            self.use_oval(titik)
        elif(self.CLICKED_BUTTON == "kotak"):
            self.use_kotak(titik)    
        elif(self.CLICKED_BUTTON == "segitiga"):    
            self.use_segitiga(titik)
# Scaling shape


if __name__ == '__main__':
    Paint()

