import os
import sys
# dl libraries
import keras
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator


MODEL_FILEPATH = sys.argv[1]
TRAIN_LOCATION = '/home/fury/Code/projects/dsml-projects/5_Playground/datasets/The_Movies/posters/train'
TEST_LOCATION = '/home/fury/Code/projects/dsml-projects/5_Playground/datasets/The_Movies/posters/test'
VALIDATION_LOCATION = '/home/fury/Code/projects/dsml-projects/5_Playground/datasets/The_Movies/posters/validation'
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
    )

    return generator

def create_aug_generator(location):
    '''
    Gets the location of the images and auguments the image.
    '''
    datagen = ImageDataGenerator(
        rescale = 1./255,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True)

    generator = datagen.flow_from_directory(
        location,
        target_size = (224, 224),
        color_mode = 'rgb',
        batch_size = 8,
        class_mode = 'categorical',
    )

    return generator    

def create_model():
    vgg16_model = keras.applications.vgg16.VGG16()
    model = Sequential()

    for layer in vgg16_model.layers[:-3]:
        model.add(layer)
    
    for layer in model.layers:
        layer.trainable = False
    
    model.add(Dense(4096, activation = 'relu'))
    model.add(Dense(4096, activation = 'relu'))
    model.add(Dense(23, activation = 'softmax'))
    
    model.compile(Adam(lr = .001), loss = 'binary_crossentropy', metrics = ['accuracy'])

    return model


def load_compiled_model():
    if MODEL_FILEPATH == 'none':
        model = create_model()
    else:
        model = load_model(MODEL_FILEPATH)
        print('Model Loaded.')
    return model

def save_trained_model(model, name):
    if MODEL_FILEPATH == 'int':
        model.save(name + 'vgg.model')
    else:
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
    train_generator = create_aug_generator(TRAIN_LOCATION)
    validation_generator = create_aug_generator(VALIDATION_LOCATION)
    test_generator = create_aug_generator(TEST_LOCATION)
    # # load pre-compiled model
    model = load_compiled_model()
    # # train the model
    model_trained = train_model(model, train_generator, validation_generator)
    # # save the model
    save_trained_model(model_trained, 'models/clf_trained')

    print('Execution done!')
