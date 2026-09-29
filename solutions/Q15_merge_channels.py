"""
Question 15: Merge three separate image channels into a single color image.

Topic: Pixel & Image Representation
Key Concepts:
- cv2.merge([b, g, r]): Combines several single-channel matrices into one multi-channel image.
- In NumPy, this is equivalent to stacking along the depth axis: np.dstack((b, g, r)).
- Splitting followed by merging is a lossless operation:
    np.array_equal(original, merged) == True.
"""

import os
import sys
import cv2
import numpy as np

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q15")
OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q15_merged.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q15: Merge three separate image channels into a single color image")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    # Read original image
    original_img = cv2.imread(INPUT_IMAGE_PATH)
    if original_img is None:
        print("Error: Could not decode image.")
        return

    # Split into B, G, R
    b, g, r = cv2.split(original_img)

    # Merge channels back into a color image
    merged_img = cv2.merge([b, g, r])

    print(f"Input channel shapes: B={b.shape}, G={g.shape}, R={r.shape}")
    print(f"Merged image shape: {merged_img.shape}")

    # Verify reconstruction accuracy
    is_identical = np.array_equal(original_img, merged_img)
    print(f"Is merged image pixel-for-pixel identical to original? {is_identical}")

    # Save merged image
    cv2.imwrite(OUTPUT_IMAGE_PATH, merged_img)
    print(f"Saved merged color image to: {OUTPUT_IMAGE_PATH}")

    # Display (supports headless mode)
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying merged color image. Press any key to close...")
        cv2.imshow("Q15 - Merged Color Image", merged_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Running in headless mode: Display window skipped.")

if __name__ == "__main__":
    main()
