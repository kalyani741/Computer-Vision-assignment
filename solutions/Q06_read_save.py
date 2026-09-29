"""
Question 6: Read an image and save it with a different filename using OpenCV.

Topic: Basic Image Handling
Key Concepts:
- cv2.imwrite(filename, img): Encodes and saves an OpenCV matrix to a file.
- The file format is determined automatically by the file extension (.png, .jpg, .bmp, etc.).
- PNG provides lossless compression, while JPEG uses lossy compression.
- Returns True if write succeeded, False otherwise.
"""

import os
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q06")
OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q06_saved_image.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q06: Read an image and save it with a different filename")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    # Read the original image
    img = cv2.imread(INPUT_IMAGE_PATH)
    if img is None:
        print("Error: Could not decode image.")
        return

    print(f"Loaded original image: {INPUT_IMAGE_PATH}")
    print(f"Original format: JPEG, Dimensions: {img.shape}")

    # Write to a different filename and format (PNG)
    success = cv2.imwrite(OUTPUT_IMAGE_PATH, img)

    if success:
        print(f"Successfully saved image with new filename to: {OUTPUT_IMAGE_PATH}")
        print(f"File size on disk: {os.path.getsize(OUTPUT_IMAGE_PATH):,} bytes")
    else:
        print(f"Error: Failed to write image to: {OUTPUT_IMAGE_PATH}")

if __name__ == "__main__":
    main()
