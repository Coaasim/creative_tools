import cv2
import numpy as np
import random

def create_blank_image(width, height, color=(0, 0, 0)):
    """Create a blank image with the given width, height, and background color."""
    image = np.zeros((height, width, 3), np.uint8)
    image[:] = color
    return image

def draw_random_lines(image, num_lines=10):
    """Draw random lines on the image."""
    height, width, _ = image.shape
    for _ in range(num_lines):
        pt1 = (random.randint(0, width), random.randint(0, height))
        pt2 = (random.randint(0, width), random.randint(0, height))
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        thickness = random.randint(1, 5)
        cv2.line(image, pt1, pt2, color, thickness)

def draw_random_circles(image, num_circles=10):
    """Draw random circles on the image."""
    height, width, _ = image.shape
    for _ in range(num_circles):
        center = (random.randint(0, width), random.randint(0, height))
        radius = random.randint(10, min(height, width) // 5)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        thickness = random.randint(-1, 5)  # -1 for filled circle
        cv2.circle(image, center, radius, color, thickness)

def add_noise(image, noise_level=0.05):
    """Add random noise to the image."""
    noise = np.random.randint(0, 256, image.shape, dtype=np.uint8)
    mask = np.random.rand(*image.shape[:2]) < noise_level
    image[mask] = noise[mask]
    
def save_image(image, filename):
    """Save the generated image to disk."""
    cv2.imwrite(filename, image)

def main():
    # Image dimensions and background color
    width, height = 800, 600
    background_color = (255, 255, 255)  # White background

    # Create a blank image
    image = create_blank_image(width, height, background_color)

    # Apply different patterns
    draw_random_lines(image, num_lines=15)
    draw_random_circles(image, num_circles=10)
    add_noise(image, noise_level=0.02)

    # Save the generated image
    output_filename = 'abstract_image.png'
    save_image(image, output_filename)
    print(f"Image saved as {output_filename}")

if __name__ == "__main__":
    main()
