import cv2
import os
from insightface.app import FaceAnalysis
import pickle

face_app = FaceAnalysis(providers=['CPUExecutionProvider'])
face_app.prepare(ctx_id=1, det_size=(640, 640))

embeddings_dir = "embeddings"
if not os.path.exists(embeddings_dir):
    os.makedirs(embeddings_dir)

image_path = input("Please enter the path of the image to generate embeddings: ")
embedding_filename = input("Enter a unique name for the embedding (e.g., face1.pkl): ").strip()
image = cv2.imread(image_path)
if image is None:
    print("Error: Image not found.")
    exit()

faces = face_app.get(image)

if len(faces) > 0:
    for i, face in enumerate(faces):
        face_embedding = face.embedding

        # Generate a filename based on the image name and face index
      #  image_name = os.path.basename(image_path)
       # embedding_filename = f"{os.path.splitext(image_name)[0]}_face_{i+1}.pkl"
        #embedding_path = os.path.join(embeddings_dir, embedding_filename)
        with open(embedding_filename, 'wb') as f:
            pickle.dump(face_embedding, f)

        print(f"Generated and saved embedding to {embedding_filename}")
else:
    print("No faces detected in the image.")
