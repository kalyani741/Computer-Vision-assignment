"""
Question 14: Split a color image into its B, G, and R channels and display each channel.

Topic: Pixel & Image Representation
Key Concepts:
- cv2.split(img): Splits a multi-channel array into separate single-channel arrays.
- Alternatively, NumPy array indexing:
    - b = img[:, :, 0]
    - g = img[:, :, 1]
    - r = img[:, :, 2]
- Each individual channel is a 2D matrix of intensity values from 0 to 255.
  A brighter area in the blue channel indicates high concentration of blue light.
"""

import os
import sys
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q14")

BLUE_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Q14_blue_channel.png")
GREEN_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Q14_green_channel.png")
RED_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Q14_red_channel.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q14: Split color image into B, G, and R channels")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    img = cv2.imread(INPUT_IMAGE_PATH)
    if img is None:
        print("Error: Could not decode image.")
        return

    # Split channels using cv2.split
    b_channel, g_channel, r_channel = cv2.split(img)

    print(f"Original image shape: {img.shape}")
    print(f"Blue channel shape:  {b_channel.shape}, dtype: {b_channel.dtype}")
    print(f"Green channel shape: {g_channel.shape}, dtype: {g_channel.dtype}")
    print(f"Red channel shape:   {r_channel.shape}, dtype: {r_channel.dtype}")

    # Save each channel as an individual 8-bit image
    cv2.imwrite(BLUE_OUTPUT_PATH, b_channel)
    cv2.imwrite(GREEN_OUTPUT_PATH, g_channel)
    cv2.imwrite(RED_OUTPUT_PATH, r_channel)

    print(f"Saved Blue Channel to:  {BLUE_OUTPUT_PATH}")
    print(f"Saved Green Channel to: {GREEN_OUTPUT_PATH}")
    print(f"Saved Red Channel to:   {RED_OUTPUT_PATH}")

    # Display (supports headless mode)
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying channel windows. Press any key to close...")
        cv2.imshow("Q14 - Blue Channel", b_channel)
        cv2.imshow("Q14 - Green Channel", g_channel)
        cv2.imshow("Q14 - Red Channel", r_channel)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Running in headless mode: Display window skipped.")

if __name__ == "__main__":
    main()
