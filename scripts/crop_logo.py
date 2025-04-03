from PIL import Image

# Load the image
image_path = "/workspaces/stasclub/static/images/logo/logo-transparent.png"
output_path = "/workspaces/stasclub/static/images/logo/logo-transparent-cropped.png"
image = Image.open(image_path)

# Calculate cropping dimensions
width, height = image.size
top_crop = height * 0.25
bottom_crop = height * 0.75

# Crop the image
cropped_image = image.crop((0, top_crop, width, bottom_crop))

# Save the cropped image
cropped_image.save(output_path)
print(f"Cropped image saved to {output_path}")
