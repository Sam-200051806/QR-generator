import pyqrcode
from tkinter import * 
from PIL import ImageTk,Image
def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file,scale = 8)
    ima = ImageTk.PhotoImage(Image.open(file))
    image_label = Label(image = ima)
    image_label.image = ima
    canvas.create_window(200,450,window=image_label)

root = Tk()
canvas = Canvas(root,width=400,height=600)
canvas.pack()
app_label = Label(root,text="Qr Code Generator",fg="Blue",font=(300))
canvas.create_window(200,50,window=app_label)
name_label = Label(root,text="Link name")
canvas.create_window(200,100,window=name_label)
link_label = Label(root,text="Link")
canvas.create_window(200,160,window=link_label)
button = Button(root,text="Quit",command=root.quit)
canvas.create_window(300,160,window=button)
name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200,130,window=name_entry)
canvas.create_window(200,190,window=link_entry)
button_qr = Button(text="Generator Qr Code",command=generate)
canvas.create_window(200,230,window=button_qr)
root.mainloop()