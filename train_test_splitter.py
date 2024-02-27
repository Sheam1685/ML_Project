import os
import shutil
from sklearn.model_selection import train_test_split

def split_emotion_images(emotion_folder, train_folder, test_folder, test_size=0.2, random_seed=None):
    # List all images in the emotion folder
    emotion_images = [f for f in os.listdir(emotion_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Split images into train and test sets
    train_images, test_images = train_test_split(emotion_images, test_size=test_size, random_state=random_seed)

    # Create train and test folders if they don't exist
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # Move train images to train folder
    for image in train_images:
        source_path = os.path.join(emotion_folder, image)
        dest_path = os.path.join(train_folder, image)
        shutil.move(source_path, dest_path)

    # Move test images to test folder
    for image in test_images:
        source_path = os.path.join(emotion_folder, image)
        dest_path = os.path.join(test_folder, image)
        shutil.move(source_path, dest_path)

# Paths
source_base_dir = 'C:\\Users\\samia\\Documents\\ML_Project\\ckplus_cropped_faces'
destination_base_dir = 'C:\\Users\\samia\\Documents\\ML_Project\\ckplus'

# Emotions
emotions = os.listdir(source_base_dir)

# Loop through each emotion folder
for emotion in emotions:
    emotion_folder = os.path.join(source_base_dir, emotion)
    
    # Create train and test directories for each emotion
    train_folder = os.path.join(destination_base_dir, 'train', emotion)
    test_folder = os.path.join(destination_base_dir, 'test', emotion)

    # Split images and move to train and test folders
    split_emotion_images(emotion_folder, train_folder, test_folder, test_size=0.2, random_seed=42)
