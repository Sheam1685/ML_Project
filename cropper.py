import cv2
import os

def detect_and_crop_faces(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # get the image name
    image_name = os.path.basename(image_path)

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained Haarcascades face detector from OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Crop and save the faces
    for i, (x, y, w, h) in enumerate(faces):
        if i > 0:
            print(image_path)
        # Add a little extension to the cropping region
        extension = 10
        x -= extension
        y -= extension
        w += 2 * extension
        h += 2 * extension

        # Crop the face
        cropped_face = image[y:y + h, x:x + w]

        # Save the cropped face as 100x100 image
        cropped_face = cv2.resize(cropped_face, (100, 100))
        output_face_path = os.path.join(output_path, f"{image_name}_{i+1}.png")
        cv2.imwrite(output_face_path, cropped_face)
        # print(f"Face {i+1} saved at: {output_face_path}")

def process_images(images_dir, des_dir):
    # Loop through each folder in images_dir
    for folder_name in os.listdir(images_dir):
        folder_path = os.path.join(images_dir, folder_name)

        # Skip if not a directory
        if not os.path.isdir(folder_path):
            continue

        # Create corresponding folder in des_dir
        des_folder_path = os.path.join(des_dir, folder_name)
        os.makedirs(des_folder_path, exist_ok=True)

        # Loop through each image in the folder
        for image_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_name)
            
            # Skip if not an image file
            if not os.path.isfile(image_path) or not image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                print(f"Skipping non-image file: {image_path}")
                continue

            # Process and save cropped faces
            detect_and_crop_faces(image_path, des_folder_path)

# Example usage
images_dir = 'C:\\Users\\samia\\Documents\\ML_Project\\ckplus_data'
des_dir = 'C:\\Users\\samia\\Documents\\ML_Project\\ckplus_cropped_faces'
process_images(images_dir, des_dir)