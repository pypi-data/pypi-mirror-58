#!/usr/bin/env python
# coding: utf-8

from abc import ABC, abstractmethod
from napoleontoolbox.features import features_type
import sys

import pandas as pd

import numpy as np

import torch


class AbstractAssembler(ABC):
    def __init__(self, features_path, returns_path, root='../data/', user = 'napoleon', features_saving_path = '_features.npy', features_names_saving_path = '_features_names.npy'):
        super().__init__()
        self.root =  root
        self.user =  user
        self.features_path = features_path
        self.returns_path = returns_path
        self.features_saving_path = features_saving_path
        self.features_names_saving_path = features_names_saving_path


    @abstractmethod
    def assembleFeature(self, feature_type, n_past_features):
        pass


class FeaturesAssembler(AbstractAssembler):
    def reassembleAdvancedFeaturesForClusterization(self, normalize = True, stationarize = True, clustering_size = 21, simple = False, features_extraction = True):
        df = pd.read_pickle(self.root + self.returns_path)

        df['Date'] = pd.to_datetime(df['Date'])
        df = df.set_index('Date')
        strats = [col for col in list(df.columns) if col != 'Date']

        df = df.fillna(method='ffill')

        advanced_features = pd.read_pickle(self.root + self.features_path)
        features_names = [col for col in list(advanced_features.columns) if col!='Date']


        advanced_features['Date'] = pd.to_datetime(advanced_features['Date'])

        # quotes_df=quotes_df.sort_values(by='date', ascending=True)
        # quotes_df.head()

        print(df.columns)
        print(df.shape)

        print(advanced_features.columns)
        print(advanced_features.shape)

        # Computationnal period (default 1 year)

        np.random.seed(0)
        torch.manual_seed(0)

        ##===================##
        ##  Setting targets  ##
        ##===================##

        #
        df_bis = df.copy()
        # df_ret = df_bis.pct_change().fillna(0.)
        # ret = df_ret.values

        print('merging')
        df_bis = pd.merge(df_bis, advanced_features, how='left', on=['Date'])

        print('merging done')
        df_bis.index = df_bis['Date']
        df_bis = df_bis.drop(columns=['Date'])
        print('return')

        df_bis = df_bis.fillna(method='ffill').fillna(method='bfill')
        df_ret = df_bis.copy()

        print('computing returns')
        for col in strats:
            print(col + str(len(df_bis.columns)))
            df_ret[col] = df_bis[col].pct_change().fillna(0.)

        if stationarize:
            print('stationarizing features')
            for col in features_names:
                print(col + str(len(df_bis.columns)))
                df_ret[col] = df_bis[col].pct_change().replace([np.inf, -np.inf], np.nan).fillna(0.)

        if normalize:
            print('normalizing features') # careful : forward looking bias
            for col in features_names:
                print(col + str(len(df_bis.columns)))
                df_ret[col] = (df_ret[col] - df_ret[col].mean()) / df_ret[col].std(ddof=0)

        print('number of infs in advanced features')
        print(np.isinf(df_ret[features_names]).sum(axis=0))

        print('number of infs in returns')
        print(np.isinf(df_ret[strats]).sum(axis=0))

        print('number of nans in advanced features')
        print(np.isnan(df_ret[features_names]).sum(axis=0))

        print('number of nans in returns')
        print(np.isnan(df_ret[strats]).sum(axis=0))

        if simple:
            return strats, features_names, df_ret

        ret_df = df_ret[strats]
        ret = ret_df.values

        feat = df_ret[features_names].values

        T = df.index.size
        N = df.columns.size

        if features_extraction:
            features = np.zeros([T, 6*len(features_names)], np.float32)
        else:
            features = np.zeros([T, clustering_size, len(features_names)], np.float32)


        # for t in range(max(n_past_features, s), T - s):
        for t in range(clustering_size, T):
            np.random.seed(0)
            torch.manual_seed(0)
            # the output to predict cannot be computed in the future
            # we still assemble the predictors
            # Set input data
            t_n = min(max(t - clustering_size, 0), T)
            F = feat[t_n: t, :]
            X_back = ret[t_n: t, :]

            if features_extraction:
                F_mean = np.mean(F, axis=0)
                F_quant_zero = np.quantile(F, 0., axis=0)
                F_quant_twenty_five = np.quantile(F, 0.25, axis=0)
                F_quant_fifty = np.quantile(F, 0.5, axis=0)
                F_quant_seventy_five = np.quantile(F, 0.75, axis=0)
                F_quant_hundred = np.quantile(F, 1., axis=0)
                features[t: t + 1] = np.concatenate(
                    (F_mean, F_quant_zero, F_quant_twenty_five, F_quant_fifty, F_quant_seventy_five, F_quant_hundred),
                    axis=0)
            else:
                features[t: t + 1] = F

            if t % 500 == 0:
                print('{:.2%}'.format(t / T))
            # we compute the utility output to predict only if not in future

        print('saved files')
        print('number of nan/infinity features')
        print(np.isnan(features).sum(axis=0).sum())
        print(np.isinf(features).sum(axis=0).sum())
        if np.isnan(features).sum(axis=0).sum() > 0:
            raise Exception('nan values for assembled features')
        if np.isinf(features).sum(axis=0).sum() > 0:
            raise Exception('inf values for assembled features')
        return strats, features_names, features


    def assembleFeature(self, feature_type, n_past_features):
        print('feature_type' + str(feature_type))
        print('n_past_features' + str(n_past_features))

        df = pd.read_pickle(self.root + self.returns_path)

        df['Date'] = pd.to_datetime(df['Date'])
        df = df.set_index('Date')
        strats = [col for col in list(df.columns) if col != 'Date']

        corr_strats = [col1+'_'+col2 for col1 in strats for col2 in strats]
        df = df.fillna(method='ffill')
        T = df.index.size

        advanced_features = pd.read_pickle(self.root + self.features_path)
        features_names = [col for col in list(advanced_features.columns) if col!='Date']
        predictor_names = None


        advanced_features['Date'] = pd.to_datetime(advanced_features['Date'])

        # quotes_df=quotes_df.sort_values(by='date', ascending=True)
        # quotes_df.head()

        print(df.columns)
        print(df.shape)

        print(advanced_features.columns)
        print(advanced_features.shape)

        # Computationnal period (default 1 year)

        np.random.seed(0)
        torch.manual_seed(0)

        ##===================##
        ##  Setting targets  ##
        ##===================##

        #
        df_bis = df.copy()
        # df_ret = df_bis.pct_change().fillna(0.)
        # ret = df_ret.values

        print('merging')
        df_bis = pd.merge(df_bis, advanced_features, how='left', on=['Date'])

        print('merging done')
        df_bis.index = df_bis['Date']
        df_bis = df_bis.drop(columns=['Date'])
        print('return')

        df_bis = df_bis.fillna(method='ffill').fillna(method='bfill')
        df_ret = df_bis.copy()

        print('computing returns')
        for col in strats:
            print(col + str(len(df_bis.columns)))
            df_ret[col] = df_bis[col].pct_change().fillna(0.)

        if feature_type is features_type.FeaturesType.STANDARD_STATIONARIZED:
            print('stationarizing features')
            for col in features_names:
                print(col + str(len(df_bis.columns)))
                df_ret[col] = df_bis[col].pct_change().replace([np.inf, -np.inf], np.nan).fillna(0.)

        if feature_type is features_type.FeaturesType.STANDARD_STATIONARIZED_NORMALIZED:
            print('normalizing features') # careful : forward looking bias
            for col in features_names:
                print(col + str(len(df_bis.columns)))
                df_ret[col] = (df_ret[col] - df_ret[col].mean()) / df_ret[col].std(ddof=0)

        print('number of infs in advanced features')
        print(np.isinf(df_ret[features_names]).sum(axis=0))

        print('number of infs in returns')
        print(np.isinf(df_ret[strats]).sum(axis=0))

        print('number of nans in advanced features')
        print(np.isnan(df_ret[features_names]).sum(axis=0))

        print('number of nans in returns')
        print(np.isnan(df_ret[strats]).sum(axis=0))


        ret_df = df_ret[strats]
        ret = ret_df.values

        feat = df_ret[features_names].values

        T = df.index.size
        N = df.columns.size


        if feature_type is features_type.FeaturesType.RAW_ADVANCED:
            features = np.zeros([T, n_past_features, N + len(features_names)], np.float32)
        if feature_type is features_type.FeaturesType.RAW:
            features = np.zeros([T, n_past_features, N], np.float32)

        if feature_type is features_type.FeaturesType.STANDARD or feature_type is features_type.FeaturesType.STANDARD_STATIONARIZED or feature_type is features_type.FeaturesType.STANDARD_STATIONARIZED_NORMALIZED:
            features = np.zeros([T, N + N * N + len(features_names)], np.float32)
            predictor_names = strats + corr_strats + features_names

        if feature_type is features_type.FeaturesType.NONE:
            features = np.zeros([T, N + N * N], np.float32)
            predictor_names = strats + corr_strats


        for t in range(n_past_features, T):
            np.random.seed(0)
            torch.manual_seed(0)
            # the output to predict cannot be computed in the future
            # we still assemble the predictors
            # Set input data
            t_n = min(max(t - n_past_features, 0), T)
            F = feat[t_n: t, :]
            X_back = ret[t_n: t, :]

            if feature_type is features_type.FeaturesType.RAW_ADVANCED or feature_type is features_type.FeaturesType.RAW:
                if feature_type is features_type.FeaturesType.RAW_ADVANCED:
                    X_back = np.concatenate((X_back, F), axis=1)
                features[t: t + 1] = X_back
            elif (feature_type is features_type.FeaturesType.STANDARD or feature_type is features_type.FeaturesType.STANDARD_STATIONARIZED or feature_type is features_type.FeaturesType.STANDARD_STATIONARIZED_NORMALIZED):
                F_mean = np.nanmean(F, axis=0)
                std = np.std(X_back, axis=0).reshape([N, 1])
                mean = np.mean(X_back, axis=0)
                mat_std = std @ std.T
                mat_std[mat_std == 0.] = 1.
                mat_corr = np.cov(X_back, rowvar=False) / mat_std

                if (feature_type is features_type.FeaturesType.STANDARD or feature_type is features_type.FeaturesType.STANDARD_STATIONARIZED or feature_type is features_type.FeaturesType.STANDARD_STATIONARIZED_NORMALIZED):
                    features[t: t + 1] = np.transpose(
                        np.concatenate((mean, mat_corr.flatten(), F_mean), axis=0))
                if (feature_type is features_type.FeaturesType.NONE):
                    features[t: t + 1] = np.transpose(
                        np.concatenate((mean, mat_corr.flatten()), axis=0))

            if t % 500 == 0:
                print('{:.2%}'.format(t / T))
            # we compute the utility output to predict only if not in future

        print('saved files')
        print('number of nan/infinity features')
        print(np.isnan(features).sum(axis=0).sum())
        print(np.isinf(features).sum(axis=0).sum())
        if np.isnan(features).sum(axis=0).sum() > 0:
            raise Exception('nan values for assembled features')
        if np.isinf(features).sum(axis=0).sum() > 0:
            raise Exception('inf values for assembled features')

        print('saving file')
        features_saving_path = self.root  + self.user + '_' + feature_type.name + '_' + str(n_past_features) + self.features_saving_path
        print(features_saving_path)
        np.save(features_saving_path, features)

        features_names_saving_path = self.root  + self.user + '_' + feature_type.name + '_' + str(n_past_features) + self.features_names_saving_path
        print(features_names_saving_path)
        np.save(features_names_saving_path, predictor_names)







