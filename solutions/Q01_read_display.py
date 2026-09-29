"""
Question 1: Read an image using OpenCV and display it.

Topic: Basic Image Handling
Key Concepts:
- cv2.imread(): Loads an image from a specified file.
- BGR color order: By default, OpenCV reads color images in BGR format rather than RGB.
- cv2.imshow(): Displays an image in a GUI window.
- cv2.imwrite(): Saves the image to disk.
"""

import os
import sys
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q01")
OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q01_original_image.png")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q01: Read an image using OpenCV and display it")
    print("=" * 60)

    # Check if the input file exists
    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    # Step 1: Read the image
    # cv2.IMREAD_COLOR (or 1) loads a color image in BGR format
    img = cv2.imread(INPUT_IMAGE_PATH, cv2.IMREAD_COLOR)

    # Step 2: Verify that image loaded correctly
    if img is None:
        print("Error: Failed to decode the image.")
        return

    print(f"Successfully loaded image from: {INPUT_IMAGE_PATH}")
    print(f"Image matrix shape: {img.shape} (Height: {img.shape[0]}, Width: {img.shape[1]}, Channels: {img.shape[2]})")

    # Step 3: Save the image to the output folder
    success = cv2.imwrite(OUTPUT_IMAGE_PATH, img)
    if success:
        print(f"Saved output image to: {OUTPUT_IMAGE_PATH}")
    else:
        print(f"Warning: Failed to save image to: {OUTPUT_IMAGE_PATH}")

    # Step 4: Display the image in a window (supports headless mode for automated runs)
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying image window. Press any key in the window to close...")
        cv2.imshow("Q01 - Original Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Running in headless mode: Display window skipped.")

if __name__ == "__main__":
    main()
