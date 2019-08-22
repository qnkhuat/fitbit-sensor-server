# https://gist.github.com/kylehounslow/767fb72fde2ebdd010a0bf4242371594
import requests
import cv2
import base64
import json
import time

start = time.time()
url = 'http://0.0.0.0:8085/emotion/analyze'
img_file = 'images/test.png'

with open(img_file, "rb") as image_file:
    payload= base64.b64encode(image_file.read())

headers = {'content-type' : 'application/json'}
headers = {'content-type' : 'base64'}
params = {}

response = requests.post(url, data=payload, params=params,headers=headers)
print(response.text)
print(f'Total time : {time.time() -start }')
