import cv2
import time
from datetime import datetime
from yolo_detector import detect_objects
from face_detection import detect_faces
import json
import os

def start_monitoring_session(duration_minutes=1):
    cap = cv2.VideoCapture(0)
    width, height = int(cap.get(3)), int(cap.get(4))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    output_filename = f"session_{timestamp}.mp4"
    out = cv2.VideoWriter(output_filename, fourcc, 20.0, (width, height))

    start_time = time.time()
    session_duration = duration_minutes * 60
    max_suspicion_score = 0
    suspicion_log = []

    suspicious_folder = "suspicious_frames"
    os.makedirs(suspicious_folder, exist_ok=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        elapsed = time.time() - start_time
        if elapsed > session_duration:
            break

        # Detection
        faces = detect_faces(frame)
        objects = detect_objects(frame)

        current_score = 0
        if len(faces) > 1:
            current_score += 20
        if 'cell phone' in objects:
            current_score += 20
        if 'book' in objects:
            current_score += 10

        # Debug print
        print(f"[DEBUG] Faces: {len(faces)}, Objects: {objects}, Score: {current_score}")

        # Update suspicion score only if it's higher
        if current_score > max_suspicion_score:
            max_suspicion_score = current_score
            if max_suspicion_score >= 30:
                snap_name = f"{suspicious_folder}/suspicious_{int(elapsed)}s.jpg"
                cv2.imwrite(snap_name, frame)

        suspicion_log.append({
            "timestamp": round(elapsed, 2),
            "score": max_suspicion_score
        })

        # Overlay
        overlay = frame.copy()
        cv2.putText(overlay, f"Time: {int(elapsed)}s", (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(overlay, f"Suspicion Score: {max_suspicion_score}", (10, 55),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        out.write(overlay)
        cv2.imshow("Monitoring", overlay)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    with open("suspicion_log.json", "w") as f:
        json.dump(suspicion_log, f, indent=4)

    print(f"\n📹 Session saved as: {output_filename}")
    print(f"🧠 Suspicion log saved to: suspicion_log.json")
