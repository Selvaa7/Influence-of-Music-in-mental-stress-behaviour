import os
import requests
import re
from pathlib import Path
from joblib import Parallel, delayed
import project_config as pc


def _download_file (url, file_path):
    r = requests.get ( url, stream=True )
    if r.ok:
        print ( "saving to", os.path.abspath ( file_path ) )
        with open ( file_path, 'wb' ) as f:
            for chunk in r.iter_content ( chunk_size=1024 * 8 ):
                if chunk:
                    f.write ( chunk )
                    f.flush ()
                    os.fsync ( f.fileno () )
    else:  # HTTP status code 4XX/5XX
        print ( "Download failed: status code {}\n{}".format ( r.status_code, r.text ) )


def download (url: str, dest_folder: str):
    filename = re.split ( r'task-', url ) [1]
    subject_id = int ( re.search ( "sub-(.*):eeg", url ) [1] )

    store_folder = f'{dest_folder}{subject_id}/'
    file_path = os.path.join ( store_folder, filename )

    if not Path ( file_path ).exists ():  # works for both file and folders

        if not os.path.exists ( store_folder ):
            os.makedirs ( store_folder )  # create folder if it does not exist

        _download_file ( url, file_path )


def _get_file_web():
    set_data = pc.set_data
    task_run = range ( 1, 7 )
    subject = range ( 1, 32 )


    all_url = []
    for sub in subject:
        all_task_sub = []

        for task in task_run:
            channels = f'{pc.base_url}{sub:02d}:eeg:sub-{sub:02d}_task-run{task:d}_{set_data ["channels"]}'
            eeg_edf = f'{pc.base_url}{sub:02d}:eeg:sub-{sub:02d}_task-run{task:d}_{set_data ["eeg_edf"]}'
            eeg_json = f'{pc.base_url}{sub:02d}:eeg:sub-{sub:02d}_task-run{task:d}_{set_data ["eeg_json"]}'
            events_json = f'{pc.base_url}{sub:02d}:eeg:sub-{sub:02d}_task-run{task:d}_{set_data ["events_json"]}'
            event_tsv = f'{pc.base_url}{sub:02d}:eeg:sub-{sub:02d}_task-run{task:d}_{set_data ["event_tsv"]}'
            all_task_sub.append ( [channels, eeg_edf, eeg_json, events_json, event_tsv] )
        all_url.append ( all_task_sub )
    _download (all_url)




def _download(all_url):
    url_ls = [item for sublist in [item for sublist in all_url for item in sublist] for item in sublist]
    njob = 3

    if njob == 1:
        [download ( x_url, dest_folder=pc.base_folder ) for x_url in url_ls]

    else:
        Parallel ( n_jobs=2 ) ( delayed ( download ) ( x_url, dest_folder=pc.base_folder)
                                for x_url in url_ls )
