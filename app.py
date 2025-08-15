import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from pdf2docx import Converter
import os

# Get Downloads folder
downloads_dir = Path(os.path.join(os.path.expanduser("~"), "Downloads"))

# --- Conversion function ---
def pdf_to_word(raw_file, converted_file):
    try:
        converted = Converter(str(raw_file))
        converted.convert(str(converted_file), start=0, end=None)
        converted.close()
        messagebox.showinfo("✅ Success", f"File converted!\nSaved to:\n{converted_file}")
    except Exception as e:
        messagebox.showerror("❌ Error", f"Conversion failed: {e}")

# --- File select ---
def select_file():
    file_path = filedialog.askopenfilename(
        title="Select PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )
    if file_path:
        raw_file_path = Path(file_path)
        converted_path = downloads_dir / (raw_file_path.stem + ".docx")
        pdf_to_word(raw_file_path, converted_path)

# --- GUI Setup ---
root = tk.Tk()
root.title("📄 PDF to Word Converter")
root.geometry("450x250")
root.resizable(False, False)
root.configure(bg="#f4f4f4")  # Light background

# --- Style ---
style = ttk.Style()
style.theme_use("clam")  # Modern ttk theme

style.configure("TButton",
                font=("Segoe UI", 12),
                padding=10)
style.configure("TLabel",
                font=("Segoe UI", 16),
                background="#f4f4f4",
                foreground="#333")

# --- Widgets ---
title_label = ttk.Label(root, text="PDF ➡ Word Converter")
title_label.pack(pady=20)

upload_button = ttk.Button(root, text="📂 Select PDF", command=select_file)
upload_button.pack(pady=10)

exit_button = ttk.Button(root, text="❌ Exit", command=root.quit)
exit_button.pack(pady=10)

developer_label = tk.Label(root, text="Developer: Alfred", font=("Arial", 10), fg="gray")
developer_label.pack(side="bottom", pady=5)

footer_label = ttk.Label(root, text="Converted files will be saved to Downloads 📥",
                         font=("Segoe UI", 10),
                         foreground="#555")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
