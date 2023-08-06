import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from scipy.signal import welch
from scipy.integrate import simps
import numpy as np
import datetime
from joblib import Parallel, delayed

class BandPowerWelch(BaseEstimator, TransformerMixin):
    
    def __init__(self, 
        output_epoch_sec:int = 4, 
        welch_window_len_sec:int = 1,
        sampling_frequency: int=100, 
        freq_band_list:list=[(0,50)],
        n_jobs=1):

        self.output_epoch_sec = output_epoch_sec
        self.sampling_frequency = sampling_frequency
        self.freq_band_list = freq_band_list
        self.welch_window_len_sec = welch_window_len_sec
        self.n_jobs = n_jobs
        self.out_df = pd.DataFrame()
        
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        cols_bands = [(col, band) for col in X.columns for band in self.freq_band_list]
        ret = Parallel(n_jobs=self.n_jobs)(delayed(lambda col, band: self._transform_column_range(X[col], col, band))(col_band[0], col_band[1]) for col_band in cols_bands)
        
        self.out_df = ret[0]
        if len(ret)>1:
            self.out_df = self.out_df.join(ret[1:])
        return self.out_df

    def _transform_column_range(self, X, col_name, band_range):
        df_out = pd.DataFrame()
        freq_ms = 1000/self.sampling_frequency
        time_idx = pd.date_range(start=datetime.MINYEAR, freq=f'{freq_ms}ms', periods=len(X))
        df_temp = pd.DataFrame(list(X), columns=['EEG'], index=time_idx)

        groupped = df_temp.groupby(pd.Grouper(freq=f'{self.output_epoch_sec}s'))
        df_out[f'{col_name}_band_power_{band_range[0]}-{band_range[1]}Hz'] = groupped.EEG \
                                    .apply(lambda grp: bandpower_welch(
                                        grp, 
                                        self.sampling_frequency, 
                                        band_range, 
                                        self.welch_window_len_sec))
        return df_out

    def get_feature_names(self):
        return self.out_df.columns.values


def bandpower_welch(data, sampling_frequency, band, window_sec):
    # Compute the modified periodogram (Welch)
    freqs, psd = welch(data, sampling_frequency, nperseg=window_sec * sampling_frequency)
    # Frequency resolution
    freq_res = freqs[1] - freqs[0]
    # Find index of band in frequency vector
    idx_band = np.logical_and(freqs >= band[0], freqs < band[1])
    # Integral approximation of the spectrum using parabola (Simpson's rule)
    #bp = simps(psd[idx_band], dx=freq_res)
    # Integration using rectangle rule
    #bp = np.sum(psd[idx_band]*freq_res)
    # Integration using trapezoid rule
    psd2 = psd*idx_band
    est = [0.5*(psd2[i]+psd[i+1])*freq_res for i in range(len(psd2)-2)]
    bp = np.sum(est)
    return bp

