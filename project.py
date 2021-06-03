from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(object):

    DEFAULT_COLOR = 'black'
    
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
        self.c.grid(row=0,columnspan=5)

        self.oval_button = Button(self.root, text="Oval", image=icon_oval ,command=self.use_oval, compound=LEFT)
        self.oval_button.grid(row=1,column=0)
        
        self.kotak_button = Button(self.root, text="Persegi", image=icon_kotak, command=self.use_kotak, compound=LEFT)
        self.kotak_button.grid(row=1,column=1)

        self.segitiga_button = Button(self.root, text="Segitiga", image=icon_segitiga, command=self.use_segitiga, compound=LEFT)
        self.segitiga_button.grid(row=1,column=3)
        
        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
    
        # self.c.bind('<B1-Motion>', self.paint)
        # self.c.bind('<ButtonRelease-1>', self.reset)

    def use_oval(self):
        #(x1,y1,x2,y2)
        self.c.delete("all")
        self.c.create_oval(10,10,80,80,fill= self.DEFAULT_COLOR,width=2)

    def use_kotak(self):
        #(x1,y1,x2,y2)
        self.c.delete("all")
        self.c.create_rectangle(10,10,110,80,fill=self.DEFAULT_COLOR,width=2)

    def use_segitiga(self):
        #(x1,y1,x2,y2,x3,y3)
        # titik 0 dari kiri atas
        # x = 0 kiri, x = 10 kanan
        # y = 0 atas, y = 10 kebawah
        self.c.delete("all")
        titik = [10,80,80,80,45,10]
        self.c.create_polygon(titik, fill=self.DEFAULT_COLOR)    

if __name__ == '__main__':
    Paint()

