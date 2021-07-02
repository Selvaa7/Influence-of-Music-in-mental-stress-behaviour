import project_config as pc
from get_file_online import _get_file_web
import pprocessing
import project_tools as pt
import feature_extraction as FE
# First is to download all file from the web. Comment the line if all files has been downloaded
_get_file_web()


set_data = pc.set_data
task_run = range ( 1, 7 )
subject = range ( 1, 32 )

# Next do the  PREPROCESSING step
def pprecossing_signal():
    for sbj in subject:
        firstR=task_run[1]
        path_store_pp=f'{pc.base_folder}/preprocessing/{sbj}/'
        path_file=f'{pc.base_folder}{sbj}/run{firstR}_eeg.edf'

        pt.check_make_folder(path_store_pp)
        pprocessing.downsample(path_file,path_store_pp)
        pprocessing.create_epoch() #
        pprocessing.demix_signal_ica() # The framework is there, try to think how to make it work
        pprocessing.zeroed_bad_signal ()


# The, extract the feature
def feature_extraction():
    '''

    :return:
    '''
    FE.calculate_feature ()
