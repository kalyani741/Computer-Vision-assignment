"""
Question 17: Calculate and print the mean intensity of a grayscale image.

Topic: Pixel & Image Representation
Key Concepts:
- Mean Intensity: Measures the overall brightness level of an image.
- Mathematical Formula:
    mean (mu) = (1 / N) * sum(I_i)
    where N is the total number of pixels, and I_i is the intensity of pixel i.
- OpenCV: cv2.mean(src) returns a 4-element tuple (mean per channel).
- NumPy: np.mean(src) computes the arithmetic average across the array.
"""

import os
import cv2
import numpy as np

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q17")
OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIR, "Q17_result.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q17: Calculate and print mean intensity of a grayscale image")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    gray_img = cv2.imread(INPUT_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    if gray_img is None:
        print("Error: Could not decode image.")
        return

    # Method 1: Using OpenCV cv2.mean()
    cv_mean = cv2.mean(gray_img)[0]

    # Method 2: Using NumPy np.mean()
    np_mean = float(np.mean(gray_img))

    # Manual verification using sum / count
    total_sum = int(np.sum(gray_img))
    total_pixels = gray_img.size
    manual_mean = total_sum / total_pixels

    report = (
        f"Image File: input/sample.jpg\n"
        f"Total Pixels (N): {total_pixels:,}\n"
        f"Sum of Pixel Intensities: {total_sum:,}\n"
        f"-----------------------------------------\n"
        f"OpenCV cv2.mean():  {cv_mean:.4f}\n"
        f"NumPy np.mean():    {np_mean:.4f}\n"
        f"Manual (Sum / N):   {manual_mean:.4f}\n"
        f"-----------------------------------------\n"
        f"Interpretation: On a 0-255 scale, an average intensity of {np_mean:.2f}\n"
        f"indicates an overall {'bright' if np_mean > 150 else ('medium' if np_mean >= 100 else 'dark')} exposure.\n"
    )

    print(report)

    with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
        f.write("Q17: Mean Intensity Report\n" + "=" * 30 + "\n" + report)

    print(f"Results saved to: {OUTPUT_FILE_PATH}")

if __name__ == "__main__":
    main()
