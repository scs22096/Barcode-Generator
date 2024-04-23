import tkinter as tk
from tkinter import messagebox
import os
import barcode

def generate_barcodes():
    data = text_entry.get("1.0", tk.END).splitlines()
    if data:
        try:
            barcode_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'barcodes')
            os.makedirs(barcode_path, exist_ok=True)
            for i, num in enumerate(data):
                if num.strip():
                    with open(os.path.join(barcode_path, f'barcode_{i}.png'), 'wb') as f:
                        barcode.Code128(num.strip(), writer=barcode.writer.ImageWriter()).write(f, options={'module_width': 0.3, 'module_height': 15})
            messagebox.showinfo("Success", "Barcodes generated and saved on Desktop!")
        except Exception as e:
            messagebox.showerror("Error", f"Error generating barcodes: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter at least one number.")

# GUI
root = tk.Tk()
root.title("Code 128 Barcode Generator")

label = tk.Label(root, text="Enter numbers (one per line):")
label.pack()

text_entry = tk.Text(root, height=10, width=30)
text_entry.pack()

generate_button = tk.Button(root, text="Generate Barcodes", command=generate_barcodes)
generate_button.pack()

root.mainloop()
