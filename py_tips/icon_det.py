##!/Anaconda/envs/py37_vis/python
# -*- coding: utf-8 -*-
##!/usr/bin/python
## -*- coding: utf-8 -*-
#
# ref:
# Python __init__.py Uasge :
#  https://www.cnblogs.com/Lands-ljk/p/5880483.html
#  https://www.cnblogs.com/AlwinXu/p/5598543.html
#
#
#
# https://github.com/akshaybahadur21/Detecting-Mouse-Pointer-Using-Tensorflow
#
# 以下是一個使用TensorFlow實現的範例網址，可以辨識Windows 10中的鼠標位置：
#
# 這個預訓練的模型 'mouse_model.h5' 是基於深度學習技術的圖像分類模型，
# 能夠辨識 10 種不同的鼠標圖示，
# 包括箭頭、手指、水滴、沙漏、旋轉箭頭、旋轉圖案、十字形、放大鏡、文字輸入符號和縮小鏡。
#
# 這些鼠標圖示是從 Win10 系統中常見的圖示中挑選出來的，經過標記和裁剪後作為訓練數據，
# 模型通過學習這些訓練數據，能夠識別出 Win10 畫面中的這些鼠標圖示。
#
# 除了辨識鼠標圖示外，這個模型還能夠預測鼠標圖示在 Win10 畫面中的位置，
# 因此能夠幫助自動化程式定位到特定的鼠標圖示並進行相應的操作。
#
# mouse_model.h5 的訓練尺寸為 128x128，因此建議使用 resize() 將原圖像縮小為 128x128。
# 當然，如果時間和計算成本允許，也可以嘗試使用更大的尺寸進行辨識，以提高精度。
#
#

__version__ = 1.0
__author__ = 'JackHung@IEC'
__date__ = 20230418


import numpy as np
import cv2
from PIL import Image, ImageGrab 
import tensorflow as tf


model = tf.keras.models.load_model('mouse_model.h5')

while(True):
    # 捕捉屏幕上的圖像
    img = np.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080)))
    
    # 將圖像轉換為模型的輸入格式
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0)
    
    # 使用模型進行預測，得到鼠標位置的概率分布
    prediction = model.predict(img)[0]
    
    # 找到最大概率對應的鼠標位置
    max_idx = np.argmax(prediction)
    x = int(max_idx % 1920)
    y = int(max_idx / 1920)
    
    # 在屏幕上顯示鼠標位置
    cv2.circle(img, (x, y), 10, (0, 255, 0), -1)
    cv2.imshow

