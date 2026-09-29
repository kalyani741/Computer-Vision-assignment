"""
Question 16: Calculate and print the minimum and maximum intensity values of a grayscale image.

Topic: Pixel & Image Representation
Key Concepts:
- cv2.minMaxLoc(src): Finds global minimum and maximum intensity values and their (x, y) coordinates.
- NumPy alternatives: np.min(src) and np.max(src).
- Dynamic range in 8-bit grayscale is nominally [0, 255].
- The difference (max_val - min_val) indicates the image's dynamic contrast spread.
"""

import os
import cv2
import numpy as np

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q16")
OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIR, "Q16_result.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q16: Calculate and print min and max intensity of grayscale image")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    # Load image directly as grayscale
    gray_img = cv2.imread(INPUT_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    if gray_img is None:
        print("Error: Could not decode image.")
        return

    # Method 1: Using OpenCV cv2.minMaxLoc
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray_img)

    # Method 2: Using NumPy functions
    np_min = np.min(gray_img)
    np_max = np.max(gray_img)

    report = (
        f"Image File: input/sample.jpg\n"
        f"Grayscale Resolution: {gray_img.shape[1]} x {gray_img.shape[0]} (Width x Height)\n"
        f"-----------------------------------------\n"
        f"OpenCV Calculation:\n"
        f"  Minimum Intensity Value: {min_val:.0f} at coordinate (x={min_loc[0]}, y={min_loc[1]})\n"
        f"  Maximum Intensity Value: {max_val:.0f} at coordinate (x={max_loc[0]}, y={max_loc[1]})\n"
        f"-----------------------------------------\n"
        f"NumPy Calculation:\n"
        f"  np.min: {np_min}\n"
        f"  np.max: {np_max}\n"
        f"-----------------------------------------\n"
        f"Dynamic Range Spread (Max - Min): {max_val - min_val:.0f}\n"
        f"Theoretical Dynamic Range: 0 to 255\n"
    )

    print(report)

    with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
        f.write("Q16: Min and Max Intensity Report\n" + "=" * 35 + "\n" + report)

    print(f"Results saved to: {OUTPUT_FILE_PATH}")

if __name__ == "__main__":
    main()
