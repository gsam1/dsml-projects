import os
import sys
# dl libraries
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator


MODEL_FILEPATH = sys.argv[1]
TRAIN_LOCATION = '/media/fury/data/Scripts/the_movies_data_scraper/datasets/The_Movies/posters/train'
TEST_LOCATION = '/media/fury/data/Scripts/the_movies_data_scraper/datasets/The_Movies/posters/test'
VALIDATION_LOCATION = '/media/fury/data/Scripts/the_movies_data_scraper/datasets/The_Movies/posters/validation'
# Check if number of epochs are defined
try:
    EPOCHS = int(sys.argv[2])
except IndexError:
    EPOCHS = 10

def create_generator(location):
    '''
    Takes the location of the images and returns a data generator
    '''
    datagen = ImageDataGenerator(rescale = 1./255)
    generator = datagen.flow_from_directory(
        location,
        target_size = (224, 224),
        color_mode = 'rgb',
        batch_size = 8,
        class_mode = 'categorical',
        shuffle = False
    )

    return generator    

def load_compiled_model():
    model = load_model(MODEL_FILEPATH)
    print('Model Loaded.')
    return model

def save_trained_model(model, name):
    model.save(name + '.model')
    print('Model %s saved.' % (name))

def train_model(model, train_generator, validation_generator):
    model.fit_generator(train_generator,
                         steps_per_epoch = train_generator.n // train_generator.batch_size,
                         epochs = EPOCHS,
                         validation_data = validation_generator,
                         validation_steps = validation_generator.n // validation_generator.batch_size)
    print('Model training complete.')
    return model


if __name__ == '__main__':
    # create train, validate and test generators
    train_generator = create_generator(TRAIN_LOCATION)
    validation_generator = create_generator(VALIDATION_LOCATION)
    test_generator = create_generator(TEST_LOCATION)
    # load pre-compiled model
    model = load_compiled_model()
    # train the model
    model_trained = train_model(model, train_generator, validation_generator)
    # save the model
    save_trained_model(model_trained, 'models/clf_trained')

    print('Execution done!')



