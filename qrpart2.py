from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
def do():
    linkname = name_entry.get()
    link = link_entry.get()
    file = linkname + ".png"
    url = pyqrcode.create(link)
    url.png(file,scale = 10)
    image = ImageTk.PhotoImage(Image.open(file))
    image_label = Label(root,image=image)
    image_label.image = image
    c.create_window(400,600,window=image_label)
root = Tk()
c = Canvas(root,width=800,height=800)
c.pack()
app_label = Label(root,text="QR karlo scan bdiya bdiya content ke liye",font=(300),fg="Blue")
c.create_window(400,200,window=app_label)
name_label = Label(root,text="Link name",font=(100))
c.create_window(400,250,window=name_label)
link_label = Label(root,text="Link",font=(100))
c.create_window(400,350,window=link_label)
name_entry = Entry(root)
c.create_window(400,300,window=name_entry)
link_entry = Entry(root)
c.create_window(400,400,window=link_entry)
button_create = Button(root,text="Generate Qr code",command=do)
c.create_window(540,400,window=button_create)
button_quit = Button(root,text="Quit",command=root.quit)
c.create_window(700,450,window=button_quit)
root.mainloop()