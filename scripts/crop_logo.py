from PIL import Image

def crop_image(image_path, output_path, left_crop=0, right_crop=0):
    # Load the image
    image = Image.open(image_path)
    width, height = image.size

    # Calculate cropping dimensions
    left = left_crop
    right = width - right_crop

    # Crop the image
    cropped_image = image.crop((left, 0, right, height))

    # Save the cropped image
    cropped_image.save(output_path)
    print(f"Cropped image saved to {output_path}")

# Crop page_exchanges.webp from the right
crop_image(
    "/workspaces/stasclub/static/images/page_exchanges.webp",
    "/workspaces/stasclub/static/images/page_exchanges_cropped2.webp",
    right_crop=120  # Adjust this value as needed
)

# Crop page_depin.png from the left
crop_image(
    "/workspaces/stasclub/static/images/page_depin.png",
    "/workspaces/stasclub/static/images/page_depin_cropped2.png",
    left_crop=90  # Adjust this value as needed
)
