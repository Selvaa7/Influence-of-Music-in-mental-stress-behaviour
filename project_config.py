import os
resamp_val=200
bandpass_fmin=1
bandpass_fmax=50
set_data = dict ( channels='channels.tsv',
                  eeg_edf='eeg.edf',
                  eeg_json='eeg.json',
                  events_json='events.json',
                  event_tsv='events.tsv' )

# link to download all experiment file
base_url = 'https://openneuro.org/crn/datasets/ds002721/snapshots/1.0.1/files/sub-'

myhost = os.name()

if myhost == 'rpb':
    base_folder = '/mnt/d/data_set/music_eeg/'
elif myhost == 'cisir2':
    base_folder = '/home/cisir2/Documents/rpb/music_eeg/'
elif myhost=='sel':
    base_folder = 'CHANGE TO WHERE YOU WANTED TO SAVE YOUR FILE'
else:
    raise ValueError ('please add new path for your new pc: CHANGE TO WHERE YOU WANTED TO SAVE YOUR FILE. The file is located at project_config')
