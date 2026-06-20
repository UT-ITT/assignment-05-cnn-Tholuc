import os
import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# --- CONFIGURATION ---
MODEL_PATH = 'gesture_recognition.keras'      # Your saved CNN model
CUSTOM_DATA_DIR = './my_custom_dataset'       # Folder containing ALL images
ANNOTATION_FILES = ['annot-your_name.json', 'annot-tutors.json'] # Both JSONs

IMG_SIZE = 64
COLOR_CHANNELS = 3

# CRITICAL: This MUST match the order used during training (e.g., model.predict output)
LABEL_NAMES = ['like', 'rock', 'peace', 'no-gesture'] 

def preprocess_image(img):
    """Convert to format expected by your CNN."""
    if COLOR_CHANNELS == 1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    return img_resized

def main():
    print(f"Loading model from {MODEL_PATH}...")
    model = load_model(MODEL_PATH)

    # Merge annotations from all provided files
    annotations = {}
    print(f"Merging annotation files: {ANNOTATION_FILES}...")
    for file in ANNOTATION_FILES:
        with open(file, 'r') as f:
            data = json.load(f)
            annotations.update(data)

    images = []
    true_labels = []

    print("Processing images and extracting bounding boxes...")
    for filename in os.listdir(CUSTOM_DATA_DIR):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
            
        uid = filename.split('.')[0]
        if uid not in annotations:
            continue
            
        img_path = os.path.join(CUSTOM_DATA_DIR, filename)
        img = cv2.imread(img_path)
        if img is None: continue
            
        anno = annotations[uid]
        
        # Process every annotated hand in the image
        for i, bbox in enumerate(anno['bboxes']):
            x1 = int(bbox[0] * img.shape[1])
            y1 = int(bbox[1] * img.shape[0])
            w = int(bbox[2] * img.shape[1])
            h = int(bbox[3] * img.shape[0])
            x2 = x1 + w
            y2 = y1 + h
            
            crop = img[y1:y2, x1:x2]
            if crop.size == 0: continue
                
            images.append(preprocess_image(crop))
            true_labels.append(anno['labels'][i])

    if not images:
        print("Error: No images found. Check file names and JSON keys.")
        return

    # Prepare data for prediction
    X_test = np.array(images).astype('float32') / 255.0
    X_test = X_test.reshape(-1, IMG_SIZE, IMG_SIZE, COLOR_CHANNELS)

    print("Running predictions...")
    y_pred_probs = model.predict(X_test)
    y_pred_indices = np.argmax(y_pred_probs, axis=1)

    try:
        y_true_indices = [LABEL_NAMES.index(lbl) for lbl in true_labels]
    except ValueError as e:
        print(f"Error: Label mismatch! Check LABEL_NAMES array. Details: {e}")
        return

    print("Generating confusion matrix...")
    cm = confusion_matrix(y_true_indices, y_pred_indices, labels=range(len(LABEL_NAMES)))
    
    fig, ax = plt.subplots(figsize=(8, 8))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=LABEL_NAMES)
    disp.plot(ax=ax, cmap='Blues', xticks_rotation=45)
    
    plt.title('Confusion Matrix: Custom Dataset')
    plt.tight_layout()
    plt.savefig('conf-matrix.png', dpi=300)
    print("Success! 'conf-matrix.png' has been saved.")

if __name__ == "__main__":
    main()