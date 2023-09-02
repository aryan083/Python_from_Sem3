from PIL import Image

# Open the image
image = Image.open("D:/Semster 3/funstuff/1.png")

# Convert the image to RGBA mode (if not already)
image = image.convert("RGBA")

# Get the image data as a list of RGBA tuples
image_data = list(image.getdata())

# Create a new image data list with transparency applied
new_image_data = []
transparency_threshold = 200  # Adjust this threshold based on your image

for pixel in image_data:
    r, g, b, a = pixel
    if r > transparency_threshold and g > transparency_threshold and b > transparency_threshold:
        # Set the pixel to fully transparent
        new_pixel = (r, g, b, 0)
    else:
        new_pixel = pixel
    new_image_data.append(new_pixel)

# Create a new image with the edited data
edited_image = Image.new("RGBA", image.size)
edited_image.putdata(new_image_data)

# Save the edited image
edited_image.save("edited_image.png")
