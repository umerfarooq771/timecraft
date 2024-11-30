import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

class FeatureGenerator:
    def __init__(self, pca_components=None):
        """
        Initializes the feature generator.

        Args:
            pca_components (int, optional): Number of principal components to generate.
        """
        self.pca_components = pca_components

    def create_statistical_features(self, df, window_size):
        """
        Generate rolling statistical features.

        Args:
            df (pd.DataFrame): Input time series data.
            window_size (int): Rolling window size for statistical calculations.

        Returns:
            pd.DataFrame: Dataframe with statistical features.
        """
        stats = pd.DataFrame()
        stats['mean'] = df.rolling(window=window_size).mean()
        stats['std'] = df.rolling(window=window_size).std()
        stats['min'] = df.rolling(window=window_size).min()
        stats['max'] = df.rolling(window=window_size).max()
        stats['skew'] = df.rolling(window=window_size).skew()
        stats['kurt'] = df.rolling(window=window_size).kurt()
        return stats

    def create_time_features(self, df):
        """
        Create time-based features such as day of the week, month, etc.

        Args:
            df (pd.DataFrame): Input dataframe with a datetime index.

        Returns:
            pd.DataFrame: Dataframe with time-based features.
        """
        time_features = pd.DataFrame(index=df.index)
        time_features['day_of_week'] = df.index.dayofweek
        time_features['month'] = df.index.month
        time_features['day_of_year'] = df.index.dayofyear
        time_features['quarter'] = df.index.quarter
        return time_features

    def apply_pca(self, df):
        """
        Apply PCA to reduce dimensionality of features.

        Args:
            df (pd.DataFrame): Input dataframe.

        Returns:
            pd.DataFrame: Dataframe with PCA-transformed features.
        """
        if self.pca_components is None:
            raise ValueError("pca_components must be specified to apply PCA.")
        pca = PCA(n_components=self.pca_components)
        pca_features = pca.fit_transform(df)
        return pd.DataFrame(pca_features, index=df.index)
    