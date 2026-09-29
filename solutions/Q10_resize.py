"""
Question 10: Resize an image to 50% of its original width and height.

Topic: Basic Image Handling
Key Concepts:
- cv2.resize(src, dsize, fx, fy, interpolation):
    - Note critical OpenCV convention: dsize is (width, height), whereas
      matrix shape is (height, width).
    - Can specify explicit dimensions (width, height) OR scale factors (fx=0.5, fy=0.5).
- Interpolation Algorithms:
    - cv2.INTER_AREA: Recommended for downsampling (shrinking) because it uses
      pixel area relation to avoid Moiré patterns and aliasing.
    - cv2.INTER_LINEAR: Good default for magnification / upsampling.
    - cv2.INTER_CUBIC: Slower, higher quality upsampling.
"""

import os
import sys
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q10")
OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q10_resized.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q10: Resize an image to 50% of its original width and height")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    img = cv2.imread(INPUT_IMAGE_PATH)
    if img is None:
        print("Error: Could not decode image.")
        return

    orig_h, orig_w = img.shape[:2]
    new_w = int(orig_w * 0.5)
    new_h = int(orig_h * 0.5)

    print(f"Original Resolution: {orig_w} x {orig_h} (Width x Height)")
    print(f"Target 50% Resolution: {new_w} x {new_h} (Width x Height)")

    # Resize using cv2.INTER_AREA for clean downsampling
    resized_img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

    print(f"Resized image matrix shape: {resized_img.shape}")

    # Save resized image
    cv2.imwrite(OUTPUT_IMAGE_PATH, resized_img)
    print(f"Saved resized image to: {OUTPUT_IMAGE_PATH}")

    # Display (supports headless mode)
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying resized image window. Press any key to close...")
        cv2.imshow("Q10 - Resized 50%", resized_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Running in headless mode: Display window skipped.")

if __name__ == "__main__":
    main()
