"""
Question 4: Calculate and print the total number of pixels in an image.

Topic: Basic Image Handling
Key Concepts:
- Spatial Pixels: Total 2D coordinate locations = Height * Width.
- Total Array Elements (img.size): Total values stored = Height * Width * Channels.
- In a color image with 3 channels, each spatial pixel has 3 sub-pixel intensity values (B, G, R).
"""

import os
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q04")
OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIR, "Q04_result.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q04: Calculate and print total number of pixels")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    img = cv2.imread(INPUT_IMAGE_PATH)
    if img is None:
        print("Error: Could not decode image.")
        return

    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2] if len(img.shape) == 3 else 1

    # Calculation 1: Spatial pixel count
    spatial_pixels = height * width

    # Calculation 2: Total intensity values (elements in NumPy array)
    total_elements = img.size  # Equivalent to height * width * channels

    report = (
        f"Image File: input/sample.jpg\n"
        f"Resolution: {width} x {height}\n"
        f"Channels: {channels}\n"
        f"Total Spatial Pixels (Width x Height): {spatial_pixels:,} pixels\n"
        f"Total Array Elements / Byte Values (Width x Height x Channels): {total_elements:,} values\n"
    )

    print(report)

    with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
        f.write("Q04: Total Pixels Report\n" + "=" * 30 + "\n" + report)

    print(f"Results saved to: {OUTPUT_FILE_PATH}")

if __name__ == "__main__":
    main()
