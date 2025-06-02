#!/usr/bin/env python3

from PIL import Image
import os

# Define source and destination directories
src_dir = os.path.expanduser("~/coursera/C6_ARWT/M1/images")
dst_dir = os.path.expanduser("~/coursera/C6_ARWT/M1/output")

# Create destination directory if it doesn't exist
os.makedirs(dst_dir, exist_ok=True)

# Process each .tiff file in the source directory
for filename in os.listdir(src_dir):
    if filename.lower().endswith("_48dp"):
        file_path = os.path.join(src_dir, filename)
        
        # Open the image
        with Image.open(file_path) as img:
            # Rotate 90 degrees clockwise
            img = img.rotate(-90, expand=True)
            # Resize to 128x128
            img = img.resize((128, 128))
            # Save as .jpeg in the destination folder
            new_filename = os.path.splitext(filename)[0] + ".jpeg"
            new_file_path = os.path.join(dst_dir, new_filename)
            img.convert("RGB").save(new_file_path, "JPEG")

print("Image processing completed.")