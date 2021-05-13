# ------ Python standard library imports ---------------------------------------
from typing import Optional
import os
# ------ External imports ------------------------------------------------------
# ------ Imports from own package or module ------------------------------------
from movieverse.movieverse import Movieverse
from movieverse.metadatalib import MetaDataLib
#-------------------------------------------------------------------------------

def _dataset_directory():

    fallback = os.path.join(os.path.expanduser("~"), ".movieverse_data")
    dir_ = os.environ.get("MOVIEVERSE_DATASET_DIR", fallback)

    if not os.path.exists(dir_):
        os.makedirs(dir_)

    return dir_

def load_movielens(dataset: str = '100k',
                   movieverse_name: Optional[str] = None,
                   directory: str = '') -> Movieverse:

    path = directory or _dataset_directory()

    if dataset == '100k':

        url = 'http://files.grouplens.org/datasets/movielens/ml-100k.zip'
        
