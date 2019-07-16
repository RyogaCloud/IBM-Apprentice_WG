import json
from ibm_watson import VisualRecognitionV3
from datetime import datetime
import cv2

visual_recognition = VisualRecognitionV3(
    '2018-03-19',  #使用するバージョン
    iam_apikey='(APIキー)')  #自分のVisual RecognitionのAPIキー

# Video Captureのインスタンスの作成
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("image", frame)

    key = cv2.waitKey(1)&0xff
    if key == ord('q'):
        break
    elif key == ord('p'):
        date = date = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = "./images/" + date + ".jpg"
        cv2.imwrite(path, frame)
        image = './images/{}.jpg'.format(date)
        with open(image, 'rb') as images_file:
            faces = visual_recognition.detect_faces(images_file).get_result()
        
        target = faces["images"][0]["faces"][0]
        age_max = target["age"]["max"]
        gender = target["gender"]["gender"]

        edframe = cv2.imread(image)
       
        cv2.putText(edframe, "gender:{}  age:{}".format(gender, age_max), (300, 600), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 8)

        cv2.imshow("Edited Frame", edframe)

