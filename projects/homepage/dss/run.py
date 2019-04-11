import os
import numpy as np
from sklearn.model_selection import train_test_split
import keras.backend as K
from keras.models import load_model
from preprocessing import preprocessing
from faphy import get_weights
from ann import ANN
from eval import eval
seed = 1
np.random.seed(seed)

# parameters
isWEIGHT = 1
WEIGHT_AGAIN = False
TRAIN_AGAIN = True
DATA_PATH = 'data/processed_data.csv'
IMP_M = 'x'
SCALE_M = 'min_max'
# PAIRWISE_PATH = ''
W_PATH = 'Z:\Github\idss_pw3\data\weights'
OUTPUT_PATH = 'Z:/Github/dss_pw3/results'+ IMP_M + '-' + SCALE_M + '-' + str(isWEIGHT) +'/'
MODEL_PATH = OUTPUT_PATH + 'ANNmodel.h5'

pred_data = '' # new data for prediction
