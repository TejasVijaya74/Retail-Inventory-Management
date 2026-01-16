import os

IMAGE_DIR = 'data/cleaned'
LABEL_DIR = 'labels'

def check_annotation_quality(image_dir, label_dir):
    # Get filenames without extensions
    images = [os.path.splitext(f)[0] for f in os.listdir(image_dir) if f.endswith((".jpg", ".png"))]
    labels = [os.path.splitext(f)[0] for f in os.listdir(label_dir) if f.endswith(".txt")]
    
    missing_labels = [img for img in images if img not in labels]
    
    print("-" * 30)
    print("DATA QUALITY REPORT")
    print("-" * 30)
    if not missing_labels:
        print("SUCCESS: All images have corresponding YOLO label files.")
    else:
        print(f"FAILED: {len(missing_labels)} images are missing labels.")
        print(f"Missing items: {missing_labels}")
    print("-" * 30)

if __name__ == "__main__":
    check_annotation_quality(IMAGE_DIR, LABEL_DIR)