"""
Question 13: Read a color image and print the B, G, and R values of a selected pixel.

Topic: Pixel & Image Representation
Key Concepts:
- OpenCV loads images in Blue, Green, Red (BGR) channel order:
    - Index 0 corresponds to the Blue (B) component.
    - Index 1 corresponds to the Green (G) component.
    - Index 2 corresponds to the Red (R) component.
- Each channel value ranges from 0 (minimum intensity) to 255 (maximum intensity).
"""

import os
import sys
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q13")
OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIR, "Q13_result.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q13: Print B, G, and R values of a selected pixel")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    img = cv2.imread(INPUT_IMAGE_PATH)
    if img is None:
        print("Error: Could not decode image.")
        return

    height, width = img.shape[:2]

    # Select coordinate (from CLI if provided, otherwise default to a vibrant point, e.g. center)
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) >= 2:
        try:
            x, y = int(args[0]), int(args[1])
        except ValueError:
            x, y = width // 2, height // 2
    else:
        x, y = width // 2, height // 2

    # Extract individual channel values at (y, x)
    pixel = img[y, x]
    b = int(pixel[0])
    g = int(pixel[1])
    r = int(pixel[2])

    report = (
        f"Image File: input/sample.jpg\n"
        f"Image Resolution: {width} x {height}\n"
        f"Inspected Pixel Location: (x={x}, y={y})\n"
        f"NumPy Matrix Index: img[{y}, {x}]\n"
        f"Complete BGR Pixel Vector: {pixel.tolist()}\n"
        f"-----------------------------------------\n"
        f"Blue  Channel Intensity (B): {b} / 255\n"
        f"Green Channel Intensity (G): {g} / 255\n"
        f"Red   Channel Intensity (R): {r} / 255\n"
        f"Dominant Channel: {('Blue' if b >= max(g, r) else ('Green' if g >= max(b, r) else 'Red'))}\n"
    )

    print(report)

    with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
        f.write("Q13: BGR Pixel Values Report\n" + "=" * 30 + "\n" + report)

    print(f"Results saved to: {OUTPUT_FILE_PATH}")

if __name__ == "__main__":
    main()
