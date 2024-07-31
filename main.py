from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageFont, ImageDraw, ImageTk
from customtkinter import CTkEntry, CTk, CTkLabel, CTkButton
import customtkinter

original_file_path = '/Users/maxwellwhite/Documents/PythonPractice/Final_Projects/watermark/1.png'


def create_image():
    file_path = filedialog.askopenfilename(filetypes=[("Allowed Types", '*.jpeg *.jpg *.png')])
    if len(file_path):
        image = Image.open(file_path)
        image.save(original_file_path)
        messagebox.showinfo("Success", "Image uploaded successfully!")
    else:
        messagebox.showinfo("No file was selected. Please choose a file.")
    with Image.open("Final_Projects/watermark/1.png").convert("RGBA") as base:

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        fnt = ImageFont.truetype("Arial", base.size[0]/10)
        draw = ImageDraw.Draw(txt)

        draw.text((base.size[0]/2, base.size[1]/2), entry_text.get(), font=fnt, fill=(255, 255, 255, 128), anchor="ms")

        out = Image.alpha_composite(base, txt)

        out.show()

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

window = CTk()
window.title("Watermark App")
window.config(padx=100, pady=50)

title = CTkLabel(text="The Mark of Water", master=window, font=("Arial",30, "bold"))
title.grid(column=0, row=0, pady=10, columnspan=2)

instructions = CTkLabel(text="Type your watermark below, then click the button.", master=window, font=("Arial",15))
instructions.grid(column=0, row=1, pady=10, columnspan=2)
# entry_label = CTkLabel(text="Enter Watermark Text Here:", master=window)
# entry_label.grid(column=1, row=1)

entry_text = CTkEntry(master=window, placeholder_text="Watermark Text",)
entry_text.grid(column=0, row=2, padx=10)

start_button = CTkButton(text="Find Image", command=create_image, master=window)
start_button.grid(column=1, row=2)

window.mainloop()
