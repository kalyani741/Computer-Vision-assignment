"""
Question 9: Display an image using Matplotlib and hide the axis.

Topic: Basic Image Handling
Key Concepts:
- Color Order Difference: OpenCV uses BGR channel order, whereas Matplotlib uses RGB.
  To display the true colors in Matplotlib, we must convert using cv2.COLOR_BGR2RGB.
- plt.axis('off'): Hides the x and y coordinate ticks and bounding frame.
- plt.savefig(): Saves the Matplotlib rendered plot directly to an image file.
"""

import os
import sys
import cv2
import matplotlib.pyplot as plt

# Resolve paths relative to project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INPUT_IMAGE_PATH = os.path.join(PROJECT_ROOT, "input", "sample.jpg")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs", "Q09")
OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_DIR, "Q09_matplotlib_output.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Q09: Display an image using Matplotlib and hide the axis")
    print("=" * 60)

    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image file not found at: {INPUT_IMAGE_PATH}")
        return

    # Read image using OpenCV (BGR order)
    img_bgr = cv2.imread(INPUT_IMAGE_PATH)
    if img_bgr is None:
        print("Error: Could not decode image.")
        return

    # Convert BGR to RGB so colors are rendered correctly by Matplotlib
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # Create Matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(img_rgb)

    # Hide the coordinate axis ticks and borders
    ax.axis("off")
    ax.set_title("Q09: Matplotlib Display (Axis Hidden)", fontsize=14, pad=10)

    # Save output plot
    plt.tight_layout()
    plt.savefig(OUTPUT_IMAGE_PATH, bbox_inches="tight", dpi=150)
    print(f"Saved Matplotlib output figure to: {OUTPUT_IMAGE_PATH}")

    # Display figure interactively unless running in headless mode
    headless = os.environ.get("HEADLESS", "0") == "1" or "--headless" in sys.argv
    if not headless:
        print("Displaying Matplotlib figure. Close the window to continue...")
        plt.show()
    else:
        print("Running in headless mode: Display window skipped.")

    plt.close(fig)

if __name__ == "__main__":
    main()
