"""
Question 20: Create and display a grayscale intensity ramp whose intensity
             gradually changes from 0 to 255.

Topic: Pixel & Image Representation
Key Concepts:
- Intensity Ramp / Gradient: A programmatic visualization showing smooth transitions
  across all available 256 quantization levels (0 to 255).
- Horizontal Gradient: Intensity increases linearly along the x-axis (columns):
    - Column 0: 0 (pure black)
    - Column 128: 128 (mid-gray)
    - Column 255: 255 (pure white)
- NumPy construction: np.tile() replicates a 1D sequence across rows to form a 2D image matrix.
"""

import os
import sys
import cv2
import numpy as np

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q20")
OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q20_intensity_ramp.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q20: Create and display grayscale intensity ramp (0 to 255)")
    print("=" * 60)

    # We create an image of height 256 and width 256
    height = 256
    width = 256

    # Create a 1D row vector containing values from 0 up to 255
    ramp_row = np.linspace(0, 255, width, dtype=np.uint8)

    # Replicate this row vertically for all 'height' rows
    ramp_img = np.tile(ramp_row, (height, 1))

    print(f"Generated ramp image shape: {ramp_img.shape}")
    print(f"Data type: {ramp_img.dtype}")
    print(f"Leftmost column (x=0) intensity:   {ramp_img[0, 0]}")
    print(f"Center column (x=128) intensity:    {ramp_img[0, 128]}")
    print(f"Rightmost column (x=255) intensity: {ramp_img[0, 255]}")

    # Save ramp image
    cv2.imwrite(OUTPUT_IMAGE_PATH, ramp_img)
    print(f"Saved intensity ramp image to: {OUTPUT_IMAGE_PATH}")

    # Display (supports headless mode)
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying intensity ramp window. Press any key to close...")
        cv2.imshow("Q20 - Intensity Ramp (0 to 255)", ramp_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Running in headless mode: Display window skipped.")

if __name__ == "__main__":
    main()
