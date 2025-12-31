from ultralytics import YOLO

# Load YOLOv8 model (first run downloads it automatically)
model = YOLO("yolov8n.pt")  # Small and fast

def detect_objects(frame):
    results = model.predict(source=frame, conf=0.5, verbose=False)
    detected = []
    for result in results:
        for c in result.boxes.cls:
            label = model.names[int(c)]
            detected.append(label.lower())

    print("🧠 Detected objects:", detected)  # For debug
    return detected
