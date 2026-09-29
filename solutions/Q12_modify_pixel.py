"""
Question 12: Modify the intensity/value of a selected pixel and save the modified image.

Topic: Pixel & Image Representation
Key Concepts:
- Pixel Modification: In NumPy arrays, pixel intensities are mutable.
    - Example: img[y, x] = [0, 255, 0] sets the pixel to pure green.
- Visibility consideration: A single 1x1 pixel on a high-resolution image is
  virtually invisible to the naked eye. In this solution:
    1. We modify the exact selected pixel (x, y).
    2. We also modify a small surrounding patch (e.g. 21x21 box and marker)
       so the change is clearly visible in the saved output image.
"""

import os
import sys
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q12")
OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q12_modified_pixel.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q12: Modify the intensity/value of a selected pixel and save")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    # Load image (make an explicit copy to avoid modifying original array reference)
    img = cv2.imread(INPUT_IMAGE_PATH)
    if img is None:
        print("Error: Could not decode image.")
        return

    modified_img = img.copy()
    height, width = modified_img.shape[:2]

    # Select target coordinate (center of image)
    x, y = width // 2, height // 2
    original_val = modified_img[y, x].copy()

    # Step 1: Modify the single exact pixel at (x, y) to bright yellow: B=0, G=255, R=255
    new_color = [0, 255, 255]  # BGR format: Yellow
    modified_img[y, x] = new_color

    print(f"Target Coordinate: (x={x}, y={y})")
    print(f"Original BGR value: {original_val.tolist()}")
    print(f"Modified BGR value: {modified_img[y, x].tolist()}")

    # Step 2: Modify a visible 21x21 neighborhood patch around (x, y)
    # This makes the modification easily verifiable to human reviewers on GitHub.
    patch_radius = 10
    y1 = max(0, y - patch_radius)
    y2 = min(height, y + patch_radius + 1)
    x1 = max(0, x - patch_radius)
    x2 = min(width, x + patch_radius + 1)
    modified_img[y1:y2, x1:x2] = new_color

    # Add a thin black border around the modified patch for high contrast
    cv2.rectangle(modified_img, (x1, y1), (x2 - 1, y2 - 1), (0, 0, 0), 1)

    # Save modified image
    cv2.imwrite(OUTPUT_IMAGE_PATH, modified_img)
    print(f"Saved modified image to: {OUTPUT_IMAGE_PATH}")

    # Display (supports headless mode)
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying modified image window. Press any key to close...")
        cv2.imshow("Q12 - Modified Pixel (Highlighted Center)", modified_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Running in headless mode: Display window skipped.")

if __name__ == "__main__":
    main()
