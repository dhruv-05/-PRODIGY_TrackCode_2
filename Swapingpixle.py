from tkinter import Tk, Label, Button, Entry, filedialog, StringVar, messagebox
from PIL import Image
import os

# Function to encrypt the image
def encrypt_image(image_path, key, output_path):
    try:
        image = Image.open(image_path)
        pixels = image.load()

        for i in range(image.width):
            for j in range(image.height):
                pixel = pixels[i, j]
                if len(pixel) == 3:
                    r, g, b = pixel
                    pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
                elif len(pixel) == 4:
                    r, g, b, a = pixel
                    pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256, a)

        image.save(output_path)
        print(f"Encrypted image saved to {output_path}")
    except Exception as e:
        print(f"Error during encryption: {e}")

# Function to decrypt the image
def decrypt_image(image_path, key, output_path):
    try:
        image = Image.open(image_path)
        pixels = image.load()

        for i in range(image.width):
            for j in range(image.height):
                pixel = pixels[i, j]
                if len(pixel) == 3:
                    r, g, b = pixel
                    pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
                elif len(pixel) == 4:
                    r, g, b, a = pixel
                    pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256, a)

        image.save(output_path)
        print(f"Decrypted image saved to {output_path}")
    except Exception as e:
        print(f"Error during decryption: {e}")

# GUI class definition
class ImageEncryptionTool:
    def __init__(self, master):
        self.master = master
        master.title("Image Encryption Tool")

        self.label = Label(master, text="Image Encryption and Decryption")
        self.label.pack()

        self.key_label = Label(master, text="Key:")
        self.key_label.pack()

        self.key_entry = Entry(master)
        self.key_entry.pack()

        self.encrypt_button = Button(master, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack()

        self.decrypt_button = Button(master, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack()

        self.image_path = StringVar()
        self.image_label = Label(master, text="No image selected")
        self.image_label.pack()

        self.select_image_button = Button(master, text="Select Image", command=self.select_image)
        self.select_image_button.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif"), ("All files", "*.*")])
        if file_path:
            self.image_path.set(file_path)
            self.image_label.config(text=os.path.basename(file_path))

    def encrypt(self):
        key = self.key_entry.get()
        if not key.isdigit():
            messagebox.showerror("Error", "Key must be an integer")
            return

        key = int(key)
        if self.image_path.get():
            output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if output_path:
                encrypt_image(self.image_path.get(), key, output_path)
                messagebox.showinfo("Success", f"Image encrypted successfully and saved to {output_path}")
        else:
            messagebox.showerror("Error", "No image selected")

    def decrypt(self):
        key = self.key_entry.get()
        if not key.isdigit():
            messagebox.showerror("Error", "Key must be an integer")
            return

        key = int(key)
        if self.image_path.get():
            output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if output_path:
                decrypt_image(self.image_path.get(), key, output_path)
                messagebox.showinfo("Success", f"Image decrypted successfully and saved to {output_path}")
        else:
            messagebox.showerror("Error", "No image selected")

# Main application
if __name__ == "__main__":
    root = Tk()
    image_encryption_tool = ImageEncryptionTool(root)
    root.mainloop()
