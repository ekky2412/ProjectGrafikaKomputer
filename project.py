from tkinter import *
import tkinter
import numpy as np
from tkinter import colorchooser
from tkinter.colorchooser import askcolor

class Paint(object):

    DEFAULT_COLOR = 'black'
    CLICKED_BUTTON = ''
    titik = []
    arah_translasi = ["Kiri Atas","Atas","Kanan Atas","Kanan","Kanan Bawah","Bawah","Kiri Bawah","Kiri"]
    
    def __init__(self):
        self.root = Tk()
        
        icon_oval = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\oval.png")
        icon_kotak = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\persegi.png")
        icon_segitiga = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\segitiga.png")

        icon_oval = icon_oval.subsample(3,3)
        icon_kotak = icon_kotak.subsample(3,3)
        icon_segitiga = icon_segitiga.subsample(3,3)
        
        #setting ukuran canvas sebesar 600px x 600px
        self.c = Canvas(self.root,bg='white',width=600,height=600)
        self.c.grid(row=0)

        #Tombol Shape
        self.oval_button = Button(self.root, text="Oval", image=icon_oval ,command=self.use_oval, compound=LEFT)
        self.oval_button.grid(row=1,column=0,sticky=NW,padx=30)
        
        self.kotak_button = Button(self.root, text="Persegi", image=icon_kotak, command=self.use_kotak, compound=LEFT)
        self.kotak_button.grid(row=1,column=0,sticky=W,padx=30)

        self.segitiga_button = Button(self.root, text="Segitiga", image=icon_segitiga, command=self.use_segitiga, compound=LEFT)
        self.segitiga_button.grid(row=1,column=0,sticky=SW,padx=30)

        #Tombol Warna
        self.pick_color_button = Button(self.root, text="Pilih Warna",command=self.pick_color)
        self.pick_color_button.grid(row=0,column=1,sticky=N,padx=30)
        
        self.pick_color_hasil = Button(self.root,background=self.DEFAULT_COLOR)
        self.pick_color_hasil.grid(row=0,column=1,sticky=N,pady=30,ipadx=10)

        #Tombol Translasi
        self.arah_button = StringVar(self.root)
        self.arah_button.set(self.arah_translasi[0])

        self.arah_isi = OptionMenu(self.root,self.arah_button,*self.arah_translasi)
        self.arah_isi.grid(row=0,column=1,sticky=W,padx=100)

        self.arah_value = Spinbox(self.root,width=5,from_=0,to=100,increment=5)
        self.arah_value.grid(column=1,padx=140,row=0,sticky=E)

        self.arah_submit = Button(self.root, text="Apply",command=self.translasi)
        self.arah_submit.grid(column=1,row=0,pady=250,sticky=S)

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
            self.titik = [200,200,400,400]
        else:
            self.titik = titik
        self.c.create_oval(self.titik,fill= self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR,width=2)
        self.CLICKED_BUTTON = "oval"
        self.print_titik()

#Pembuatan Persegi
    def use_kotak(self,titik = None):
        #(x1,y1,x2,y2)
        self.c.delete("all")
        if(titik == None):
            self.titik = [200,200,400,400]
        else:
            self.titik = titik
        self.c.create_rectangle(self.titik,fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR,width=2)
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
            self.titik = [200,400,400,400,300,200]
        else:
            self.titik = titik
        self.c.create_polygon(self.titik, fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR)
        self.CLICKED_BUTTON = "segitiga"
        self.print_titik()

# Untuk memilih warna
    def pick_color(self):
        self.DEFAULT_COLOR = colorchooser.askcolor(title = "Choose color")[1]
        self.onCLick(self.titik)

# Untuk menyimpan button apa yang telah ditekan antara bangun datar
    def onCLick(self,titik):
        if self.CLICKED_BUTTON == 'oval':
            self.c.create_oval(titik,fill= self.DEFAULT_COLOR,width=2,outline=self.DEFAULT_COLOR)
        elif self.CLICKED_BUTTON == 'kotak':
            self.c.create_rectangle(titik,fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR,width=2)
        elif self.CLICKED_BUTTON == 'segitiga':
            self.c.create_polygon(titik, fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR)
        self.pick_color_hasil.configure(bg=self.DEFAULT_COLOR)

# Untuk menulis output koordinat
    def print_titik(self):
        self.print_titik_kotak.delete("1.0",END)
        self.print_titik_kotak.insert(END,self.titik)

# Fungsi pergeseran
    def translasi(self):
        if(self.arah_button.get() == "Kiri"):
            titik = []
            # perulangan untuk mengecek index
            # jika index nya genap, maka dikurangi
            # index genap = koordinat x
            # index ganjil = koordinat y
            for i in range(0, len(self.titik)):
                if i%2 == 0:
                    titik.append(self.titik[i] - int(self.arah_value.get()))
                else:
                    titik.append(self.titik[i])
            
            # Untuk mengaplikasikan pergeseran sesuai bentuk
            if(self.CLICKED_BUTTON == "oval"):
                self.use_oval(titik)
            elif(self.CLICKED_BUTTON == "kotak"):
                self.use_kotak(titik)    
            elif(self.CLICKED_BUTTON == "segitiga"):    
                self.use_segitiga(titik)

        elif(self.arah_button.get() == "Kiri Atas"):
            titik =[x - int(self.arah_value.get()) for x in self.titik]
            
            if(self.CLICKED_BUTTON == "oval"):
                self.use_oval(titik)
            elif(self.CLICKED_BUTTON == "kotak"):
                self.use_kotak(titik)    
            elif(self.CLICKED_BUTTON == "segitiga"):    
                self.use_segitiga(titik)

# Next to do :
# Bagian Atas hingga Kiri Bawah
        elif(self.arah_button.get() == "Atas"):
            self.use_oval(np.subtract(self.titik,self.arah_value.get()))
        elif(self.arah_button.get() == "Kanan Atas"):
            self.use_oval(np.subtract(self.titik,self.arah_value.get())) 
        elif(self.arah_button.get() == "Kanan"):
            self.use_oval(np.subtract(self.titik,self.arah_value.get())) 
        elif(self.arah_button.get() == "Kanan Bawah"):
            self.use_oval(np.subtract(self.titik,self.arah_value.get()))
        elif(self.arah_button.get() == "Bawah"):
            self.use_oval(np.subtract(self.titik,self.arah_value.get()))
        elif(self.arah_button.get() == "Kiri Bawah"):
            self.use_oval(np.subtract(self.titik,self.arah_value.get()))
        
        self.print_titik()

# OTW Fungsi :
# Perubahan tebal shape
# Rotasi shape
# Scaling shape


if __name__ == '__main__':
    Paint()

