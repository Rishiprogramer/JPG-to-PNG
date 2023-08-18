import os
from PIL import Image

input_directory = "path/to/orignal/directory"
output_directory = "path/to/out/dirctory"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through all files in the input directory
for filename in os.listdir(input_directory):
    if filename.lower().endswith(".jpg"):
        img = Image.open(os.path.join(input_directory, filename))
        new_filename = os.path.splitext(filename)[0] + ".png"
        img.save(os.path.join(output_directory, new_filename), "PNG")
        print(f"Converted {filename} to {new_filename}")
        os.remove(os.path.join(input_directory, filename))
        print(f"Deleted {filename}")

print("Conversion complete!")
