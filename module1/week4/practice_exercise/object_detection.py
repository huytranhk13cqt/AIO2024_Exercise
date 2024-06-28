import cv2
import numpy as np
import streamlit as st
from PIL import Image

# Paths to the pre-trained model and prototxt file
MODEL = "model/MobileNetSSD_deploy.caffemodel"
PROTOTXT = "model/MobileNetSSD_deploy.prototxt.txt"


# Function to read class labels from a file
def load_classes(file_path):
    with open(file_path, 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    return classes


# Load the class labels from the text file
CLASSES = load_classes("model/mobileNet_SSD_labels.txt")


# Function to process an image and detect objects
def process_image(image):

    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
    )
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()

    return detections


# Function to annotate the image with bounding boxes and labels
def annotate_image(image, detections, confidence_threshold=0.5):

    (height, width) = image.shape[:2]

    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > confidence_threshold:
            # Extract the index of the class label from the detections,
            # then compute the (x, y)-coordinates of the bounding box for the object
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * \
                np.array([width, height, width, height])
            (start_x, start_y, end_x, end_y) = box.astype("int")

            # Draw the bounding box and label on the image
            label = f"{CLASSES[idx]}: {confidence:.2f}"
            cv2.rectangle(image, (start_x, start_y),
                          (end_x, end_y), (0, 255, 255), 2)
            y = start_y - 15 if start_y - 15 > 15 else start_y + 15
            cv2.putText(image, label, (start_x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
    return image


def main():
    st.title('Object Detection for Images')
    file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])

    if file is not None:
        st.image(file, caption="Uploaded Image")
        image = Image.open(file)
        image = np.array(image)
        detections = process_image(image)
        processed_image = annotate_image(image, detections)
        st.image(processed_image, caption="Processed Image")


if __name__ == "__main__":
    main()
