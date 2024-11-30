# timecraft/feature_generation.py

import pandas as pd

class FeatureGenerator:
    def __init__(self):
        pass

    def generate_features(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Generate additional features based on the input data.

        Args:
            data (pd.DataFrame): The input dataframe with at least one column to generate features.

        Returns:
            pd.DataFrame: The dataframe with additional features added.
        """
        # Example feature: Calculate the rolling mean (e.g., 2-period rolling mean)
        if 'value' in data.columns:
            data['rolling_mean'] = data['value'].rolling(window=2).mean()

        # Example feature: Extract month and year from a datetime index
        if isinstance(data.index, pd.DatetimeIndex):
            data['year'] = data.index.year
            data['month'] = data.index.month

        # Example feature: Lagged values (previous day's value)
        data['lagged_value'] = data['value'].shift(1)

        # Add more features as needed, e.g., seasonal indicators, aggregations, etc.

        return data
