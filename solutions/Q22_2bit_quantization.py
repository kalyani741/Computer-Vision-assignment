"""
Question 22: Convert an 8-bit grayscale image into a 2-bit quantized image
             and display/save the result.

Topic: Sampling, Quantization & Geometric Operations
Key Concepts:
- Quantization Theory:
    - 8-bit grayscale contains 2^8 = 256 discrete intensity levels (0 to 255).
    - 2-bit quantization reduces this to only 2^2 = 4 discrete intensity levels (0, 1, 2, 3).
- Step-by-Step Logic:
    1. Interval / Step Size: Delta = 256 / 4 = 64.
       Intensity ranges are partitioned into 4 distinct bins:
         - Bin 0: [0, 63]   -> Level 0
         - Bin 1: [64, 127] -> Level 1
         - Bin 2: [128, 191]-> Level 2
         - Bin 3: [192, 255]-> Level 3
    2. Quantization Level (q):
       q = intensity // 64  (values in {0, 1, 2, 3}, or bit-shift: intensity >> 6).
    3. Rescaling to 8-bit Display Dynamic Range:
       To display properly on an 8-bit monitor, scale each discrete level q by
       (255 / (4 - 1)) = (255 / 3) = 85:
       I_quantized = q * 85
       Values produced:
         q=0 -> 0   (Pure Black)
         q=1 -> 85  (Dark Gray)
         q=2 -> 170 (Light Gray)
         q=3 -> 255 (Pure White)
    4. Visual Effect (Posterization & False Contouring):
       - With only 4 tones available, the image exhibits severe posterization
         and extreme false contouring, converting continuous gradients into discrete steps.
"""

import os
import sys
import cv2
import numpy as np

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q22")
OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q22_2bit_quantized.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def quantize_2bit(gray_img: np.ndarray) -> np.ndarray:
    """
    Quantizes an 8-bit grayscale image (256 levels) to 2-bit (4 levels)
    and rescales to 0-255 for proper visual presentation.
    """
    # Step 1: Compute 2-bit discrete bins (values in range 0..3)
    # Integer division by 64 groups each block of 64 gray levels into one discrete bin
    levels_2bit = gray_img // 64  # equivalent to: np.right_shift(gray_img, 6)

    # Step 2: Scale 0..3 levels back to the full 0..255 dynamic range
    # 255 / (4 - 1) = 255 / 3 = 85
    scaled_2bit = (levels_2bit * 85).astype(np.uint8)

    return scaled_2bit

def main():
    print("=" * 60)
    print("Q22: 8-bit to 2-bit Grayscale Quantization")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    # Load image in grayscale mode
    gray_img = cv2.imread(INPUT_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    if gray_img is None:
        print("Error: Could not decode image.")
        return

    # Perform 2-bit quantization
    quantized_img = quantize_2bit(gray_img)

    # Inspect unique intensity levels
    unique_orig = len(np.unique(gray_img))
    unique_quant = len(np.unique(quantized_img))

    print(f"Original image shape: {gray_img.shape}")
    print(f"Original unique gray levels: {unique_orig} (out of 256 max)")
    print(f"2-bit quantized unique levels: {unique_quant} (out of 4 max)")
    print(f"Exact 4 intensity values: {np.unique(quantized_img).tolist()}")

    # Save output image
    cv2.imwrite(OUTPUT_IMAGE_PATH, quantized_img)
    print(f"Saved 2-bit quantized image to: {OUTPUT_IMAGE_PATH}")

    # Display (supports headless mode)
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying 2-bit quantized image window. Press any key to close...")
        cv2.imshow("Q22 - 2-bit Quantized Image (4 levels)", quantized_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Running in headless mode: Display window skipped.")

if __name__ == "__main__":
    main()
