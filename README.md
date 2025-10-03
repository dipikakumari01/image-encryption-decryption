# image-encryption-decryption
A Python project to encrypt and decrypt images using simple cryptography techniques.
# 🔐 Image Encryption & Decryption

A Python GUI-based project to **encrypt and decrypt images** using a secret key.  
Built with Tkinter and Pillow, this app demonstrates simple cryptography with an interactive user interface.

---

## 💡 Overview
This project allows users to encrypt an image into an unreadable format and then decrypt it back to its original form using a secret key (1–255).  
It also provides a **side-by-side preview** of the original and processed image, making it beginner-friendly and visually intuitive.

---

## 🛠 Features
- GUI interface built with **Tkinter** (dark theme)  
- Browse image files (JPG, PNG, JPEG)  
- **Encrypt images** using XOR with a secret key (1–255)  
- **Decrypt back** to the original image  
- Side-by-side image preview (original vs encrypted/decrypted)  
- **Drag-and-drop support** for images (Windows only)  

---

## 💻 Tech Stack
- **Python** – Core language  
- **Tkinter** – GUI framework  
- **Pillow (PIL)** – Image processing  
- **OS** – File handling  
- **tkinterdnd2** – Drag-and-drop support  

---
## 🚀 How to Run
1.  **Clone the repo**
    ```bash
    git clone https://github.com/dipikakumar101/image-encryption-decryption.git
    ```
2.  **Navigate to the project folder**
    ```bash
    cd image-encryption-decryption
    ```
3.  **Install dependencies**
    ```bash
    pip install pillow tkinterdnd2
    ```
4.  **Run the application**
    ```bash
    python image_encryption.py
    ```

## 📸 Screenshots
![Encrypted Image](screenshots/demo_encrypt.png)
![Decrypted Image](screenshots/demo_decrypt.png)

## ✅ Author
**Dipika Kumari** – B.Tech Student | Cybersecurity Enthusiast | Python Developer  
[GitHub Profile](https://github.com/dipikakumar101)
