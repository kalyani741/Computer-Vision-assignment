"""
Question 7: Read an image directly in grayscale mode and display it.

Topic: Basic Image Handling
Key Concepts:
- Passing cv2.IMREAD_GRAYSCALE (or integer 0) to cv2.imread() instructs OpenCV
  to convert the image into a single-channel 8-bit grayscale image during file loading.
- The returned NumPy matrix has only 2 dimensions: (height, width).
- Grayscale intensities range from 0 (black) to 255 (white).
"""

import os
import sys
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q07")
OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q07_grayscale.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q07: Read an image directly in grayscale mode and display it")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    # Read image directly in grayscale mode
    gray_img = cv2.imread(INPUT_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

    if gray_img is None:
        print("Error: Could not decode image.")
        return

    print(f"Loaded image directly in grayscale mode from: {INPUT_IMAGE_PATH}")
    print(f"Grayscale matrix shape: {gray_img.shape} (2D array, channels = 1)")
    print(f"Data type: {gray_img.dtype}")

    # Save the grayscale image
    cv2.imwrite(OUTPUT_IMAGE_PATH, gray_img)
    print(f"Saved grayscale image to: {OUTPUT_IMAGE_PATH}")

    # Display window (supports headless mode)
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying grayscale image window. Press any key to close...")
        cv2.imshow("Q07 - Grayscale (Direct Read)", gray_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Running in headless mode: Display window skipped.")

if __name__ == "__main__":
    main()
