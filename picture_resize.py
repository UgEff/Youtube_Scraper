from PIL import Image
import os

def resize_image(image_path, output_path):
    imag = Image.open(image_path)
    width, height = imag.size
    print(f"Original size: {width}x{height}")
    new_size = min(width, height)
    print(f"New size (smallest dimension for cropping): {new_size}")
    left = (width - new_size) // 2
    top = (height - new_size) // 2
    right = (width + new_size) // 2
    bottom = (height + new_size) // 2
    imag_cropped = imag.crop((left, top, right, bottom))
    imag_resized = imag_cropped.resize((new_size, new_size))
    imag_resized.save(output_path)
    print(f"Image processed and saved to {output_path}")

