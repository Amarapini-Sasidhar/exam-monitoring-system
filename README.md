# Secure Examination Monitoring System (SEMS)

A Python-based examination monitoring prototype that combines user authentication, webcam-based monitoring, computer vision, suspicion scoring, and examination management features.

The project is designed as a local application for experimenting with automated exam monitoring and security-related workflows.

## Features

### Authentication & User Roles

* Student and Faculty registration and login
* Role-based access to application features
* Password hashing using `bcrypt`
* Username and role validation

### Student Features

* View student marks
* View faculty notifications
* Submit anonymous feedback

### Faculty Features

* Update student marks
* Post notifications
* Start webcam-based monitoring sessions
* Generate suspicion score visualizations
* Export suspicion reports to CSV and PDF
* Initialize file integrity hashes
* Check monitored files for tampering

### Automated Exam Monitoring

The monitoring module uses the computer's webcam and performs basic computer-vision checks during a monitoring session.

It currently includes:

* Webcam capture using OpenCV
* Face detection using OpenCV Haar Cascades
* Object detection using YOLOv8
* Detection of multiple faces
* Detection of objects such as cell phones and books
* Rule-based suspicion scoring
* Suspicious-frame capture
* Session video recording
* Timestamped suspicion logging

### File Integrity Monitoring

The project includes a basic file-integrity mechanism using SHA-256 hashes.

The system can:

* Generate baseline hashes for selected data files
* Recalculate hashes during later checks
* Report files whose contents have changed

### Reporting

Monitoring data can be exported as:

* CSV
* PDF

A simple matplotlib-based visualization is also available for reviewing suspicion scores over time.

---

## Technology Stack

* **Language:** Python 3
* **GUI / Interface:** Command-line interface
* **Computer Vision:** OpenCV
* **Object Detection:** YOLOv8 via Ultralytics
* **Authentication:** bcrypt
* **Data Storage:** JSON and text files
* **Data Processing:** pandas
* **Visualization:** Matplotlib
* **Reporting:** FPDF
* **Concurrency / Processing:** Python standard libraries

---

## Project Structure

```text
exam-monitoring-system/
│
├── data/
│   ├── feedback.txt
│   ├── marks.json
│   ├── notifications.json
│   ├── suspicion_log.json
│   └── users.json
│
├── sessions/
│   └── .gitkeep
│
├── suspicious_frames/
│   └── .gitkeep
│
├── src/
│   ├── auth.py
│   ├── cheat_detection.py
│   ├── dashboard.py
│   ├── export.py
│   ├── face_detection.py
│   ├── feedback.py
│   ├── hash_check.py
│   ├── hashing.py
│   ├── heatmap.py
│   ├── main.py
│   ├── marks.py
│   ├── notifications.py
│   ├── suspicion_log.json
│   ├── yolo_detector.py
│   └── yolov8n.pt
│
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Amarapini-Sasidhar/exam-monitoring-system.git
cd exam-monitoring-system
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The project requires:

* `bcrypt`
* `opencv-python`
* `ultralytics`
* `matplotlib`
* `fpdf`
* `pandas`
* `torch`

A working webcam is required for the monitoring functionality.

---

## Running the Application

From the `src` directory:

```bash
cd src
python main.py
```

The application provides a command-line menu for authentication and role-based functionality.

---

## Monitoring Workflow

A Faculty user can start a monitoring session and specify the monitoring duration.

During the session, the application:

1. Captures frames from the webcam.
2. Detects faces using OpenCV.
3. Detects objects using YOLOv8.
4. Calculates a rule-based suspicion score.
5. Captures selected suspicious frames.
6. Records the monitoring session as an MP4 video.
7. Stores timestamped suspicion information.

The current scoring rules include:

| Detection           | Score |
| ------------------- | ----: |
| Multiple faces      |   +20 |
| Cell phone detected |   +20 |
| Book detected       |   +10 |

The highest observed suspicion score is retained during the session.

---

## Output Files

Depending on the operations performed, the application can generate:

* Monitoring session videos
* Suspicious frame images
* Suspicion logs
* CSV reports
* PDF reports
* File-integrity hash records

Generated runtime files should be treated as local application data.

---

## File Integrity Checking

The project includes a simple SHA-256 based integrity-checking mechanism.

Faculty users can initialize hashes for selected data files and later run an integrity check to identify files whose contents have changed.

This provides a basic demonstration of file-integrity monitoring rather than a complete tamper-proof evidence system.

---

## Limitations

This project is currently a **prototype for learning and experimentation** rather than a production-ready examination platform.

Current limitations include:

* Local JSON/text-file storage instead of a centralized database
* Command-line based user interface
* Local webcam monitoring
* Rule-based suspicion scoring
* Basic face and object detection
* No distributed or cloud deployment
* No centralized multi-user monitoring infrastructure
* No dedicated web frontend
* No production-grade evidence management system

The object-detection and suspicion rules can produce false positives and should not be treated as definitive evidence of cheating.

---

## Future Improvements

Possible future improvements include:

* Web-based student and faculty interfaces
* Database-backed persistence
* More sophisticated behavioral analysis
* Improved detection and tracking
* Configurable suspicion rules
* Authentication and authorization improvements
* Secure storage of monitoring recordings
* Automated testing
* Better logging and error handling
* Containerized deployment
* Centralized monitoring for multiple examination sessions

---

## Disclaimer

This project is intended for educational purposes and authorized testing/development environments.

Automated monitoring results should be reviewed by a human and should not be used as the sole basis for determining academic misconduct.

---

## Author

**Amarapini Sasidhar**

GitHub: [Amarapini-Sasidhar](https://github.com/Amarapini-Sasidhar)
