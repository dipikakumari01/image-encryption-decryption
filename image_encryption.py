import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# ---------- Function to Encrypt or Decrypt ----------
def encrypt_decrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path).convert("RGB")
        pixels = img.load()
        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        img.save(output_path)
        return output_path
    except Exception as e:
        print(e)
        return None

# ---------- File Dialog ----------
def browse_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
    )
    if filepath:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, filepath)

# ---------- Image Processing ----------
def process_image(mode):
    path = entry_path.get()
    key_str = entry_key.get()

    if not os.path.exists(path):
        messagebox.showerror("Error", "Image path not found.")
        return

    if not key_str.isdigit() or not (1 <= int(key_str) <= 255):
        messagebox.showerror("Error", "Key must be a number between 1 and 255.")
        return

    key = int(key_str)
    filename = os.path.basename(path)
    name, ext = os.path.splitext(filename)
    output_name = f"{name}_{mode.lower()}{ext}"
    output_path = os.path.join(os.path.dirname(path), output_name)

    result = encrypt_decrypt_image(path, output_path, key)

    if result:
        messagebox.showinfo("Success", f"Image {mode}ed successfully!")
        show_side_by_side(path, result, mode)
    else:
        messagebox.showerror("Error", "Something went wrong.")

# ---------- Show Side-by-Side Images ----------
def show_side_by_side(original, result, mode):
    top = tk.Toplevel(root)
    top.title(f"{mode}ed Image Preview")
    top.configure(bg="#1e1e1e")

    # Load and resize both images
    img1 = Image.open(original)
    img2 = Image.open(result)
    img1.thumbnail((300, 300))
    img2.thumbnail((300, 300))

    tk_img1 = ImageTk.PhotoImage(img1)
    tk_img2 = ImageTk.PhotoImage(img2)

    tk.Label(top, text="Original Image", fg="white", bg="#1e1e1e").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(top, text=f"{mode}ed Image", fg="white", bg="#1e1e1e").grid(row=0, column=1, padx=10, pady=5)

    lbl1 = tk.Label(top, image=tk_img1, bg="#1e1e1e")
    lbl1.image = tk_img1
    lbl1.grid(row=1, column=0, padx=10)

    lbl2 = tk.Label(top, image=tk_img2, bg="#1e1e1e")
    lbl2.image = tk_img2
    lbl2.grid(row=1, column=1, padx=10)

# ---------- Drag and Drop File ----------
def drop(event):
    filepath = event.data.replace("{", "").replace("}", "")
    entry_path.delete(0, tk.END)
    entry_path.insert(0, filepath)

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("🔐 Image Encryption & Decryption")
root.geometry("460x380")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Drag-and-drop support (Windows only)
try:
    root.tk.call('tkdnd::drop_target', 'register', root, '*')
    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', drop)
except:
    pass

tk.Label(root, text="🔍 Select Image File", fg="white", bg="#1e1e1e", font=("Arial", 11)).pack(pady=5)
entry_path = tk.Entry(root, width=40, bg="#2d2d2d", fg="white", insertbackground="white")
entry_path.pack(pady=5)
tk.Button(root, text="Browse", command=browse_file, bg="#444", fg="white").pack(pady=5)

tk.Label(root, text="🔑 Encryption Key (1-255)", fg="white", bg="#1e1e1e", font=("Arial", 11)).pack(pady=10)
entry_key = tk.Entry(root, width=10, bg="#2d2d2d", fg="white", insertbackground="white")
entry_key.pack(pady=5)

tk.Button(root, text="Encrypt Image", bg="#4CAF50", fg="white", width=20,
          command=lambda: process_image("Encrypt")).pack(pady=10)

tk.Button(root, text="Decrypt Image", bg="#2196F3", fg="white", width=20,
          command=lambda: process_image("Decrypt")).pack(pady=5)

tk.Label(root, text="💡 Drag & Drop Supported", fg="#bbbbbb", bg="#1e1e1e", font=("Arial", 9)).pack(pady=10)

root.mainloop()
