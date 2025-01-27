import cv2
import time
import numpy as np
import pickle
import mysql.connector
from datetime import datetime
from retinaface import RetinaFace
from insightface.app import FaceAnalysis

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="persons"
        )
        if connection.is_connected():
            print("Connected to database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def load_embeddings_from_db(connection):
    embeddings = {}
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT username, embedding FROM face_embeddings")
        for username, embedding_blob in cursor.fetchall():
            embedding = pickle.loads(embedding_blob)
            embeddings[username] = embedding
        cursor.close()
        print("Embeddings loaded from database.")
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    return embeddings

def update_time_present(connection, username):
    try:
        cursor = connection.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("UPDATE face_embeddings SET time_present = %s WHERE username = %s", (current_time, username))
        connection.commit()
        cursor.close()
       # print(f"Updated presence time for {username} to {current_time}.")
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
cap = cv2.VideoCapture(0)

face_app = FaceAnalysis(providers=['CPUExecutionProvider'])
face_app.prepare(ctx_id=0, det_size=(640, 640))

connection = connect_to_db()
embeddings = load_embeddings_from_db(connection)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break
    frame = cv2.flip(frame, 1)
    faces = RetinaFace.detect_faces(frame)
    if isinstance(faces, dict):
        for face_id, face_info in faces.items():
            if 'facial_area' in face_info:
                facial_area = face_info['facial_area']
                x1, y1, x2, y2 = facial_area
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)

                detected_faces = face_app.get(frame)
                if len(detected_faces) > 0:
                    face_feature = detected_faces[0].embedding
                    best_match_score = -1
                    best_match_name = None

                    for name, stored_embedding in embeddings.items():
                        similarity = np.dot(stored_embedding, face_feature) / (np.linalg.norm(stored_embedding) * np.linalg.norm(face_feature))
                       # print(f"Similarity Score with {name}: {similarity}")

                        if similarity > best_match_score:
                            best_match_score = similarity
                            best_match_name = name

                    if best_match_score > 0.4:  
                        match_status = f'{best_match_name}'
                        cv2.putText(frame, match_status, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 1)
                        update_time_present(connection, best_match_name)
                    else:
                        match_status = 'Unidentified'
                        cv2.putText(frame, match_status, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 1)

    cv2.imshow('Real-Time Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if connection:
    connection.close()
