import os
from PIL import Image

# Set folder paths
input_folder = "input_images"
output_folder = "resized_images"
new_size = (300, 300)  # Width x Height

# Check if input folder exists
if not os.path.exists(input_folder):
    print(f" Folder '{input_folder}' not found. Please create it and add some images.")
    exit()

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get list of image files
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if not image_files:
    print("️ No image files found in the input_images folder.")
    exit()

# Resize and save images
for filename in image_files:
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    with Image.open(input_path) as img:
        resized = img.resize(new_size)
        resized.save(output_path)

    print(f" Resized and saved: {filename}")
