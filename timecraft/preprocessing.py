# timecraft/preprocessing.py

from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

class Preprocessor:
    def __init__(self, normalize_method='zscore'):
        """
        Initialize the preprocessor with the desired normalization method.

        Args:
            normalize_method (str): Normalization method, 'zscore' (standardization) or 'minmax' (scaling to [0, 1]).
        """
        self.normalize_method = normalize_method
        self.scaler = None

    def resample_data(self, data: pd.DataFrame, freq: str) -> pd.DataFrame:
        """
        Resample the data to the specified frequency and generate additional features.

        Args:
            data (pd.DataFrame): The input data to be resampled.
            freq (str): The frequency to resample the data (e.g., 'D' for daily, 'W' for weekly).

        Returns:
            pd.DataFrame: The resampled dataframe with generated features (e.g., rolling mean).
        """
        # Resample the data using the specified frequency (mean as default aggregation)
        resampled = data.resample(freq).mean()

        # Add feature generation, e.g., rolling mean
        if 'value' in resampled.columns:
            resampled['rolling_mean'] = resampled['value'].rolling(window=2).mean()

        # Add any other feature generation logic as needed here
        # e.g., resampled['new_feature'] = ...

        return resampled

    def normalize(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Normalize the dataframe using the specified normalization method.

        Args:
            df (pd.DataFrame): The input dataframe to normalize.

        Returns:
            pd.DataFrame: The normalized dataframe.
        """
        if self.normalize_method == 'zscore':
            self.scaler = StandardScaler()
        elif self.normalize_method == 'minmax':
            self.scaler = MinMaxScaler()
        else:
            raise ValueError("normalize_method must be 'zscore' or 'minmax'.")

        # Fit and transform the data using the selected scaler
        scaled_data = self.scaler.fit_transform(df)
        
        # Return the normalized data with the same structure as the input
        return pd.DataFrame(scaled_data, index=df.index, columns=df.columns)
