import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

class TextFromImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text from Image App")

        self.create_widgets()

    def create_widgets(self):
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=10)

        self.image_label = tk.Label(self.image_frame)
        self.image_label.grid(row=0, column=0)

        self.browse_button = tk.Button(self.image_frame, text="Browse Image", command=self.load_image)
        self.browse_button.grid(row=1, column=0, pady=5)

        self.extract_button = tk.Button(self.image_frame, text="Extract Text", command=self.extract_text)
        self.extract_button.grid(row=2, column=0, pady=5)

        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack(pady=10)

        self.text_label = tk.Label(self.text_frame, wraplength=500, justify="left")
        self.text_label.grid(row=0, column=0)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((400, 400))  # Menyesuaikan ukuran gambar agar sesuai dengan label
            photo = ImageTk.PhotoImage(image)

            # Menampilkan gambar di label
            self.image_label.config(image=photo)
            self.image_label.image = photo

            # Menyimpan path gambar
            self.image_path = file_path

    def extract_text(self):
        if hasattr(self, 'image_path'):
            image = Image.open(self.image_path)
            text = pytesseract.image_to_string(image)

            # Menampilkan teks hasil ekstraksi
            self.text_label.config(text=text)
        else:
            self.text_label.config(text="Pilih gambar terlebih dahulu.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextFromImageApp(root)
    root.mainloop()
