import cv2
import os

# Define paths relative to the root folder
INPUT_DIR = 'data/raw'
OUTPUT_DIR = 'data/cleaned'

def preprocess_images(input_path, output_path, size=(640, 640)):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Check if raw folder is empty
    files = [f for f in os.listdir(input_path) if f.endswith((".jpg", ".png", ".jpeg"))]
    if not files:
        print(f"No images found in {input_path}. Please add some images first!")
        return

    for filename in files:
        img = cv2.imread(os.path.join(input_path, filename))
        if img is not None:
            # Resize image to 640x640
            resized_img = cv2.resize(img, size)
            cv2.imwrite(os.path.join(output_path, filename), resized_img)
            print(f"Processed and saved: {filename}")

if __name__ == "__main__":
    preprocess_images(INPUT_DIR, OUTPUT_DIR)