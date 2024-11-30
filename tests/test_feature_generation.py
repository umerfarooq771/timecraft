# timecraft/tests/test_feature_generation.py

import pytest
import pandas as pd
from timecraft.feature_generation import FeatureGenerator

def test_generate_features():
    data = pd.DataFrame({
        'value': [1, 2, 3, 4, 5, 6],
        'index': pd.date_range(start='2023-01-01', periods=6, freq='D')
    })
    data.set_index('index', inplace=True)

    fg = FeatureGenerator()
    features = fg.generate_features(data)

    # Test if the 'rolling_mean' column was added
    assert 'rolling_mean' in features.columns
    # Test if the 'lagged_value' column was added
    assert 'lagged_value' in features.columns
