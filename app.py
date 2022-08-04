import cv2
import time
from flask import Flask, request, Response,render_template
import json
import detect
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))#basedir：D:\\yolov5\\yolov5
class_names = ['ore carrier','general cargo ship','bulk cargo carrier','container ship','fishing boat','passenger ship']
file_name = ['jpg','jpeg','png']

@app.route('/images', methods= ['POST'])
def get_image():
    image = request.files["images"]
    path = basedir + "\\data\\images"
    image_name = image.filename
    file_path = path + image.filename
    image.save(file_path)
    Path = 'yolov5/data/images'
    if image_name.split(".")[-1] in file_name:
        detect_api = detect.DetectAPI(exist_ok=True)
        img = cv2.imread(file_path)
        cv2.imwrite(os.path.join(path, 'test.jpg'), img)
        label = detect_api.run()
        with open("runs/detect/myexp/test.jpg", 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype='image/jpeg')
        try:
            return resp
            #return Response(response=lable, status=200, contenetype='text/html;charset=utf-8')
        except:
            return render_template('index1.html')
@app.route('/')
def upload_file():
   return render_template('index1.html')
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

