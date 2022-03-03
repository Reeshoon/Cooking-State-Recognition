import os
from glob import glob
import cv2


for dir in os.listdir('train'):
    source_dir = os.path.join("train", dir)
    img_path = glob(source_dir + "/*")
    img_dic = {}
    for i in range(len(img_path)):
        img = cv2.imread(img_path[i])
        img =cv2.resize(img, (300,300))
        cv2.imwrite(img_path[i], img)
for dir in os.listdir('train'):
    source_dir = os.path.join("train", dir)
    img_path = glob(source_dir + "/*")
    img_dic = {}
    for i in range(len(img_path)):
        img = cv2.imread(img_path[i])
        # img.shape
        if img.shape in img_dic.keys():
            img_dic[img.shape]+=1
        else:
            img_dic[img.shape] = 1
 
print(img_dic)