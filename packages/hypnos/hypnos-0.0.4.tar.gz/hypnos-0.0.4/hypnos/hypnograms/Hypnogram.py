import pandas as pd
import numpy as np
import matplotlib
from  graphviz import Digraph 
import scipy.stats
import plotly.graph_objs as go
import plotly.offline as py
import plotly.express as px
from datetime import datetime

class Hypnogram:

    def __init__(self):
        self.stage = pd.Series

    @staticmethod
    def from_dataframe(df:pd.DataFrame, column_name="stage", output_epoch_sec=30, combine_stages=None):
        if type(df.index) != pd.DatetimeIndex:
            raise Exception(f"DataFrame index should be of the type DatetimeIndex.")
        if column_name not in df.columns:
            raise Exception(f"Column '{column_name}' not found in the DataFrame.")
        dd = df[column_name].copy().rename("stage")
        if combine_stages:
           for key in combine_stages:
               dd.replace(combine_stages[key], key, inplace=True)
        hypno = Hypnogram()
        hypno.stage = dd.groupby(pd.Grouper(freq=f"{output_epoch_sec}s")).agg(pd.Series.mode).astype(str)
        return hypno
    
    def get_stages(self, sleep_only=False, to_hrs_of_sleep=False):
        sleep_start = self.stage[self.stage!='Wake'].index[0]
        sleep_end = self.stage[self.stage!='Wake'].index[-1]
        if not to_hrs_of_sleep:
            return self.stage[sleep_start : sleep_end] if sleep_only else self.stage
        else:
            ret = self.stage[sleep_start : sleep_end].copy() if sleep_only else self.stage.copy()
            ret.index = [datetime.min + (x-sleep_start) for x in ret.index]
            return ret
    
    def plot(self, title="", sleep_only=False, to_hrs_of_sleep=False, datetime_format='%H:%M', width=None, height=None):
        stage_data = self.get_stages(sleep_only, to_hrs_of_sleep)
        if 'NREM' in stage_data.values:
            ord_stages = ['NREM','REM','Wake']
        else:
            ord_stages = ['N3','N2','N1','REM','Wake']
        if 'N4' in stage_data.values:
            ord_stages = ['N4'] + ord

        fig = go.Figure(go.Scatter(
            line= {'shape': 'hvh'}, 
            x=stage_data.index, 
            y=stage_data))
        fig.update_layout(
            width = width,
            height = height,
            title = {'text':title, 'x':0.5, 'xanchor':'center', 'yanchor':'top'},
            xaxis_tickformat = datetime_format,
            xaxis_title = "hour of sleep" if to_hrs_of_sleep else "clock hour",
            yaxis = {'type': 'category', 'categoryarray': ord_stages},
            yaxis_title = "Stage")
        return fig