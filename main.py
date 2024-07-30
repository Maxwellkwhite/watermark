from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageFont, ImageDraw, ImageTk

original_file_path = '/Users/maxwellwhite/Documents/PythonPractice/Final_Projects/watermark/1.png'

def image_upload():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image.save(file_path)
        messagebox.showinfo("Success", "Image uploaded successfully!")
    else:
        messagebox.showinfo("No file was selected. Please choose a file.")


def create_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image.save(original_file_path)
        messagebox.showinfo("Success", "Image uploaded successfully!")
    else:
        messagebox.showinfo("No file was selected. Please choose a file.")
    with Image.open("Final_Projects/watermark/1.png").convert("RGBA") as base:

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("Arial", base.size[0]/10)
        # get a drawing context
        d = ImageDraw.Draw(txt)

        d.text((base.size[0]/2, base.size[1]/2), entry_text.get(), font=fnt, fill=(255, 255, 255, 128), anchor="ms")
        # d.text((base.size[0]/2, base.size[1]/5), entry_text.get(), font=fnt, fill=(255, 255, 255, 128), anchor="ms")
        # d.text((base.size[0]/2, base.size[1]/1.25), entry_text.get(), font=fnt, fill=(255, 255, 255, 128), anchor="ms")

        out = Image.alpha_composite(base, txt)

        out.show()


window = Tk()
window.title("Watermark App")
window.config(padx=100, pady=50)

title = Label(text="Watermark App")
title.grid(column=0, row=0)
title.config(pady=20)

# img_upload = Button(text="Image Upload", command=image_upload)
# img_upload.grid(column=0, row=1)

entry_text = Entry()
entry_text.grid(column=0, row=2)

start_button = Button(text="Start", command=create_image)
start_button.grid(column=0, row=3)

window.mainloop()
