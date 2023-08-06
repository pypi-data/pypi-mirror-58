#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import seaborn as sns
import numpy as np

def createCorrelationBarMovie(rolled_sharpe, saving_path):
    FFMpegWriter = manimation.writers['ffmpeg']
    metadata = dict(title='Movie Test', artist='Matplotlib',
                    comment='Movie support!')
    writer = FFMpegWriter(fps=15, metadata=metadata)
    fig = plt.figure()
    ax = fig.gca()
    with writer.saving(fig, saving_path, 100):
        for row in rolled_sharpe.iterrows():
            ax.clear()
            plt.ylim(-1, 1)
            histo_values = row[1].to_frame()
            histo_values.columns = ['CORR']
            histo_values['STRAT'] = histo_values.index
            histo_values.plot.bar(x='STRAT', y='CORR', rot=90, ax = ax, title = str(row[0]), legend = None)
            writer.grab_frame()

def createCorrelationMovie(stacked_rolled_sharpe, saving_path, fillna = True):
    stacked_rolled_sharpe.index.names = ['ts', 'strat']
    FFMpegWriter = manimation.writers['ffmpeg']
    metadata = dict(title='Movie Test', artist='Matplotlib',
                    comment='Movie support!')
    writer = FFMpegWriter(fps=15, metadata=metadata)
    fig = plt.figure()
    ax = fig.gca()
    with writer.saving(fig, saving_path, 100):
        for date in stacked_rolled_sharpe.index.get_level_values('ts').unique():
            ax.clear()
            plt.ylim(-1, 1)
            plt.xlim(-1, 1)
            corr = stacked_rolled_sharpe.loc[date]
            if fillna :
                corr = corr.fillna(0.)
            sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
                        cmap=sns.diverging_palette(220, 10, as_cmap=True),
                        square=True, ax=ax)
            writer.grab_frame()
