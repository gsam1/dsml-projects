import os
import numpy as np
import pandas as pd
import h5py
import scipy
import scipy.io
import scipy.ndimage
import matplotlib.pyplot as plt
import multiprocessing
from tqdm import tqdm
from ovreport.report import report_to_overwatch

def calc_sigma(distances, index):
    '''
        Calculates sigma for the density map
    '''
    return (distances[index][1]+distances[index][2]+distances[index][3])*0.1

def get_kn(points_coordinates):
    # build kdtree
    tree = scipy.spatial.KDTree(points_coordinates.copy(), leafsize=2048)
    # query kdtree
    distances, _ = tree.query(points_coordinates, k=4)

    return distances



def gen_kn_density(image, points):
    '''
        Takes as an input the image as a numpy array and the annotation points.
        Returns the density map.
    '''
    image_h = image.shape[0]
    image_w = image.shape[1]

    # coordinate of heads in the image
    points_coordinates = points
    # quantity of heads in the image
    points_quantity = len(points_coordinates)

    # generate ground truth density map
    densitymap = np.zeros((image_h, image_w))
    if points_quantity == 0:
        return densitymap
    else:

        distances = get_kn(points_coordinates)
        for i, pt in enumerate(points_coordinates):
            pt2d = np.zeros((image_h,image_w), dtype=np.float32)
            if int(pt[1]) < image_h and int(pt[0]) < image_w:
                pt2d[int(pt[1]), int(pt[0])] = 1.
            
            sigma = calc_sigma(distances, i)
            densitymap += scipy.ndimage.filters.gaussian_filter(pt2d, sigma, mode='constant')

        return densitymap

def handle_mat_file(filepath, write_loc, id):
    '''
        Takes the location of the math file and creates a sample h5 file.
    '''
    mat_loaded = scipy.io.loadmat(filepath)
    ann_points = mat_loaded['annPoints']
    
    image_filepath = filepath.split('_a')[0]
    image_name = image_filepath.split('/')[-1]
    
    image_format_name = image_filepath + '.jpg'
    image_array = plt.imread(image_format_name)
    
    density = gen_kn_density(image_array, ann_points)
    count = mat_loaded['annPoints'].shape[0]
    
    # write to disk
    hf = h5py.File(f'{write_loc + image_name}.h5', 'w')
    hf.create_dataset('image_name', data=image_name)
    hf.create_dataset('image_array', data=image_array)
    hf.create_dataset('density_map', data=density)
    hf.create_dataset('count', data=count)
    hf.close()

def process_batch(batch, num_procs=4):
    '''
        Gets the density/count vector by reading the .mat file 
        and getting the shape of the file. 
        The function only requires the path to the dataset.
    '''
    # get only the split_0 csv
    write_location = 'training_dataset/UCF-QNRF_ECCV18/Train_h5/'
    print(f'Number of processors {num_procs}')
    
    only_mat_files = list(batch['path'].values)
    
    jobs = []
    for i in range(0, num_procs):
        mat = only_mat_files[i]
        process = multiprocessing.Process(target=handle_mat_file,
                                         args=(mat, write_location, i))
        
        jobs.append(process)
    
    for j in jobs:
        j.start()
    
    for j in jobs:
        j.join()
        
    # batched n:n + num_procs proccessed
    items_processed = list(batch['id'])
    return items_processed

def image_processor(df_location, batch_size=4, n_items_processed=None, new=True, prev_count=100):
    '''
        Sends in a predefined batch of images and generates a predefined .h5 file
    '''
    split_0_df = pd.read_csv(df_location)
    # split_0_df.columns = ['id', 'path', 'df_split_id', 'processed']
    
    # Check if the split_df has been processed before
    if new:
        # since it is new split augument the dataset appropriatly
        split_0_df['processed'] = False
        split_0_df.columns = ['id', 'path', 'df_split_id', 'processed']
    else:
        split_0_df = split_0_df[split_0_df['processed'] == False].copy()
    
    if n_items_processed is None or n_items_processed > split_0_df.shape[0]:
        n_items_processed = split_0_df.shape[0]
    
    split_0_df_bcp = split_0_df.copy()
    print('Processing Data...')
    for i in tqdm(range(0, n_items_processed, batch_size)):
        end = i + batch_size
        
        if (i + batch_size) > n_items_processed:
            end = n_items_processed
        
        tmp_df = split_0_df[i:end].copy()
        num_procs = batch_size
        
        if num_procs > 16:
            raise Exception('Really?') # num proccesors of the local machine exceeded.
        
        if tmp_df.shape[0] < batch_size:
            num_procs = tmp_df.shape[0]
            
        
        # send the batch in
        items_processed = process_batch(tmp_df, num_procs)
        
#         split_0_df_bcp.loc[items_processed, 'processed'] = True
        
    
    # save the state of the batches in the df
#     count_processed = split_0_df_bcp[split_0_df_bcp['processed']].shape[0]
#     split_0_df_bcp.to_csv(f'training_dataset/split_2_proc_{count_processed}.csv', index=False)
    
    print('Complete!')
    report_to_overwatch('VM:DP:P', 'Atlas', f'{n_items_processed} densities created!')


if __name__ == '__main__':
    image_processor('training_dataset/split_1.csv', batch_size=12, n_items_processed=300, new=True, prev_count=0)