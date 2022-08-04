import cv2
import yolov5.detect
import os

video_capture = cv2.VideoCapture(0)
detect_api = yolov5 - master.detect.DetectAPI(exist_ok=True)

while True:
    k = cv2.waitKey(1)
ret, frame = video_capture.read()

path = '/root/autodl-tmp/ship/yolov5/data/images'
cv2.imwrite(os.path.join(path, 'test.jpg'), frame)

label = detect_api.run()
print(str(label))

image = cv2.imread('/root/autodl-tmp/ship/yolov5/runs/detect/myexp/test.jpg', flags=1)
cv2.imshow("video", image)

if k == 27:  # 按下ESC退出窗口
    break

video_capture.release()

