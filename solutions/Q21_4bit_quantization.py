"""
Question 21: Convert an 8-bit grayscale image into a 4-bit quantized image
             and display/save the result.

Topic: Sampling, Quantization & Geometric Operations
Key Concepts:
- Quantization Theory:
    - Quantization is the process of mapping a large (or continuous) set of values
      to a smaller discrete set of values.
    - 8-bit grayscale: 2^8 = 256 discrete levels (0, 1, 2, ..., 255).
    - 4-bit grayscale: 2^4 = 16 discrete levels (0, 1, 2, ..., 15).
- Step-by-Step Logic:
    1. Interval / Step Size: Delta = 256 / 16 = 16.
    2. Quantization Level (q): Divide 8-bit intensity by 16 using integer division:
       q = intensity // 16  (values from 0 to 15, or bit-shift: intensity >> 4).
    3. Rescaling to 8-bit Display Dynamic Range:
       Since image files and monitors display in 8-bit [0, 255], we scale level q
       by (255 / 15) = 17:
       I_quantized = q * 17
       This maps:
         q=0  -> 0
         q=1  -> 17
         ...
         q=15 -> 255
    4. Visual Effect:
       - Reduction from 256 to 16 levels introduces slight "false contouring"
         (color banding in smooth gradients), which is the hallmark of coarse quantization.
"""

import os
import sys
import cv2
import numpy as np

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q21")
OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q21_4bit_quantized.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def quantize_4bit(gray_img: np.ndarray) -> np.ndarray:
    """
    Quantizes an 8-bit grayscale image (256 levels) to 4-bit (16 levels)
    and rescales to 0-255 for proper visual presentation.
    """
    # Step 1: Compute 4-bit discrete bins (values in range 0..15)
    # Integer division by 16 groups each range of 16 pixel values into one bin
    levels_4bit = gray_img // 16  # equivalent to: np.right_shift(gray_img, 4)

    # Step 2: Scale 0..15 levels back to the full 0..255 dynamic range
    # 255 / (16 - 1) = 255 / 15 = 17
    scaled_4bit = (levels_4bit * 17).astype(np.uint8)

    return scaled_4bit

def main():
    print("=" * 60)
    print("Q21: 8-bit to 4-bit Grayscale Quantization")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    # Load image in grayscale mode
    gray_img = cv2.imread(INPUT_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    if gray_img is None:
        print("Error: Could not decode image.")
        return

    # Perform 4-bit quantization
    quantized_img = quantize_4bit(gray_img)

    # Inspect unique intensity levels
    unique_orig = len(np.unique(gray_img))
    unique_quant = len(np.unique(quantized_img))

    print(f"Original image shape: {gray_img.shape}")
    print(f"Original unique gray levels: {unique_orig} (out of 256 max)")
    print(f"4-bit quantized unique levels: {unique_quant} (out of 16 max)")
    print(f"4-bit distinct values present: {np.unique(quantized_img).tolist()}")

    # Save output image
    cv2.imwrite(OUTPUT_IMAGE_PATH, quantized_img)
    print(f"Saved 4-bit quantized image to: {OUTPUT_IMAGE_PATH}")

    # Display (supports headless mode)
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying 4-bit quantized image window. Press any key to close...")
        cv2.imshow("Q21 - 4-bit Quantized Image (16 levels)", quantized_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Running in headless mode: Display window skipped.")

if __name__ == "__main__":
    main()
