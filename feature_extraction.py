from mne_features.feature_extraction import extract_features  # try to think how to install this.
import mne


def calculate_feature ():
    clean_epoc_dir = 'zeroed_interpolated-epo.fif'
    epochs_zeroed = mne.read_epochs ( clean_epoc_dir, preload=True )
    sfreq = epochs_zeroed.info ['sfreq']  # the sampling frequency

    # selected_features = ['pow_freq_bands', 'samp_entropy']
    # see https://github.com/mne-tools/mne-features/tree/master/mne_features
    # for list of feature
    selected_features = ['pow_freq_bands']

    features = extract_features ( epochs_zeroed.get_data (), sfreq,
                                  selected_funcs=selected_features, return_as_df=True )
