import os
import sys
# dl libraries
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model
from keras.processing.image import ImageDataGenerator

MODEL_FILEPATH = sys.argv[2]
TRAIN_LOCATION = '/media/fury/data/Scripts/the_movies_data_scraper/datasets/The_Movies/posters/train'
TEST_LOCATION = '/media/fury/data/Scripts/the_movies_data_scraper/datasets/The_Movies/posters/test'
VALIDATION_LOCATION = '/media/fury/data/Scripts/the_movies_data_scraper/datasets/The_Movies/posters/validation'

def create_generator(location):
    '''
    Takes the location of the images and returns a data generator
    '''
    datagen = ImageDataGenerator(rescale = 1./255)
    generator = datagen.flow_from_directory(
        location,
        target_size = (300, 300),
        color_mode = 'rgb',
        batch_size = 8,
        class_mode = 'categorical',
        seed = 42
    )

    return generator    

def load_model():
    model = load_model(MODEL_FILEPATH)
    print('Model Loaded.')
    return model

