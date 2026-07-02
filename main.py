#QR code generator
import tkinter as tk
from tkinter import messagebox as md
from tkinter import filedialog
import qrcode
from PIL import ImageTk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QR Code Generator")
        #self.root.geometry('400x500')
        self.root.configure(bg="#28A0A0")
        #self.root.iconbitmap('islands-reti.ico') 
        self.title_label = tk.Label(self.root, 
                                    text='enter the text here', 
                                    bg="#74FFF3"
                                    )
        self.title_label.pack()
        
        self.text = tk.Text(
            self.root, 
            width=45, 
            height=3, 
            fg="#F20F0F", 
            bg="#3F7DF9"
        )
        self.text.pack(side='top', pady=10)

        self.butt = tk.Button(
            text='make code', 
            command=self.qr_code_make, 
            bg="#D78D16",
            width=40,
            height=2
        )
        self.butt.pack(pady=5)
        
        self.label = tk.Label(self.root)
        self.label.pack(pady=10)


        self.painting_code = None

    def qr_code_make(self):
        data = self.text.get('1.0', 'end-1c').strip()
        if not data:
            md.showwarning("Empty Input", "Please enter some text to generate a QR code.")
            return
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.ERROR_CORRECT_L,
                box_size=10,
                border=4
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')
            
            self.painting_code = ImageTk.PhotoImage(img)
            self.label.config(image=self.painting_code)

            file_name = filedialog.asksaveasfilename()
            if not file_name:
                return
            else:
                img.save(file_name + '.png')

            md.showinfo('Success', f'your QR code has been saved as {file_name}.')
        except Exception as e:
            md.showerror('Error', f'Failed to generate QR code/n{e}')

if __name__ == '__main__':
    app = App()
    app.root.mainloop()