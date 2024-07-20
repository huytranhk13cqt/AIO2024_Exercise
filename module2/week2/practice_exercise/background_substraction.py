import os

import cv2
import numpy as np

# Define image paths and target size
green_bg_path = "../data/GreenBackground.png"
object_image_path = "../data/Object.png"
new_bg_path = "../data/NewBackground.jpg"
target_size = (678, 381)


def load_and_resize_image(image_path, size):
    """Check if the file exists, read, and resize the image."""
    if not os.path.exists(image_path):
        print(f"File doesn't exist: {image_path}")
        return None

    image = cv2.imread(image_path, 1)
    if image is None:
        print(f"Cannot access file: {image_path}")
        return None

    return cv2.resize(image, size)


# Load and resize images
bg1_image = load_and_resize_image(green_bg_path, target_size)
ob_image = load_and_resize_image(object_image_path, target_size)
bg2_image = load_and_resize_image(new_bg_path, target_size)


def compute_difference(bg_img, input_img, threshold=50):
    # Convert the images to grayscale
    gray_bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    gray_input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference between the images
    difference_img = cv2.absdiff(gray_bg_img, gray_input_img)

    # Apply Gaussian blur to reduce noise
    blurred_diff = cv2.GaussianBlur(difference_img, (3, 3), 0)

    # Create a single channel image
    _, difference_single_channel = cv2.threshold(
        blurred_diff, threshold, 255, cv2.THRESH_BINARY
    )

    return difference_single_channel


def compute_binary_mask(difference_single_channel, threshold=50):

    # Create a binary mask
    _, difference_binary = cv2.threshold(
        difference_single_channel, threshold, 255, cv2.THRESH_BINARY
    )
    return difference_binary


def replace_background(bg1_image, bg2_image, ob_image, threshold=50):

    difference_single_channel = compute_difference(
        bg1_image, ob_image, threshold)

    binary_mask = compute_binary_mask(difference_single_channel, threshold)

    # Create the output image by replacing the background
    output = np.where(binary_mask[:, :, np.newaxis]
                      == 255, ob_image, bg2_image)

    return output


if __name__ == "__main__":
    # Testing
    output_image = replace_background(
        bg1_image, bg2_image, ob_image, threshold=1)

    # Display the final output
    cv2.imshow("Final Output", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
