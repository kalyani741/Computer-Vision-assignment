"""
Question 19: Create a 256 x 256 grayscale image in which every pixel has intensity value 128.

Topic: Pixel & Image Representation
Key Concepts:
- Synthetic Image Generation: Images can be created programmatically from scratch using NumPy.
- np.full(shape, fill_value, dtype): Allocates a matrix filled uniformly with a specific scalar.
- An intensity value of 128 corresponds to "mid-gray" (approximately 50% brightness on the 0-255 scale).
- Data type must be np.uint8 for standard 8-bit image display and storage.
"""

import os
import sys
import cv2
import numpy as np

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q19")
OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q19_constant_128.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q19: Create a 256 x 256 grayscale image with constant intensity 128")
    print("=" * 60)

    # Image specifications
    width, height = 256, 256
    intensity_value = 128

    # Create the 256x256 image with all pixels initialized to 128
    constant_img = np.full((height, width), intensity_value, dtype=np.uint8)

    # Verification checks
    print(f"Created synthetic image with shape: {constant_img.shape}")
    print(f"Data type: {constant_img.dtype}")
    print(f"Minimum pixel value: {np.min(constant_img)}")
    print(f"Maximum pixel value: {np.max(constant_img)}")
    print(f"Mean pixel value:    {np.mean(constant_img):.2f}")
    print(f"Are all pixels strictly equal to 128? {np.all(constant_img == 128)}")

    # Save generated image
    success = cv2.imwrite(OUTPUT_IMAGE_PATH, constant_img)
    if success:
        print(f"Successfully saved image to: {OUTPUT_IMAGE_PATH}")
    else:
        print(f"Error: Failed to save image to {OUTPUT_IMAGE_PATH}")

    # Display (supports headless mode)
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying constant gray image window. Press any key to close...")
        cv2.imshow("Q19 - Constant Intensity 128 (256x256)", constant_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Running in headless mode: Display window skipped.")

if __name__ == "__main__":
    main()
