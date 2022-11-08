import cv2 
import numpy as np
import pytesseract
from pytesseract import Output

#psm stands for page segmantation mode and oem stands for OCR engine mode
custom_config = r'--oem 3 --psm 11'

img = cv2.imread("text_1.png")

#get shape of image
height, width, _ = img.shape

#print text recognized
#text = pytesseract.image_to_string(img, config=custom_config)
#print(text)

#get coordinates of boxes
#boxes = pytesseract.image_to_boxes(img, config=custom_config)
#form boxes around the text recognized
"""for box  in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)"""



#to have boxes around whole text rather then single letters
data = pytesseract.image_to_data(img,config=custom_config,output_type=Output.DICT)
n_boxes = len(data['text'])
for i in range(n_boxes):
    if float(data['conf'][i]) > 20:
        (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        img = cv2.putText(img, data["text"][i], (x,y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)