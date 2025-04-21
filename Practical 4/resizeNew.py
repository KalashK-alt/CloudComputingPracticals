from PIL import Image
import os

input_folder = "images"
output_folder = "resized"
resize_size = (200, 200)  # You can change this

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Resize all images
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img = img.resize(resize_size, Image.Resampling.LANCZOS)


        output_path = os.path.join(output_folder, filename)
        img.save(output_path)
        print(f"Resized: {filename}")
