from PIL import Image

def is_transparent(image_path):
    try:
        img = Image.open(image_path)
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            return True
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

image_path = "edited_image.png"  # Replace with the actual path to your image
if is_transparent(image_path):
    print("The image is transparent.")
else:
    print("The image is not transparent.")
