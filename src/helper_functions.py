import numpy as np
import matplotlib.pyplot as plt
import re
import pandas as pd

# used to look at images
import cv2 as cv

# tensorflow - for CNN
import tensorflow as tf
from tensorflow.keras.models import Model, load_model


dog_classifier_model = load_model('/Users/belindanguyen/Desktop/Galvanize/Capstones/whos-a-good-boy/dog_classifier_model.h5')
vgg16_dog_classifier = load_model('/Users/belindanguyen/Desktop/Galvanize/Capstones/whos-a-good-boy//vgg16_dog_classifier_model.h5')

def inception_breed_predict(img_path, lst):
    '''
    Parameters:
    img_path: file path to image
    lst: list of breeds

    Returns:
    image of dog and breed prediction
    '''
    # read in image
    img = cv.imread(img_path)

    # resize for model
    img = cv.resize(img, (224, 224))

    # add another dimension
    img_NN = np.expand_dims(img, axis = 0)

    prediction = dog_classifier_model.predict(img_NN)

    # get the highest prediction's index
    prediction = np.array(tf.argmax(prediction, axis = 1))[0]
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.axis('off')
    text_predict = f"You are most likely a {re.sub('_', ' ', lst[prediction])}.\nYou are definitely a good dog!"
    plt.text(x=120, y = -15, s = text_predict, size = 20, ha = 'center',
        bbox=dict(boxstyle = 'round', facecolor = '#89CFF0', alpha = 0.5))


def vgg_breed_predict(img_path, lst):
    '''
    Parameters:
    img_path: file path to image
    lst: list of breeds

    Returns:
    image of dog and breed prediction
    '''
    # read in image
    img = cv.imread(img_path)

    # resize for model
    img = cv.resize(img, (224, 224))

    # add another dimension
    img_NN = np.expand_dims(img, axis = 0)

    prediction = vgg16_dog_classifier.predict(img_NN)

    # get the highest prediction's index
    prediction = np.array(tf.argmax(prediction, axis = 1))[0]
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.axis('off')
    text_predict = f"You are most likely a {re.sub('_', ' ', lst[prediction])}.\nYou are definitely a good dog!"
    plt.text(x=120, y = -15, s = text_predict, size = 20, ha = 'center',
        bbox=dict(boxstyle = 'round', facecolor = '#89CFF0', alpha = 0.5))
