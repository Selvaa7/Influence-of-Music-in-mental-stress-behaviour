import os


def check_make_folder (store_folder):
    if not os.path.exists ( store_folder ):
        os.makedirs ( store_folder )  # create folder if it does not exist
