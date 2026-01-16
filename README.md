# Retail Inventory Management – Dataset Preparation & QA

This repository focuses on **data collection, preprocessing, annotation, and quality assurance** for a retail inventory management use case using **YOLO-format object detection data**.

---

## What I Accomplished

### 1. Data Collection & Pre-processing
- **Raw Data**: Collected diverse images of retail grocery shelves under varying lighting conditions and angles.
- **Automation**: Developed a Python script using **OpenCV** to resize and normalize all images to **640 × 640**, ensuring consistency for model training.

---

### 2. Annotation Workflow
- **Tool Used**: Migrated from *LabelImg* to **Label Studio** for a more scalable, web-based annotation experience.
- **Dataset Volume**: Annotated **6 high-resolution shelf images** containing multiple product instances.
- **Class Labels**:
  - `Product`
  - `Price_Tag`
  - `Void`
- **Format**: Exported annotations in **YOLO v8** format.
- **Best Practices**:
  - Followed **tight bounding box** labeling standards
  - Removed random UI-generated filename prefixes to maintain clean dataset structure

---

### 3. Quality Assurance (QA)
- **Technical Validation**: Implemented a custom Python script to verify correct **image-to-label mapping**.
- **Integrity Checks**:
  - Ensured no images were missing annotations
  - Prevented silent dataset corruption before training
- **Outcome**: High-confidence, training-ready dataset

---

## Project Structure

```plaintext
├── data/
│   ├── raw/           # Original images
│   └── cleaned/       # Standardized 640x640 images
├── labels/            # Final YOLO .txt annotations
├── scripts/
│   ├── preprocess.py  # OpenCV resizing script
│   └── validate_qa.py # Integrity check script
├── classes.txt        # Label definitions
└── README.md
