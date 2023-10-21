import os
import threading
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image


class ImageConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image Format Converter")
        self.root.resizable(width=False, height=False)

        # Input directory label and entry
        self.input_directory_label = tk.Label(self.root, text="Input directory:")
        self.input_directory_entry = tk.Entry(self.root)
        self.input_directory_label.grid(row=0, column=0)
        self.input_directory_entry.grid(row=0, column=1)

        # Output directory label and entry
        self.output_directory_label = tk.Label(self.root, text="Output directory:")
        self.output_directory_entry = tk.Entry(self.root)
        self.output_directory_label.grid(row=1, column=0)
        self.output_directory_entry.grid(row=1, column=1)

        # Browse button for input directory
        self.input_directory_browse_button = tk.Button(self.root, text="Browse", command=self.browse_input_directory)
        self.input_directory_browse_button.grid(row=0, column=2)

        # Browse button for output directory
        self.output_directory_browse_button = tk.Button(self.root, text="Browse", command=self.browse_output_directory)
        self.output_directory_browse_button.grid(row=1, column=2)

        # Conversion direction (JPG to PNG or PNG to JPG)
        self.convert_direction_var = tk.IntVar()
        self.convert_direction_var.set(1)  # Default to JPG to PNG
        self.direction_label = tk.Label(self.root, text="Conversion Direction:")
        self.jpg_to_png_radio = tk.Radiobutton(self.root, text="JPG to PNG", variable=self.convert_direction_var,
                                               value=1)
        self.png_to_jpg_radio = tk.Radiobutton(self.root, text="PNG to JPG", variable=self.convert_direction_var,
                                               value=2)
        self.direction_label.grid(row=2, column=0, columnspan=3)
        self.jpg_to_png_radio.grid(row=3, column=0, columnspan=3)
        self.png_to_jpg_radio.grid(row=4, column=0, columnspan=3)

        # Convert button
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert)
        self.convert_button.grid(row=5, column=0, columnspan=3)

        # Progress bar
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", mode="indeterminate")
        self.progress_bar.grid(row=6, column=0, columnspan=3)

        # Start the mainloop
        self.root.mainloop()

    def browse_input_directory(self):
        input_directory = filedialog.askdirectory(title="Select input directory")
        self.input_directory_entry.delete(0, tk.END)
        self.input_directory_entry.insert(0, input_directory)

    def browse_output_directory(self):
        output_directory = filedialog.askdirectory(title="Select output directory")
        self.output_directory_entry.delete(0, tk.END)
        self.output_directory_entry.insert(0, output_directory)

    def convert(self):
        input_directory = self.input_directory_entry.get()
        output_directory = self.output_directory_entry.get()
        convert_direction = self.convert_direction_var.get()

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        self.progress_bar.start()

        def convert_images():
            for filename in os.listdir(input_directory):
                if convert_direction == 1:  # JPG to PNG
                    if filename.lower().endswith(".jpg"):
                        img = Image.open(os.path.join(input_directory, filename))
                        new_filename = os.path.splitext(filename)[0] + ".png"
                        img.save(os.path.join(output_directory, new_filename), "PNG")
                        print(f"Converted {filename} to {new_filename}")
                        os.remove(os.path.join(input_directory, filename))
                        print(f"Deleted {filename}")
                        self.progress_bar.step(1)
                elif convert_direction == 2:  # PNG to JPG
                    if filename.lower().endswith(".png"):
                        img = Image.open(os.path.join(input_directory, filename))
                        new_filename = os.path.splitext(filename)[0] + ".jpg"
                        img.save(os.path.join(output_directory, new_filename), "JPEG")
                        print(f"Converted {filename} to {new_filename}")
                        os.remove(os.path.join(input_directory, filename))
                        print(f"Deleted {filename}")
                        self.progress_bar.step(1)

            self.progress_bar.stop()
            messagebox.showinfo(title="Conversion complete!",
                                message="All images have been converted and saved to the output directory.")
        thread = threading.Thread(target=convert_images)
        thread.start()
        


if __name__ == "__main__":
    ImageConverter()
