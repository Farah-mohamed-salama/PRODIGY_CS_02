import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Key for encryption and decryption
encryption_key = 0xAB  

def encrypt_image(input_image_path, output_image_path):
    try:
        image = Image.open(input_image_path)
        width, height = image.size

        # Create a new image to store the encrypted image
        encrypted_image = Image.new("RGB", (width, height))

        # Loop through each pixel in the image
        for x in range(width):
            for y in range(height):
                # Get the RGB values of the current pixel
                r, g, b = image.getpixel((x, y))

                # Encrypt the pixel values using XOR cipher
                r ^= encryption_key
                g ^= encryption_key
                b ^= encryption_key

                # Set the encrypted pixel value in the encrypted image
                encrypted_image.putpixel((x, y), (r, g, b))

        # Save the encrypted image
        encrypted_image.save(output_image_path)
        print("Image encrypted successfully!")
        return True
    except Exception as e:
        print("Error encrypting image:", str(e))
        return False

def decrypt_image(input_image_path, output_image_path):
    try:
        # Open the encrypted image
        encrypted_image = Image.open(input_image_path)
        width, height = encrypted_image.size

        # Create a new image to store the decrypted image
        decrypted_image = Image.new("RGB", (width, height))

        # Loop through each pixel in the image
        for x in range(width):
            for y in range(height):
                # Get the RGB values of the current pixel
                r, g, b = encrypted_image.getpixel((x, y))

                # Decrypt the pixel values using XOR cipher (XOR with the same key)
                r ^= encryption_key
                g ^= encryption_key
                b ^= encryption_key

                # Set the decrypted pixel value in the decrypted image
                decrypted_image.putpixel((x, y), (r, g, b))

        # Save the decrypted image
        decrypted_image.save(output_image_path)
        print("Image decrypted successfully!")
        return True
    except Exception as e:
        print("Error decrypting image:", str(e))
        return False

class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryptor")

        # Create buttons
        self.encrypt_button = tk.Button(root, text="Encrypt Image", command=self.encrypt)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(root, text="Decrypt Image", command=self.decrypt)
        self.decrypt_button.pack(pady=10)

    def encrypt(self):
        input_image_path = filedialog.askopenfilename()
        if input_image_path:
            output_image_path = filedialog.asksaveasfilename(defaultextension=".png")
            if output_image_path:
                if encrypt_image(input_image_path, output_image_path):
                    tk.messagebox.showinfo("Success", "Image encrypted successfully!")
                else:
                    tk.messagebox.showerror("Error", "Failed to encrypt image.")

    def decrypt(self):
        input_image_path = filedialog.askopenfilename()
        if input_image_path:
            output_image_path = filedialog.asksaveasfilename(defaultextension=".png")
            if output_image_path:
                if decrypt_image(input_image_path, output_image_path):
                    tk.messagebox.showinfo("Success", "Image decrypted successfully!")
                else:
                    tk.messagebox.showerror("Error", "Failed to decrypt image.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()
