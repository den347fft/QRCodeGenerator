import qrcode
from tkinter import *
from tkinter import messagebox,filedialog

def create():
    
    qr = qrcode.QRCode(
            version=1, 
            error_correction=qrcode.constants.ERROR_CORRECT_L,  
            box_size=10, 
            border=4,  
        )
    qr.add_data(text_to_encode.get())
    qr.make(fit=True)
    if bg_fg.get() == "white-black":
        img = qr.make_image(fill_color="white", back_color="black")
    elif bg_fg.get() == "black-white":
        img = qr.make_image(fill_color="black", back_color="white")
    output_file = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("Image Type","*.png")])
    img.save(output_file)

root = Tk()
root.title("QRCodeGenerator")
root['bg'] = "#212625"

text_to_encode = StringVar()
bg_fg = StringVar()
bg_fg.set("black-white")

text_ = Label(text='Write text or url to encode', bg='#212625',fg='#4cedcd',font='Sans 10 bold')
text = Entry(textvariable=text_to_encode,bg="#212625",fg='#4cedcd',font='Sans 10 bold')
chose_bg_fg = OptionMenu(root, bg_fg, "white-black","black-white")
chose_bg_fg.config(bg='#212625',fg='#4cedcd',font='Sans 10 bold')
chose_bg_fg['menu'].config(bg='#212625',font='Sans 10 bold')
btn = Button(text="generate and save",command=create,bg='#212625',fg='#4cedcd',font='Sans 10 bold')

text_.pack()
text.pack()
chose_bg_fg.pack()
btn.pack()

root.mainloop()