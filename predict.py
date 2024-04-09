import tensorflow as tf 
classifierLoad = tf.keras.models.load_model('model.h5') # load the model here
import pandas as pd
import numpy as np
import cv2
from keras.preprocessing import image
test_image1 = cv2.imread('3.jpg',0)
test_image = image.load_img('5.jpg', target_size = (200,200))  # load the sample image here
#test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifierLoad.predict(test_image)
if result[0][0] == 1:
    print("briyani")
    print("High in calories, saturated fats, and may lack balanced nutrition.")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('briyani.xlsx')
    print(df)
elif result[0][1] == 1:
    print("burger")
    print("Loaded with unhealthy fats, calories, and sodium, contributing to poor cardiovascular health")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('burger.xlsx')
    print(df)
elif result[0][2] == 1:
    print("dosa")
    print("High glycemic index and potential for unhealthy frying methods.")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('dosa.xlsx')
    print(df)
elif result[0][3] == 1:
    print("idly")
    print("Low in essential nutrients and may lead to blood sugar spikes.")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('idly.xlsx')
    print(df)
elif result[0][4] == 1:
    print("noodles")
    print("Often processed and high in sodium, leading to potential health issues ")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('noodles.xlsx')
    print(df)
elif result[0][5] == 1:
    print("pizza")
    print("Often high in calories, saturated fats, and sodium ")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('pizza.xlsx')
    print(df)
elif result[0][6] == 1:
    print("soup")
    print("Some varieties may be high in sodium and lack sufficient nutrients. ")
    test_image1 = cv2.resize(test_image1, (380,360))                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    df = pd.read_excel('soup.xlsx')
    print(df)
  # this are results



