import os
import numpy as np
from shutil import move


TRAIN_LOCATION = '/media/fury/data/Scripts/the_movies_data_scraper/datasets/The_Movies/posters/train'
TEST_LOCATION = '/media/fury/data/Scripts/the_movies_data_scraper/datasets/The_Movies/posters/test'
VALIDATION_LOCATION = '/media/fury/data/Scripts/the_movies_data_scraper/datasets/The_Movies/posters/validation'


def get_total_posters(dataset, location):
    '''Utility function to get the number of items per dataset type'''
    num_items = 0
    for item in os.listdir(location):
        num_posters = len(os.listdir(os.path.join(location, item)))
        num_items += num_posters

    print("%s: %i" % (dataset, num_items))

 
def move_images(perc, location, target_location):
    '''
    Move a certain percentage of the target dataset to a new location.
    The percentage is drawn from each genre.
    '''
    for genre in os.listdir(location):
        dir_contents = os.listdir(os.path.join(location, genre))
        dir_len = len(dir_contents)
        num_items_to_take = int(np.ceil(perc * dir_len / 100))
        # Randomize the draw with a integeres drawn from descrete uniform
        items_idx_array = np.random.choice(dir_len, num_items_to_take, replace = False)    
        
        for idx in items_idx_array:
            src = os.path.join(location, genre, dir_contents[idx])
            dst_dir = os.path.join(target_location, genre)
            if not os.path.exists(dst_dir): # make sure that the path exists
                os.makedirs(dst_dir)
            move(src, os.path.join(dst_dir, dir_contents[idx]))
            
    print('Done!') # just because

if __name__ == '__main__':
    move_images(33, TEST_LOCATION, TRAIN_LOCATION)
    get_total_posters('Train', TRAIN_LOCATION)
    get_total_posters('Test', TEST_LOCATION)