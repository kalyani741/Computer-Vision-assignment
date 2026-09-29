"""
Question 25: Rotate an image by 90 degrees, display it, and save the rotated image.

Topic: Sampling, Quantization & Geometric Operations
Key Concepts:
- Orthogonal Rotation in OpenCV:
    - cv2.rotate(src, rotateCode): Performs 90-degree rotations without interpolation artifacts.
    - Supported flags:
        * cv2.ROTATE_90_CLOCKWISE (rotate 90 degrees clockwise)
        * cv2.ROTATE_180 (rotate 180 degrees)
        * cv2.ROTATE_90_COUNTERCLOCKWISE (rotate 270 degrees clockwise / 90 counter-clockwise)
- Mathematical Mechanism:
    - A 90-degree clockwise rotation is equivalent to Matrix Transpose followed by
      Horizontal Flip (mirroring across the vertical axis):
        rotated = cv2.flip(cv2.transpose(img), 1)
- Dimension Inversion:
    - An image of shape (Height, Width) becomes (Width, Height) after a 90-degree rotation.
"""

import os
import sys
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q25")
OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q25_rotated_90.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q25: Rotate an image by 90 degrees")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    img = cv2.imread(INPUT_IMAGE_PATH)
    if img is None:
        print("Error: Could not decode image.")
        return

    orig_h, orig_w = img.shape[:2]
    print(f"Original Image Dimensions: {orig_w} x {orig_h} (Width x Height)")

    # Rotate 90 degrees clockwise using OpenCV cv2.rotate
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    new_h, new_w = rotated_img.shape[:2]
    print(f"Rotated Image Dimensions:  {new_w} x {new_h} (Width x Height)")
    print(f"Dimension swap verified: ({orig_h} -> {new_w}, {orig_w} -> {new_h})")

    # Save rotated image
    cv2.imwrite(OUTPUT_IMAGE_PATH, rotated_img)
    print(f"Saved 90-degree rotated image to: {OUTPUT_IMAGE_PATH}")

    # Display (supports headless mode)
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying rotated image window. Press any key to close...")
        cv2.imshow("Q25 - Original Image", img)
        cv2.imshow("Q25 - Rotated 90 Degrees Clockwise", rotated_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Running in headless mode: Display window skipped.")

if __name__ == "__main__":
    main()
