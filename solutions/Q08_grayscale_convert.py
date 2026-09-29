"""
Question 8: Convert a color image to grayscale using cv2.cvtColor().

Topic: Basic Image Handling
Key Concepts:
- cv2.cvtColor(src, code): Converts an image from one color space to another.
- cv2.COLOR_BGR2GRAY: Transforms a 3-channel BGR image into a 1-channel grayscale image.
- Luminance weighting formula used by OpenCV (ITU-R BT.601 standard):
    Gray = 0.299 * R + 0.587 * G + 0.114 * B
- Human eyes are biologically most sensitive to green light and least sensitive
  to blue light, which is reflected in these perceptual weights.
"""

import os
import sys
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q08")
OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q08_grayscale_converted.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q08: Convert a color image to grayscale using cv2.cvtColor()")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    # Step 1: Read the color image in BGR format
    bgr_img = cv2.imread(INPUT_IMAGE_PATH, cv2.IMREAD_COLOR)
    if bgr_img is None:
        print("Error: Could not decode color image.")
        return

    print(f"Original color image shape: {bgr_img.shape}")

    # Step 2: Convert to grayscale using cv2.cvtColor()
    # Formula: Gray = 0.299 * R + 0.587 * G + 0.114 * B
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

    print(f"Converted grayscale image shape: {gray_img.shape}")
    print(f"Grayscale data type: {gray_img.dtype}")

    # Step 3: Save converted image
    cv2.imwrite(OUTPUT_IMAGE_PATH, gray_img)
    print(f"Saved converted grayscale image to: {OUTPUT_IMAGE_PATH}")

    # Step 4: Display (supports headless mode)
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying converted grayscale window. Press any key to close...")
        cv2.imshow("Q08 - Converted Grayscale (cv2.cvtColor)", gray_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Running in headless mode: Display window skipped.")

if __name__ == "__main__":
    main()
