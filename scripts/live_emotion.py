import cv2
import sys
import matplotlib.pyplot as plt
sys.path.insert(0,'../')

from src.emotion.models import load_model as load_emotion
from src.detect_face.inference import load_detection_model as load_face
from src.utils import *

vid = cv2.VideoCapture(0)
face_detector = load_face()
emotion_detector = load_emotion(model_name='resnet18-fastai')


while True:
    _,frame = vid.read()
    face = face_detector.find_biggest_face(frame)
    emotion = emotion_detector.predict_array(face)['emotion']
    cv2.imshow(emotion,frame)
    if 0x00==ord('q') & cv2.waitKey(1):
        break



