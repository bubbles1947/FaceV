from flask import Flask, Response, request, jsonify
import cv2
import numpy as np
import os
import subprocess
from retinaface import RetinaFace

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/process_frame', methods=['POST'])
def process_frame():
    file = request.files['frame'].read()
    npimg = np.frombuffer(file, np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    faces = RetinaFace.detect_faces(frame)
    if isinstance(faces, dict):
        for face_id, face_info in faces.items():
            facial_area = face_info['facial_area']
            x1, y1, x2, y2 = facial_area
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)
            landmarks = face_info['landmarks']
            for _, point in landmarks.items():
                cv2.circle(frame, (int(point[0]), int(point[1])), 2, (0, 0, 255), -1)

    _, jpeg = cv2.imencode('.jpg', frame)
    return Response(jpeg.tobytes(), mimetype='image/jpeg')
    
@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    username = request.form.get('username')
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    if not username:
        return jsonify({"error": "Username not provided"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    result = subprocess.run(
        ["python", "testGUI3.py", filepath, username],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        return jsonify({"error": result.stderr}), 500

    return jsonify({"message": "Image processed successfully", "username": username})

@app.route('/start_face_recognition', methods=['POST'])
def start_face_recognition():
    result = subprocess.run(
        ["python", "faceRecUpWtime.py"],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        return jsonify({"error": result.stderr}), 500

    return jsonify({"message": "Face recognition started"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
