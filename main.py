from tkinter import *
from PIL import Image, ImageFont, ImageDraw

def create_image():
    with Image.open("/Users/maxwellwhite/Documents/PythonPractice/Final_Projects/watermark/bellingrath-gardens-alabama-landscape-scenic-158063.jpeg").convert("RGBA") as base:

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("Arial", 100)
        # get a drawing context
        d = ImageDraw.Draw(txt)

        d.text((base.size[0]/2, base.size[1]/2), entry_text.get(), font=fnt, fill=(255, 255, 255, 128), anchor="ms")
        d.text((base.size[0]/2, base.size[1]/5), entry_text.get(), font=fnt, fill=(255, 255, 255, 128), anchor="ms")
        d.text((base.size[0]/2, base.size[1]/1.25), entry_text.get(), font=fnt, fill=(255, 255, 255, 128), anchor="ms")

        out = Image.alpha_composite(base, txt)

        out.show()

window = Tk()
window.title("Watermark App")
window.config(padx=100, pady=50)

title = Label(text="Watermark App")
title.grid(column=0, row=0)
title.config(pady=20)

entry_text = Entry()
entry_text.grid(column=0, row=1)

start_button = Button(text="Start", command=create_image)
start_button.grid(column=0, row=2)

window.mainloop()
