import pandas as pd
from timecraft.feature_generation import FeatureGenerator

def test_create_statistical_features():
    data = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
    fg = FeatureGenerator()
    stats = fg.create_statistical_features(data, window_size=2)
    assert 'mean' in stats.columns
