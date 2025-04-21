from PIL import Image
import sys

def reduce_resolution(input_path, output_path, scale=0.5):
    img = Image.open(input_path)
    new_size = (int(img.width * scale), int(img.height * scale))
    img_resized = img.resize(new_size, Image.ANTIALIAS)
    img_resized.save(output_path)
    print(f"Image saved at {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python resize_image.py <input_image> <output_image> <scale>")
        sys.exit(1)

    input_image = sys.argv[1]
    output_image = sys.argv[2]
    scale = float(sys.argv[3])
    
    reduce_resolution(input_image, output_image, scale)
