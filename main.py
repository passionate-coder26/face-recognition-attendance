import encode_faces
import face_detection

if _name_ == "_main_":
    # Step 1: Encode faces from the images directory
    print("Encoding faces from the images directory...")
    encode_faces.encode_faces("images")
    print("Face encoding completed.")

    # Step 2: Start face detection and attendance marking
    print("Starting face detection and attendance marking...")
    face_detection.recognize_faces()
    print("Face detection and attendance marking completed.")
