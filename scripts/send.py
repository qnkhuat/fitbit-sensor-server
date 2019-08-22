# https://gist.github.com/kylehounslow/767fb72fde2ebdd010a0bf4242371594
import requests
import cv2
import base64
import json
import time
#import curlify

start = time.time()
#url = 'http://0.0.0.0:5000/api/v1/emotion/'
#url = 'https://ai.kidtopi.com/api/emotion/predict'
#url = 'https://ai.kidtopi.com/api/v1/emotion'
url = 'http://202.134.19.193:8088/predict'
#img_file = 'images/notface.png'
img_file = 'images/test.png'

with open(img_file, "rb") as image_file:
    payload= base64.b64encode(image_file.read()) # bytes
    payload = payload.decode('utf-8') # str

headers = {'content-type' : 'application/json'}
#headers = {'content-type' : 'base64'}
params = {}

response = requests.post(url, data=json.dumps({'data':payload}), params=params,headers=headers)
#response = requests.post(url, data=payload, params=params,headers=headers)
#print(curlify.to_curl(response.request))
print(response.text)
print(f'Total time : {time.time() -start }')
