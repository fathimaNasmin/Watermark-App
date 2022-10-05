import tkinter
import tkinter.ttk
from tkinter import filedialog as fd
from tkinter import colorchooser
import customtkinter
from PIL import ImageTk, Image, ImageDraw, ImageFont

window = customtkinter.CTk()
# define the size of app window
window.geometry("1200x600")
window.title("Image Watermarking App")

class MainWindow:
    def __init__(self, master):

        #Button for uploading Image
        self.upload_image = customtkinter.CTkButton(master=master, text="Upload Image", command=self.uploadimage,
                                                    text_font=('Helvetica', 18))
        # self.upload_image.pack()
        self.upload_image.place(height=50, width=150, relx=0.05, rely=0.05)

        self.add_text = customtkinter.CTkButton(master=master, text="Add Watermark", text_font=('Helvetica', 18), command=self.addtext)
        self.add_text.place(height=50, width=150, relx=0.05, rely=0.2)

        # self.save_btn = customtkinter.CTkButton(master=master, text="Save Image", text_font=('Helvetica', 18))
        # self.save_btn.place(height=50, width=150, relx=0.05, rely=0.35)

    # Button upload function
    def uploadimage(self):
        file_type = [('Jpg File', '*.jpg'), ('PNG file', '*.png'), ('Jpeg file', '*.jpeg')]
        self.filename = fd.askopenfilename(filetypes=file_type)
        self.img = Image.open(self.filename).resize((800, 500))

        # Create an object of tkinter ImageTk
        self.new_img = ImageTk.PhotoImage(self.img)
        # Create a Label Widget to display the text or Image
        self.label = tkinter.Label(window)
        self.label.place(relx=0.27, rely=0.03)
        self.label.config(image=self.new_img)


    #AddWatermark Button function
    def addtext(self):
        tw =TextWindow()


    def showwatermark(self, input_text,wm_color):
        img_width, img_height = self.img.size
        draw = ImageDraw.Draw(self.img)
        font_size = int(img_width / 8)
        font = ImageFont.truetype("Arial Unicode.ttf", font_size)
        # find coordinates of watermark
        x, y = int(img_width / 2), int(img_height / 2)
        # Add watermark
        draw.text((x, y), input_text, font=font, fill=wm_color, stroke_width=5, stroke_fill="#222", anchor='ms')
        # self.img.show()

        #save the image and open on the window
        self.img = self.img.save(f"{self.filename}_watermark.jpg")
        self.marked_img = ImageTk.PhotoImage(Image.open(f"{self.filename}_watermark.jpg"))
        self.label.config(image=self.marked_img)


class TextWindow:
    def __init__(self):
        self.text_window = customtkinter.CTkToplevel()
        self.text_window.geometry('500x300')
        self.text_window.minsize(500, 300)
        self.text_window.maxsize(500, 300)
        self.text_window.title("Add Text")

        # Add fields to Add text window
        self.text_label = customtkinter.CTkLabel(master=self.text_window, text="Text", text_font=('Helvetica', 16))
        self.text_label.place(relx=0.05, rely=0.05)
        self.text_entry = customtkinter.CTkEntry(master=self.text_window, placeholder_text="Enter Text Here", width=250,
                                            height=30, corner_radius=5, text_font=('Helvetica', 16))
        self.text_entry.place(relx=0.25, rely=0.05)

        #Button to choose a color
        self.color_entry = customtkinter.CTkEntry(master=self.text_window, placeholder_text="Pick a color", text_font=('Helvetica', 16))
        self.color_entry.place(relx=0.16, rely=0.25)
        self.color_button = customtkinter.CTkButton(master=self.text_window, text="Color Picker", text_font=('Helvetica', 16), command=self.choosecolor)
        self.color_button.place(relx=0.46, rely=0.25)

        # Add button to add the text to image on main window
        self.add_btn = customtkinter.CTkButton(master=self.text_window, text="Add", text_font=('Helvetica', 16), command=self.addbutton)
        self.add_btn.place(relx=0.35, rely=0.55)

    def addbutton(self):
        self.input_text = self.text_entry.get()
        if self.color_entry == "":
            self.color = "#FFF"
        self.color = self.color_entry.get()
        print(self.color)
        print(self.input_text)
        self.text_window.destroy()
        app.showwatermark(self.input_text, self.color)

    def choosecolor(self):
        self.color = colorchooser.askcolor(title="Choose color")
        # print(self.color[1])
        self.color_entry.insert(0, self.color[1])


app = MainWindow(window)
window.mainloop()
