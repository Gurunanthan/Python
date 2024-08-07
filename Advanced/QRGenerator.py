import qrcode
import tkinter as tk
from tkinter import filedialog

def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(filename)

def save_qr_code():
    url = url_entry.get()
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        generate_qr_code(url, file_path)
        status_label.config(text="QR code saved successfully!")

root = tk.Tk()
root.title("QR Code Generator")

url_label = tk.Label(root, text="Enter website URL for QR code:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

save_button = tk.Button(root, text="Save QR Code", command=save_qr_code)
save_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
