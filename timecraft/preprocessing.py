from sklearn.preprocessing import StandardScaler, MinMaxScaler

class Preprocessor:
    def __init__(self, normalize_method='zscore'):
        """
        Initialize the preprocessor.

        Args:
            normalize_method (str): Normalization method, 'zscore' or 'minmax'.
        """
        self.normalize_method = normalize_method
        self.scaler = None

    def resample_data(self, df, freq):
        """
        Resample time series data to a specified frequency.

        Args:
            df (pd.DataFrame): Input time series data.
            freq (str): Resampling frequency (e.g., 'D', 'W', 'M').

        Returns:
            pd.DataFrame: Resampled dataframe.
        """
        return df.resample(freq).mean()

    def normalize(self, df):
        """
        Normalize the data using the specified method.

        Args:
            df (pd.DataFrame): Input dataframe.

        Returns:
            pd.DataFrame: Normalized dataframe.
        """
        if self.normalize_method == 'zscore':
            self.scaler = StandardScaler()
        elif self.normalize_method == 'minmax':
            self.scaler = MinMaxScaler()
        else:
            raise ValueError("normalize_method must be 'zscore' or 'minmax'.")

        scaled_data = self.scaler.fit_transform(df)
        return pd.DataFrame(scaled_data, index=df.index, columns=df.columns)
