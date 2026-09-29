"""
Question 11: Access and print the pixel value at a user-provided (x, y) coordinate.

Topic: Pixel & Image Representation
Key Concepts:
- Coordinate indexing convention in NumPy:
    - In geometry/cartesian coordinates: (x, y) represents (horizontal, vertical).
    - In NumPy array slicing: img[y, x] where y = row index and x = column index.
- For a BGR color image, accessing img[y, x] returns an array [Blue, Green, Red].
- Boundary validation is essential to avoid IndexError.
"""

import os
import sys
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q11")
OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIR, "Q11_result.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def parse_coordinates(width: int, height: int) -> tuple[int, int]:
    """
    Retrieves (x, y) from CLI args, user input (if interactive),
    or defaults to the center of the image.
    """
    # Check CLI arguments: python Q11_pixel_access.py <x> <y>
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) >= 2:
        try:
            x, y = int(args[0]), int(args[1])
            return x, y
        except ValueError:
            pass

    # If running interactively with a terminal attached
    if sys.stdin.isatty():
        try:
            user_x = input(f"Enter x-coordinate (0 to {width - 1}) [default {width // 2}]: ").strip()
            user_y = input(f"Enter y-coordinate (0 to {height - 1}) [default {height // 2}]: ").strip()
            x = int(user_x) if user_x else width // 2
            y = int(user_y) if user_y else height // 2
            return x, y
        except (ValueError, EOFError):
            pass

    # Safe default: Center coordinate
    return width // 2, height // 2

def main():
    print("=" * 60)
    print("Q11: Access pixel value at a user-provided (x, y) coordinate")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    img = cv2.imread(INPUT_IMAGE_PATH)
    if img is None:
        print("Error: Could not decode image.")
        return

    height, width = img.shape[:2]
    x, y = parse_coordinates(width, height)

    # Validate coordinate boundaries
    if not (0 <= x < width and 0 <= y < height):
        print(f"Error: Coordinates ({x}, {y}) are out of bounds for image size {width}x{height}!")
        return

    # Access pixel value using row-column indexing: img[y, x]
    pixel_value = img[y, x]
    b, g, r = int(pixel_value[0]), int(pixel_value[1]), int(pixel_value[2])

    report = (
        f"Image File: input/sample.jpg\n"
        f"Image Dimensions: Width={width}, Height={height}\n"
        f"Selected Coordinate: (x={x}, y={y})\n"
        f"Array Index Used: img[y={y}, x={x}]\n"
        f"Raw Pixel Vector (BGR): {pixel_value.tolist()}\n"
        f"Blue  (B) Channel Intensity: {b}\n"
        f"Green (G) Channel Intensity: {g}\n"
        f"Red   (R) Channel Intensity: {r}\n"
    )

    print(report)

    with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
        f.write("Q11: Pixel Access Report\n" + "=" * 30 + "\n" + report)

    print(f"Results saved to: {OUTPUT_FILE_PATH}")

if __name__ == "__main__":
    main()
