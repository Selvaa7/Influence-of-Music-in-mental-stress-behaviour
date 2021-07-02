import mne
import project_config as pc
from mne.preprocessing import ICA, create_ecg_epochs, create_eog_epochs
from mne.report import Report


def downsample (path_file, path_store_pp):
    raw = mne.io.read_raw_edf ( path_file, preload=True )

    # # Downsample to 200 Hz # https://mne.tools/dev/auto_tutorials/preprocessing/plot_30_filtering_resampling
    # .html#sphx-glr-auto-tutorials-preprocessing-plot-30-filtering-resampling-py
    raw.resample ( pc.resamp_val, npad="auto" )

    raw_band_pass = raw.copy ().filter (
        pc.bandpass_fmin, pc.bandpass_fmax, l_trans_bandwidth='auto',
        h_trans_bandwidth='auto', filter_length='auto', phase='zero',
        fir_window='hamming', fir_design='firwin' )

    raw_band_pass.save ( f"{path_store_pp}raw_filtered.fif", overwrite=True )


def create_epoch ():
    '''

    Make epoch from the event
    :return:
    '''


def demix_signal_ica (filename, path_store_pp):
    n_components = 19  # since we have 19 ch
    epochs = mne.read_epochs ( path_store_pp + 'PLEASE CHANGE TO THE SET ICA NAME', preload=True )

    ica = ICA ( method='infomax', random_state=42, n_components=n_components ). \
        fit ( epochs )

    ica.save ( f"{path_store_pp}MAKE_UR_OWN_NAME.fif" )

    fig = ica.plot_components ( title='Full ICA', show=False )  # attach this to the report:rpb
    comments = ['IC_' + str ( i ) for i in fig]
    captions = ['IC_' + str ( i ) for i in list ( range ( 0, len ( fig ) ) )]

    '''
    Refer topoplot to get which IC is artifact-related
    Refer this link to understand how to distinguish bad good IC
    https://labeling.ucsd.edu/tutorial/labels
    '''
    rep = Report ()
    rep.add_figs_to_section ( fig, captions=captions, section='Pre_ica' )
    rep.save ( f"{path_store_pp}MAKE_OWN_NAME.html", overwrite=True, open_browser=False )


def zeroed_bad_signal (path_store_pp):
    ica = mne.preprocessing.read_ica ( path_store_pp + 'fit_ica.fif', verbose=None )
    epochs = mne.read_epochs ( path_store_pp + 'raw-epo.fif', preload=True )

    ica.exclude = []  # try to think how extract the selected bad IC automatically
    ica.apply ( epochs )

    # save the clean signal with name 'zeroed-epo.fif'
    epochs.save ( f'{path_store_pp}zeroed-epo.fif', overwrite=True )
