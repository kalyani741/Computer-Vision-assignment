"""
Question 24: Crop a rectangular Region of Interest (ROI) from an image
             using user-provided coordinates.

Topic: Sampling, Quantization & Geometric Operations
Key Concepts:
- Region of Interest (ROI): A specific sub-area of an image isolated for analysis
  (e.g., face detection, license plate recognition).
- NumPy Array Slicing Syntax:
    roi = img[y1:y2, x1:x2]
    - Note that y indices (rows) come first, followed by x indices (columns).
- Coordinate Definitions:
    - (x1, y1): Top-left corner of the bounding rectangle.
    - (x2, y2): Bottom-right corner of the bounding rectangle.
- Coordinate Validation:
    - 0 <= x1 < x2 <= width
    - 0 <= y1 < y2 <= height
"""

import os
import sys
import cv2

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q24")
OUTPUT_ROI_PATH = os.path.join(OUTPUT_DIR, "Q24_roi.png")
OUTPUT_BOX_PATH = os.path.join(OUTPUT_DIR, "Q24_roi_with_bounding_box.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_roi_coordinates(width: int, height: int) -> tuple[int, int, int, int]:
    """
    Retrieves x1, y1, x2, y2 from CLI arguments, interactive input, or default coordinates.
    Default extracts Grace Hopper's face region on sample.jpg.
    """
    # Check CLI arguments: python Q24_roi_crop.py <x1> <y1> <x2> <y2>
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) >= 4:
        try:
            return int(args[0]), int(args[1]), int(args[2]), int(args[3])
        except ValueError:
            pass

    # Interactive input if run in an interactive terminal
    if sys.stdin.isatty():
        try:
            print("Provide ROI coordinates (Press Enter to use defaults):")
            u_x1 = input(f"Enter x1 (top-left x) [default 150]: ").strip()
            u_y1 = input(f"Enter y1 (top-left y) [default 80]: ").strip()
            u_x2 = input(f"Enter x2 (bottom-right x) [default 360]: ").strip()
            u_y2 = input(f"Enter y2 (bottom-right y) [default 340]: ").strip()
            x1 = int(u_x1) if u_x1 else 150
            y1 = int(u_y1) if u_y1 else 80
            x2 = int(u_x2) if u_x2 else 360
            y2 = int(u_y2) if u_y2 else 340
            return x1, y1, x2, y2
        except (ValueError, EOFError):
            pass

    # Default coordinates (Face / central feature region)
    default_x1 = max(0, int(width * 0.25))
    default_y1 = max(0, int(height * 0.12))
    default_x2 = min(width, int(width * 0.72))
    default_y2 = min(height, int(height * 0.58))
    return default_x1, default_y1, default_x2, default_y2

def main():
    print("=" * 60)
    print("Q24: Crop a rectangular Region of Interest (ROI)")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    img = cv2.imread(INPUT_IMAGE_PATH)
    if img is None:
        print("Error: Could not decode image.")
        return

    height, width = img.shape[:2]
    print(f"Loaded image resolution: {width} x {height} (Width x Height)")

    # Get ROI coordinates
    x1, y1, x2, y2 = get_roi_coordinates(width, height)

    # Validate coordinate boundaries
    if not (0 <= x1 < x2 <= width and 0 <= y1 < y2 <= height):
        print(f"Error: Invalid ROI coordinates: ({x1}, {y1}) to ({x2}, {y2}) for image of size {width}x{height}")
        return

    print(f"Using ROI Coordinates: x1={x1}, y1={y1}, x2={x2}, y2={y2}")
    print(f"ROI Size: {x2 - x1} x {y2 - y1} (Width x Height)")

    # Perform ROI cropping via NumPy slicing
    # Notice: rows (y) are sliced first, columns (x) second
    cropped_roi = img[y1:y2, x1:x2]

    # Save cropped ROI
    cv2.imwrite(OUTPUT_ROI_PATH, cropped_roi)
    print(f"Saved cropped ROI to: {OUTPUT_ROI_PATH}")

    # Draw bounding box on original image copy to visualize where ROI came from
    annotated = img.copy()
    cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(annotated, f"ROI ({x2 - x1}x{y2 - y1})", (x1, max(20, y1 - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imwrite(OUTPUT_BOX_PATH, annotated)
    print(f"Saved ROI context visualization to: {OUTPUT_BOX_PATH}")

    # Display (supports headless mode)
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying cropped ROI window. Press any key to close...")
        cv2.imshow("Q24 - Cropped ROI", cropped_roi)
        cv2.imshow("Q24 - Bounding Box on Original", annotated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Running in headless mode: Display window skipped.")

if __name__ == "__main__":
    main()
