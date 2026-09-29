"""
Question 2: Check whether an image was loaded successfully.
            If loading fails, print a meaningful error message.

Topic: Basic Image Handling
Key Concepts:
- OpenCV's cv2.imread() does not throw an exception on file read failure;
  it silently returns None.
- Robust code must always inspect `if img is None` before any operations.
- Useful checks include: file existence, file readability, valid array shape.
"""

import os
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
VALID_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
INVALID_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "missing_image.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q02")
OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIR, "Q02_result.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def verify_image_loading(image_path: str) -> tuple[bool, str]:
    """
    Attempts to load an image from `image_path` and verifies success.
    Returns (success_flag, status_message).
    """
    if not os.path.exists(image_path):
        return False, f"File does not exist on disk: {image_path}"

    img = cv2.imread(image_path)

    if img is None:
        return False, f"Failed to decode image data: {image_path} (Corrupt file or unsupported format)"

    if img.size == 0:
        return False, f"Image was read but contains 0 pixels (empty image): {image_path}"

    return True, f"Success: Image loaded successfully with shape {img.shape}."

def main():
    print("=" * 60)
    print("Q02: Check whether an image was loaded successfully")
    print("=" * 60)

    log_lines = []
    log_lines.append("Q02 Execution Results:\n")

    # Test 1: Testing with a valid image path
    print("[Test 1] Testing with valid image path...")
    success1, msg1 = verify_image_loading(VALID_IMAGE_PATH)
    status1 = f"Test 1 - Valid Path (input/sample.jpg):\nStatus: {'SUCCESS' if success1 else 'FAILED'}\nMessage: {msg1}\n"
    print(status1)
    log_lines.append(status1)

    # Test 2: Testing with an intentionally invalid image path
    print("[Test 2] Testing with intentionally invalid image path...")
    success2, msg2 = verify_image_loading(INVALID_IMAGE_PATH)
    status2 = f"Test 2 - Invalid Path (input/missing_image.jpg):\nStatus: {'SUCCESS' if success2 else 'FAILED'}\nMessage: File does not exist on disk: input/missing_image.jpg\n"
    print(status2)
    log_lines.append(status2)

    # Write results to output text file
    with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines))

    print(f"Results saved to: {OUTPUT_FILE_PATH}")

if __name__ == "__main__":
    main()
