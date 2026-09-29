"""
Question 23: Downsample an image by a factor of 2 in both width and height
             and print the original and new resolutions.

Topic: Sampling, Quantization & Geometric Operations
Key Concepts:
- Spatial Sampling: Reducing the spatial resolution of an image grid.
- Downsampling by Factor of 2:
    - Retaining every 2nd pixel horizontally and vertically: img[::2, ::2].
    - New width = Original width / 2.
    - New height = Original height / 2.
    - Total pixel count is reduced by a factor of 4 (2 * 2).
- Aliasing: Without pre-filtering (anti-aliasing low-pass filter), direct decimation
  can cause high-frequency textures to appear jagged. Area averaging (cv2.INTER_AREA)
  helps mitigate this.
"""

import os
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q23")

ORIGINAL_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q23_original.png")
DOWNSAMPLED_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q23_downsampled.png")
RESOLUTION_FILE_PATH = os.path.join(OUTPUT_DIR, "Q23_resolution.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q23: Downsample image by factor of 2 in width and height")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    img = cv2.imread(INPUT_IMAGE_PATH)
    if img is None:
        print("Error: Could not decode image.")
        return

    orig_h, orig_w = img.shape[:2]

    # Method: Direct spatial decimation (sub-sampling every 2nd row and 2nd column)
    downsampled_img = img[::2, ::2]
    new_h, new_w = downsampled_img.shape[:2]

    orig_pixels = orig_w * orig_h
    new_pixels = new_w * new_h
    reduction_ratio = orig_pixels / new_pixels

    report = (
        f"Image File: input/sample.jpg\n"
        f"-----------------------------------------\n"
        f"Original Resolution:    {orig_w} x {orig_h} (Width x Height)\n"
        f"Original Pixel Count:   {orig_pixels:,} pixels\n"
        f"-----------------------------------------\n"
        f"Downsampling Factor:    2 (Horizontal & Vertical)\n"
        f"New Resolution:         {new_w} x {new_h} (Width x Height)\n"
        f"New Pixel Count:        {new_pixels:,} pixels\n"
        f"Pixel Reduction Factor: {reduction_ratio:.2f}x (Nominally 4x reduction)\n"
        f"-----------------------------------------\n"
        f"Sampling Technique:     Spatial Subsampling (Decimation via img[::2, ::2])\n"
    )

    print(report)

    # Save original image
    cv2.imwrite(ORIGINAL_IMAGE_PATH, img)
    print(f"Saved original image to:    {ORIGINAL_IMAGE_PATH}")

    # Save downsampled image
    cv2.imwrite(DOWNSAMPLED_IMAGE_PATH, downsampled_img)
    print(f"Saved downsampled image to: {DOWNSAMPLED_IMAGE_PATH}")

    # Save resolution report
    with open(RESOLUTION_FILE_PATH, "w", encoding="utf-8") as f:
        f.write("Q23: Downsampling Resolution Report\n" + "=" * 40 + "\n" + report)

    print(f"Saved resolution report to: {RESOLUTION_FILE_PATH}")

if __name__ == "__main__":
    main()
