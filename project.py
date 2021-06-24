from tkinter import *
import numpy as np
import math
from tkinter import colorchooser
from tkinter.colorchooser import askcolor
from tkinter.ttk import Style

from numpy.lib.function_base import append

class Paint(object):

    WIDTH = 600
    HEIGHT = 600
    center = [WIDTH/2,HEIGHT/2]
    x = y = 0
    DEFAULT_COLOR = 'black'
    DEFAULT_COLOR_OUTLINE = 'black'
    CLICKED_BUTTON = ''
    titik = []
    pilihan_tipe = ["default","dash","dash dot","dash dot dot"]
    tipe_dipilih = "default"
    tipe_dash = {
        "default":(),
        "dash":(4,2),
        "dash dot":(6,4,1,4),
        "dash dot dot":(6,4,1,4,1,4)
    }
    arah_translasi = ["Kiri Atas","Atas","Kanan Atas","Kanan","Kanan Bawah","Bawah","Kiri Bawah","Kiri"]
    
    def __init__(self):
        self.root = Tk()
        
        icon_oval = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\oval.png")
        icon_kotak = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\persegi.png")
        icon_segitiga = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\segitiga.png")
        icon_ketupat = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\ketupat.png")
        icon_segilima = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\segilima.png")

        # Ikon Panah
        self.icon_arrow_up = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\\arrow-up.png")
        self.icon_arrow_down = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\\arrow-down.png")
        self.icon_arrow_left = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\\arrow-left.png")
        self.icon_arrow_right = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\\arrow-right.png")
        self.icon_arrow_left_up = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\\arrow-left-up.png")
        self.icon_arrow_left_down = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\\arrow-left-down.png")
        self.icon_arrow_right_up = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\\arrow-right-up.png")
        self.icon_arrow_right_down = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\\arrow-right-down.png")

        # Ikon Tambahan
        icon_zoom = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\magnifier.png")
        icon_rotate = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\\rotate.png")
        icon_pen = PhotoImage(file = "D:\KULIAH\Grafika Komputer\Project Akhir\images\pen.png")

        icon_oval = icon_oval.subsample(3,3)
        icon_kotak = icon_kotak.subsample(3,3)
        icon_segitiga = icon_segitiga.subsample(3,3)
        icon_ketupat = icon_ketupat.subsample(3,3)
        icon_segilima = icon_segilima.subsample(3,3)
        
        self.icon_arrow_up = self.icon_arrow_up.subsample(4,4)
        self.icon_arrow_down = self.icon_arrow_down.subsample(4,4)
        self.icon_arrow_left = self.icon_arrow_left.subsample(4,4)
        self.icon_arrow_right = self.icon_arrow_right.subsample(4,4)
        self.icon_arrow_left_up = self.icon_arrow_left_up.subsample(4,4)
        self.icon_arrow_left_down = self.icon_arrow_left_down.subsample(4,4)
        self.icon_arrow_right_up = self.icon_arrow_right_up.subsample(4,4)
        self.icon_arrow_right_down = self.icon_arrow_right_down.subsample(4,4)

        icon_zoom = icon_zoom.subsample(4,4)
        icon_rotate = icon_rotate.subsample(4,4)
        icon_pen = icon_pen.subsample(4,4)

        
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

        self.ketupat_button = Button(self.root, text="Belah Ketupat", image=icon_ketupat, command=self.use_ketupat,compound=LEFT)
        self.ketupat_button.grid(row=1,column=0,sticky=NW,padx=30,pady=50)

        self.segilima_button = Button(self.root, text="Segilima", image=icon_segilima, command=self.use_segilima,compound=LEFT)
        self.segilima_button.grid(row=1,column=0,sticky=SW,padx=30,pady=50)

        #Tombol Pen
        self.pen_button = Button(self.root, text="Pen", command=self.use_pen_first, image=icon_pen, compound=LEFT)
        self.pen_button.grid(row=0,column=1,sticky=NW,padx=30,pady=10)

        self.tipe_dash_value = StringVar(self.root)
        self.tipe_dash_value.set(self.pilihan_tipe[0])

        self.pilihan_dash_button = OptionMenu(self.root,self.tipe_dash_value,*self.pilihan_tipe,command=self.tipe_dash_function)
        self.pilihan_dash_button.grid(row=0,column=1,sticky=NW,padx=30,pady=45)

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

        self.arah_isi = OptionMenu(self.root,self.arah_button,*self.arah_translasi,command=self.ganti_icon_panah)
        self.arah_isi.grid(row=0,column=1,sticky=W,padx=100)

        self.arah_value = Spinbox(self.root,width=5,from_=0,to=100,increment=5)
        self.arah_value.grid(column=1,padx=140,row=0,sticky=E)

        self.arah_submit = Button(self.root, text="Apply",command=self.translasi)
        self.arah_submit.grid(column=1,row=0,pady=250,sticky=S)

        self.arah_icon = Button(self.root, image=self.icon_arrow_left_up,border=0)
        self.arah_icon.grid(column=1,row=0,padx=70,sticky=W)

        #Tombol Rotasi
        self.rotasi_button = Button(self.root, text="Rotate",command=self.rotasi, image=icon_rotate, compound=LEFT)
        self.rotasi_button.grid(column=0,row=1,sticky=NE,padx=300,pady=10)

        self.rotasi_value = Spinbox(self.root,width=5,from_=-100,to=100,increment=5)
        self.rotasi_value.grid(column=0,padx=240,row=1,sticky=NE,pady=13)

        #Tombol Scaling
        self.zoom_value = Scale(self.root,from_=100,to=-100)
        self.zoom_value.grid(column=1,row=0,sticky=S,pady=40)

        self.zoom_button = Button(self.root,text="Zoom",command=self.zoom,image=icon_zoom, compound=LEFT)
        self.zoom_button.grid(column=1,row=0,sticky=S,pady=10)

        #Tombol Output Koordinat
        self.print_titik_kotak = Text(self.root, height=15, width=50)
        self.print_titik_kotak.grid(row=1,column=1)

        #Binding klik kiri ke canvas
        self.c.bind("<ButtonPress-1>", self.on_button_press)
        self.c.bind("<ButtonRelease-1>",self.on_button_release)
        
        self.setup()
        self.root.mainloop()
        
    def setup(self):
        self.old_x = None
        self.old_y = None

        self.use_oval()
        # self.c.bind('<B1-Motion>', self.paint)
        # self.c.bind('<ButtonRelease-1>', self.reset)

#Event Mouse Click dan Release
    def on_button_press(self, event):
        self.x = event.x
        self.y = event.y

    def on_button_release(self, event):
        titik = [[self.x, self.y]]
        titik.append([event.x, event.y])

        if(self.CLICKED_BUTTON == "oval"):
            self.use_oval(titik)
        elif(self.CLICKED_BUTTON == "kotak"):
            self.use_kotak(titik)    
        elif(self.CLICKED_BUTTON == "segitiga"):    
            self.use_segitiga(titik)
        elif(self.CLICKED_BUTTON == "pen"):
            self.use_pen(titik)
        self.titik = titik
        # self.print_titik()

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
            self.titik = [[200,200],[200,400],[400,400],[400,200]]
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

#Pembuatan Belah Ketupat
    def use_ketupat(self,titik = None):
        self.c.delete("all")
        if(titik == None):
            self.titik = [[200,300],[300,200],[400,300],[300,400]]
        else:
            self.titik = titik
        self.c.create_polygon(self.titik, fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR_OUTLINE)
        self.CLICKED_BUTTON = "belah ketupat"
        self.print_titik()

#Pembuatan Segilima
    def use_segilima(self,titik = None):
        self.c.delete("all")
        if(titik == None):
            # Perlu dicari koordinat yang benar
            self.titik = [[150,300],[300,180],[450,300],[380,450],[220,450]]
        else:
            self.titik = titik
        self.c.create_polygon(self.titik, fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR_OUTLINE)
        self.CLICKED_BUTTON = "segilima"
        self.print_titik()

# Fungsi tombol pen
    def use_pen_first(self):
        self.c.delete("all")
        self.CLICKED_BUTTON = "pen"

    def use_pen(self,titik):
        self.titik = titik
        if(self.tipe_dipilih == "default"):
            self.c.create_line(titik,fill=self.DEFAULT_COLOR_OUTLINE)
        else:
            self.c.create_line(titik, dash=self.tipe_dash[self.tipe_dipilih],fill=self.DEFAULT_COLOR_OUTLINE)
        self.print_titik()
        
# Untuk memilih warna
    def pick_color(self):
        self.DEFAULT_COLOR = colorchooser.askcolor(title = "Choose color")[1]
        self.onCLick(self.titik)

    def pick_color_outline(self):
        self.DEFAULT_COLOR_OUTLINE = colorchooser.askcolor(title = "Choose color")[1]
        self.onCLick(self.titik)

# Memilih tipe dash
    def tipe_dash_function(self,arah = "default"):
        self.tipe_dipilih = arah

# Untuk menyimpan button apa yang telah ditekan antara bangun datar
    def onCLick(self,titik):
        if self.CLICKED_BUTTON == 'oval':
            self.c.create_oval(titik,fill= self.DEFAULT_COLOR,width=2,outline=self.DEFAULT_COLOR_OUTLINE)
        elif self.CLICKED_BUTTON == 'kotak':
            self.c.create_polygon(titik,fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR_OUTLINE,width=2)
        elif (self.CLICKED_BUTTON == 'segitiga' or self.CLICKED_BUTTON == 'belah ketupat' or self.CLICKED_BUTTON == 'segilima'):
            self.c.create_polygon(titik, fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR_OUTLINE)
        # elif self.CLICKED_BUTTON == 'belah ketupat':
        #     self.c.create_polygon(titik, fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR_OUTLINE)
        # elif self.CLICKED_BUTTON == 'segilima':
        #     self.c.create_polygon(titik, fill=self.DEFAULT_COLOR,outline=self.DEFAULT_COLOR_OUTLINE)        
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
                print(var_titik)        

        elif(self.arah_button.get() == "Kiri Atas"):
            titik =[]
            for i in range(0,len(self.titik)):
                var_titik = []
                for j in range(0,len(self.titik[i])):
                    var_titik.append(self.titik[i][j] - int(self.arah_value.get()))  
                titik.append(var_titik)

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
        
        elif(self.arah_button.get() == "Kanan Bawah"):
            titik =[]
            for i in range(0,len(self.titik)):
                var_titik = []
                for j in range(0,len(self.titik[i])):
                    var_titik.append(self.titik[i][j] + int(self.arah_value.get()))

                titik.append(var_titik)
        
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

        self.c.delete("all")    
        # Untuk mengaplikasikan pergeseran sesuai bentuk    
        if(self.CLICKED_BUTTON == "oval"):
            self.use_oval(titik)
        elif(self.CLICKED_BUTTON == "kotak"):
            self.use_kotak(titik)    
        elif(self.CLICKED_BUTTON == "segitiga"):    
            self.use_segitiga(titik)
        elif(self.CLICKED_BUTTON == "belah ketupat"):    
            self.use_ketupat(titik)
        elif(self.CLICKED_BUTTON == "segilima"):    
            self.use_segilima(titik)
        elif(self.CLICKED_BUTTON == "pen"):
            self.use_pen(titik)    
        print(self.titik)
        self.print_titik()

# Perubahan Icon Translasi
    def ganti_icon_panah(self,arah):
        if(arah == "Kiri Atas"):
            self.arah_icon.config(image=self.icon_arrow_left_up)
        elif(arah == "Atas"):
            self.arah_icon.config(image=self.icon_arrow_up)
        elif(arah == "Kanan Atas"):
            self.arah_icon.config(image=self.icon_arrow_right_up)
        elif(arah == "Kanan"):
            self.arah_icon.config(image=self.icon_arrow_right)
        elif(arah == "Kanan Bawah"):
            self.arah_icon.config(image=self.icon_arrow_right_down)
        elif(arah == "Bawah"):
            self.arah_icon.config(image=self.icon_arrow_down)
        elif(arah == "Kiri Bawah"):
            self.arah_icon.config(image=self.icon_arrow_left_down)
        elif(arah == "Kiri"):
            self.arah_icon.config(image=self.icon_arrow_left)

# OTW Fungsi :
# Perubahan tebal shape
# Rotasi shape
    def rotasi(self):
        if(self.CLICKED_BUTTON != "oval"):
            sudut = math.radians(int(self.rotasi_value.get()))
            cos_val = math.cos(sudut)
            sin_val = math.sin(sudut)

            tx = 0
            ty = 0
            
            for x in range(len(self.titik)):
                tx += self.titik[x][0]
                ty += self.titik[x][1]
                
            tx = round(tx/len(self.titik))
            ty = round(ty/len(self.titik))
            
            cx ,cy = tx,ty
            titik = []

            for x_lama , y_lama in self.titik:
                x_lama -= cx
                y_lama -= cy
                x_baru = x_lama * cos_val - y_lama * sin_val
                y_baru = x_lama * sin_val + y_lama * cos_val
                titik.append([x_baru + cx, y_baru + cy])
            
            self.c.delete("all")
            if(self.CLICKED_BUTTON == "oval"):
                self.use_oval(titik)
            elif(self.CLICKED_BUTTON == "kotak"):
                self.use_kotak(titik)    
            elif(self.CLICKED_BUTTON == "segitiga"):    
                self.use_segitiga(titik)
            elif(self.CLICKED_BUTTON == "belah ketupat"):    
                self.use_ketupat(titik)
            elif(self.CLICKED_BUTTON == "segilima"):    
                self.use_segilima(titik)
            elif(self.CLICKED_BUTTON == "pen"):
                self.use_pen(titik)    
            

# Scaling shape
    def zoom(self):
        tx = 0
        ty = 0
        
        for x in range(len(self.titik)):
            tx += self.titik[x][0]
            ty += self.titik[x][1]
            
        tx = round(tx/len(self.titik))
        ty = round(ty/len(self.titik))

        titik = []

        ukuran_perbesar = (self.zoom_value.get()/100) + 1

        for x_lama , y_lama in self.titik:
            x_lama -= tx
            y_lama -= ty

            x_baru = ukuran_perbesar * x_lama
            y_baru = ukuran_perbesar * y_lama

            x_baru += tx
            y_baru += ty

            titik.append([x_baru, y_baru])

        if(self.CLICKED_BUTTON == "oval"):
            self.use_oval(titik)
        elif(self.CLICKED_BUTTON == "kotak"):
            self.use_kotak(titik)    
        elif(self.CLICKED_BUTTON == "segitiga"):    
            self.use_segitiga(titik)
        elif(self.CLICKED_BUTTON == "belah ketupat"):    
            self.use_ketupat(titik)
        elif(self.CLICKED_BUTTON == "segilima"):    
            self.use_segilima(titik)
        elif(self.CLICKED_BUTTON == "pen"):
            self.use_pen(titik)    

if __name__ == '__main__':
    Paint()

