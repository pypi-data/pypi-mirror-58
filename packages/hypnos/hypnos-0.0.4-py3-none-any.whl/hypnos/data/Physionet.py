import pandas as pd
from datetime import datetime
import urllib.request
import mne
import tempfile
import os
import requests
import lxml.html as lh

class Physionet:

    def download_physionet_file(self, file_path, sub_dir=''):
        sub_dir = sub_dir if sub_dir=='' else sub_dir+'/'
        temp_dir = f"{tempfile.gettempdir()}\\physionet.org"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        base_url = "https://physionet.org/files/sleep-edfx/1.0.0"
        source_file = f"{base_url}/{sub_dir}{file_path}?download"
        
        out_file = f"{temp_dir}\\{file_path}"
        if not os.path.isfile(out_file):
            urllib.request.urlretrieve (source_file, out_file)
        return str(out_file)

    def get_subjects_metadata(self, useCache=True):
        f = self.download_physionet_file("SC-subjects.xls")
        df = pd.read_excel(f)
        df = df.rename(columns={"sex (F=1)":'sex'})
        subs_with_missing_data = [36, 52, 13]
        df = df[~df.subject.isin(subs_with_missing_data)].copy()

        f = self.download_physionet_file("sleep-cassette")
        
        links = lh.parse(f).xpath('//a')
        all_files = [x.text for x in links if x.text!='../']
        
        filter_func = lambda row: [x for x in all_files if x.startswith(f"SC4{row.subject:02d}{row.night}")]
        df['PSG'] = df.apply(lambda row: filter_func(row)[0], axis=1)
        df['Hypno'] = df.apply(lambda row: filter_func(row)[1], axis=1)
        
        return df

    def _get_cached_dataset(self, dataset_name):
        cache_dir = f"{tempfile.gettempdir()}\\physionet.org\\datasets"
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        cache_file = f"{cache_dir}\\{dataset_name}"

        if os.path.isfile(cache_file):
            return pd.read_parquet(cache_file), cache_file
        return pd.DataFrame(), cache_file

    def get_sc_subject(self, subject, night=1):
        cache_df,cache_file = self._get_cached_dataset(f"sc_{subject}_{night}.parquet")
        if not cache_df.empty: return cache_df

        sub_df = self.get_subjects_metadata()
        sub_df = sub_df[(sub_df.subject==subject)&(sub_df.night==night)]
        psg_file = sub_df.PSG.values[0] #f"SC40{subject}{night}E0-PSG.edf"
        psg_file = self.download_physionet_file(psg_file, sub_dir='sleep-cassette')
        hypno_file = sub_df.Hypno.values[0] #f"SC40{subject}{night}EH-Hypnogram.edf"
        hypno_file = self.download_physionet_file(hypno_file, sub_dir='sleep-cassette')
        raw_train = mne.io.read_raw_edf(psg_file, verbose=0)
        annot_train = mne.read_annotations(hypno_file)
        #sf = raw_train.info['sfreq']
        start_datetime = datetime.fromtimestamp(raw_train.info['meas_date'][0])
        
        df = pd.DataFrame(raw_train[:][0])
        df = df.transpose()
        df.columns=raw_train.info['ch_names']
        #df['time'] = raw_train[:][1]
        df['datetime'] = pd.to_timedelta(raw_train[:][1], unit='s') + start_datetime
        df = df.set_index('datetime')
        #convert EEG values from V to uV
        df['EEG Fpz-Cz'] = df['EEG Fpz-Cz']*10**6
        df['EEG Pz-Oz'] = df['EEG Pz-Oz']*10**6
        
        annotdf = pd.DataFrame()
        annotdf['Stage'] = annot_train.description
        annotdf['Stage'] = annotdf.Stage.str.replace('Sleep stage ','')
        annotdf['Stage'] = annotdf.Stage.map({'W':'Wake','1':'N1','2':'N2','3':'N3','R':'REM','?':'?'})
        annotdf['Onset'] = pd.to_timedelta(annot_train.onset, unit='s')+df.index[0]
        annotdf = annotdf.set_index('Onset')
        
        df = df.join(annotdf['Stage'],how='left')
        df.Stage = df.Stage.fillna(method='ffill')
        df.to_parquet(cache_file)
        return df