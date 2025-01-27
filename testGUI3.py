import cv2
import pickle
import mysql.connector
import sys
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
            print("Connected to MySQL database!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def upload_embedding_to_db(username, embedding_data, connection):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO face_embeddings (username, embedding) VALUES (%s, %s)"
        cursor.execute(insert_query, (username, embedding_data))
        connection.commit()
        cursor.close()
        print("Embedding uploaded to database successfully!")
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

def process_image_and_upload(file_path, username, connection):
    face_app = FaceAnalysis(providers=['CPUExecutionProvider'])
    face_app.prepare(ctx_id=1, det_size=(640, 640))
    image = cv2.imread(file_path)
    faces = face_app.get(image)
    
    if faces:
        embedding_data = pickle.dumps(faces[0].embedding)
        upload_embedding_to_db(username, embedding_data, connection)
        print(f"Embedding generated and uploaded for username: {username}")
    else:
        print("No face detected in the image.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python testGUIwithoutGUI.py <image_path> <username>")
        sys.exit(1)
    
    file_path = sys.argv[1] 
    username = sys.argv[2]  
    
    connection = connect_to_db()
    
    if connection:
        process_image_and_upload(file_path, username, connection)
        connection.close()

if __name__ == "__main__":
    main()
