from PIL import Image

def crop_to_square(image):
    width, height = image.size
    size = min(width, height)
    left = (width - size) // 2
    top = (height - size) // 2
    right = left + size
    bottom = top + size
    return image.crop((left, top, right, bottom))

def crop_center_20_percent(image):
    """Crop 20% from each side of a square image, keeping the center."""
    width, height = image.size
    # Calculate 20% of the size
    crop_amount = int(width * 0.125)  # Since it's square, width == height
    
    # Calculate new boundaries
    left = crop_amount
    top = crop_amount
    right = width - crop_amount
    bottom = height - crop_amount
    
    return image.crop((left, top, right, bottom))

def resize_image(input_path, output_path):
    with Image.open(input_path) as img:
        # Crop to square
        img_square = crop_to_square(img)
        # Crop additional 20% from center
        img_center = crop_center_20_percent(img_square)
        # Save the final image
        img_center.save(output_path, quality=100)

