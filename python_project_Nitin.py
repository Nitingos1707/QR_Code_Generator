import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk

class QRCodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")

        self.label_text = tk.StringVar()
        self.label_text.set("Enter text to generate QR code:")

        self.label = ttk.Label(master, textvariable=self.label_text)
        self.label.pack(pady=10)

        self.text_entry = ttk.Entry(master, width=40)
        self.text_entry.pack(pady=10)

        self.generate_button = ttk.Button(master, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        self.qr_code_image_label = ttk.Label(master)
        self.qr_code_image_label.pack(pady=10)

    def generate_qr_code(self):
        text_to_encode = self.text_entry.get()

        if text_to_encode:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text_to_encode)
            qr.make(fit=True)

            qr_code_img = qr.make_image(fill_color="black", back_color="white")

            # Save the generated QR code image
            qr_code_img.save("generated_qr_code.png")

            # Display the generated QR code image in the GUI
            image = Image.open("generated_qr_code.png")
            photo = ImageTk.PhotoImage(image)
            self.qr_code_image_label.config(image=photo)
            self.qr_code_image_label.image = photo

            self.label_text.set("QR Code generated successfully!")
        else:
            self.label_text.set("Please enter text before generating QR code.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
