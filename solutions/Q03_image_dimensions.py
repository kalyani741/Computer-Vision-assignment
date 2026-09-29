"""
Question 3: Print the image height, width, and number of channels.

Topic: Basic Image Handling
Key Concepts:
- In NumPy/OpenCV, an image is represented as a multidimensional array.
- The attribute `img.shape` yields:
    - (height, width, channels) for a color image (3D array).
    - (height, width) for a grayscale image (2D array).
- In image coordinates:
    - height = number of rows (y-axis).
    - width = number of columns (x-axis).
    - channels = color depth (typically 3 for BGR).
"""

import os
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q03")
OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIR, "Q03_result.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q03: Print image height, width, and number of channels")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    img = cv2.imread(INPUT_IMAGE_PATH)
    if img is None:
        print("Error: Could not decode image.")
        return

    # Extract dimensions using img.shape
    shape = img.shape
    height = shape[0]
    width = shape[1]
    channels = shape[2] if len(shape) == 3 else 1

    report = (
        f"Image File: input/sample.jpg\n"
        f"Full Shape: {shape}\n"
        f"Height (Rows): {height} pixels\n"
        f"Width (Columns): {width} pixels\n"
        f"Number of Channels: {channels}\n"
    )

    print(report)

    with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
        f.write("Q03: Image Dimensions Report\n" + "=" * 30 + "\n" + report)

    print(f"Results saved to: {OUTPUT_FILE_PATH}")

if __name__ == "__main__":
    main()
