import os
import datetime
import base64
import numpy as np
import cv2
import json
import random

def encode_payload(payload):
    payload = payload.decode('utf8')
    payload += "=" * ((4 - len(payload) % 4) % 4)
    #payload = json.loads(payload)
    return payload


def bytes2array(data):
    data = data.decode('utf8')
    data = base64.b64decode(data)
    array = np.fromstring(data, np.uint8)
    image = cv2.imdecode(array, cv2.IMREAD_UNCHANGED)
    return image 
 

def create_save_dir(root='upload'):
    # store images with folder name by days
    today = datetime.datetime.today()
    save_dir = os.path.join(root,today.strftime('%Y/%m/%d'))
    os.makedirs(save_dir,exist_ok=True)
    return save_dir

def save_image_today(image,root):
    """
    Save image to the folder by date
    """
    assert root in ['upload/raw','upload/face'],"Root folder are not allowed"
    today = datetime.datetime.today()
    save_dir = create_save_dir(root)
    filename = str(int(today.timestamp()))+'_'+ str(random.randint(0,1000)) +'.jpg'
    filedir = os.path.join(save_dir,filename)
    cv2.imwrite(filedir,image)
    return filedir
