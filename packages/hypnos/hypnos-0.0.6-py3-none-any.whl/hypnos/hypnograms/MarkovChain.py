# %%
import pandas as pd
import numpy as np
from  graphviz import Digraph
import scipy.stats
import plotly.graph_objs as go
import plotly.offline as py
import plotly.express as px
from .Hypnogram import Hypnogram

class MarkovChain:

    def __init__(self, hypgr: Hypnogram):
        self.stage = hypgr.stage
        self._probabilities = pd.DataFrame()
        
    
    def calc_probabilities(self):
        if not self._probabilities.empty: return self._probabilities
        dd = pd.DataFrame(self.stage)
        dd['next_stage'] = dd.stage.shift(-1)
        dd = dd.dropna()
        dd['trans_count'] = 0
        dd1 = dd.groupby(['stage','next_stage'], as_index =False).trans_count.count()
        dd1['prob'] = [x.trans_count/dd1.groupby(['stage']).trans_count.sum()[x.stage] for (_, x) in dd1.iterrows()]
        self._probabilities = dd1
        return self._probabilities

    def get_graph(self, title=None):
        df = self.calc_probabilities()
        G=Digraph(format='svg')
        
        G.graph_attr['fontname']=G.node_attr['fontname']=G.edge_attr['fontname']=font = 'arial'
        G.graph_attr['label']= f"{title}\n\n"
        G.graph_attr['labelloc']= 't'
        G.graph_attr['labeldistance']= '500'
        G.graph_attr['fontsize'] = '16'
        
        G.node_attr['shape']='circle'        
        G.node_attr['style']='filled'
        G.node_attr['fillcolor']='#ddddff'
        G.node_attr['fontsize'] = '10'
        
        for (_,trans) in df.iterrows():
            G.edge(trans.stage, 
                    trans.next_stage, 
                    label=str(np.round(trans.prob*100, 1))+'%', 
                    penwidth=str(np.maximum(0.1,3.0*trans.prob)), 
                    fontsize=str(8+6.0*trans.prob))

        G.node('Wake', style='filled', fillcolor='#ddffdd')
        G.node('REM', style='filled', fillcolor='#ffdddd')
        return G

    def probability_matrix(self):
        df = self.calc_probabilities()
        prob_matrix = df.pivot('stage','next_stage','prob').fillna(0.0)
        return prob_matrix

    def probability_heatmap(self):
        probs = self.probability_matrix()*100
        fig = go.Figure(data=go.Heatmap(z=probs[probs.columns[::-1]],x=probs.columns,y=probs.index[::-1], colorscale=px.colors.sequential.Emrld))
        return fig
 

# %%
