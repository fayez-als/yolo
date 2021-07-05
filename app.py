
import base64
import os

from flask import Flask,jsonify,request 
from flask_restful import Api, Resource


import requests
import subprocess
import json


from flask_cors import CORS, cross_origin
from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps





app = Flask(__name__)
cors =CORS(app,resources={r"/upload":{"origins":"*"}})
app.config['CORS_HEADERS']= 'Content-Type'


@app.route('/')
def home():
    return 'working!'


@app.route('/upload',methods=['POST'])
@cross_origin(origin="*",headers=['Content-Type','Authorization'])
def upload_files():
    uploaded_file = request.files['image']
    if uploaded_file.filename !="":
        uploaded_file.save('guitar.jpg')
        os.system('./darknet detect cfg/yolov3.cfg yolov3.weights guitar.jpg')


    
        
        os.remove("guitar.jpg")

        
        with open("predictions.jpg", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        os.remove("predictions.jpg")
        

        return encoded_string
    


    return jsonify({"result":"detected currectly"})


if __name__=='__main__':
    app.run(host='0.0.0.0')


