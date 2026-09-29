"""
Question 5: Print the data type (dtype) of the image matrix.

Topic: Basic Image Handling
Key Concepts:
- `img.dtype` provides the NumPy data type of the underlying pixel matrix.
- Standard 8-bit images use `uint8` (unsigned 8-bit integer, values 0 to 255).
- Each intensity value takes 1 byte (8 bits).
- `img.nbytes` gives total memory allocated in bytes.
"""

import os
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q05")
OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIR, "Q05_result.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q05: Print data type (dtype) of the image matrix")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    img = cv2.imread(INPUT_IMAGE_PATH)
    if img is None:
        print("Error: Could not decode image.")
        return

    dtype = img.dtype
    item_size = img.itemsize  # bytes per element
    total_bytes = img.nbytes  # total memory size

    report = (
        f"Image File: input/sample.jpg\n"
        f"NumPy Data Type (dtype): {dtype}\n"
        f"Bytes per Element: {item_size} byte(s)\n"
        f"Total Memory Consumption: {total_bytes:,} bytes ({total_bytes / (1024 * 1024):.2f} MB)\n"
        f"Interpretation: uint8 represents unsigned 8-bit integers with dynamic range [0, 255].\n"
    )

    print(report)

    with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
        f.write("Q05: Image Data Type Report\n" + "=" * 30 + "\n" + report)

    print(f"Results saved to: {OUTPUT_FILE_PATH}")

if __name__ == "__main__":
    main()
