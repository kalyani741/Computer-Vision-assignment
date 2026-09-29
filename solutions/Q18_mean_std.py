"""
Question 18: Calculate and print the mean and standard deviation of a
             grayscale image using NumPy/OpenCV.

Topic: Pixel & Image Representation
Key Concepts:
- Mean (mu): Represents the average brightness level of the image.
- Standard Deviation (sigma): Measures the spread/dispersion of pixel intensities
  around the mean. In computer vision, standard deviation is directly related to image contrast:
    - High sigma: High contrast (wide range of dark and light tones).
    - Low sigma: Low contrast (flat, gray, or washed out appearance).
- OpenCV: cv2.meanStdDev(src) returns (mean, stddev).
- NumPy: np.mean(src) and np.std(src).
"""

import os
import cv2
import numpy as np

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q18")
OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIR, "Q18_result.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q18: Calculate and print mean and standard deviation")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    gray_img = cv2.imread(INPUT_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    if gray_img is None:
        print("Error: Could not decode image.")
        return

    # Method 1: Using OpenCV cv2.meanStdDev()
    mean_cv, std_cv = cv2.meanStdDev(gray_img)
    cv_mean_val = float(mean_cv[0][0])
    cv_std_val = float(std_cv[0][0])

    # Method 2: Using NumPy
    np_mean_val = float(np.mean(gray_img))
    np_std_val = float(np.std(gray_img))

    # Variance is standard deviation squared
    variance_val = np_std_val ** 2

    report = (
        f"Image File: input/sample.jpg\n"
        f"Grayscale Resolution: {gray_img.shape[1]} x {gray_img.shape[0]}\n"
        f"-----------------------------------------\n"
        f"OpenCV cv2.meanStdDev():\n"
        f"  Mean (Average Brightness):        {cv_mean_val:.4f}\n"
        f"  Standard Deviation (Contrast):     {cv_std_val:.4f}\n"
        f"-----------------------------------------\n"
        f"NumPy np.mean() / np.std():\n"
        f"  Mean:                              {np_mean_val:.4f}\n"
        f"  Standard Deviation:                {np_std_val:.4f}\n"
        f"  Variance (sigma^2):                {variance_val:.4f}\n"
        f"-----------------------------------------\n"
        f"Statistical Analysis:\n"
        f"  The mean of {np_mean_val:.2f} confirms the general illumination level,\n"
        f"  while the standard deviation of {np_std_val:.2f} indicates the tonal contrast.\n"
    )

    print(report)

    with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
        f.write("Q18: Mean and Standard Deviation Report\n" + "=" * 40 + "\n" + report)

    print(f"Results saved to: {OUTPUT_FILE_PATH}")

if __name__ == "__main__":
    main()
