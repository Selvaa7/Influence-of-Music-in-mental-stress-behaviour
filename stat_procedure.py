
import pickle
import pandas as pd
from bioinfokit.analys import stat

# get ANOVA table as R like output
import statsmodels.api as sm
from statsmodels.formula.api import ols


def statistic_anova():
    nfolder =  '/stat'

    df_main = pickle.load ( open ( f'{nfolder}/df_stat_anova.pickle', "rb" ) )
    df=df_main.loc [:, (['pow_freq_bands', 'window'], ['ch0_band4', ''])]
    df.columns = df.columns.to_flat_index ().str.join ( '_' )





statistic_anova()