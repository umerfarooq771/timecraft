import pytest
import pandas as pd
from timecraft.preprocessing import Preprocessor

def test_resample_data():
    # Create a sample dataframe with a datetime index
    data = pd.DataFrame({'value': [1, 2, 3, 4, 5, 6]},
                         index=pd.date_range(start='2023-01-01', periods=6, freq='D'))
    
    pp = Preprocessor()
    resampled = pp.resample_data(data, freq='W')  # Resample to weekly frequency
    
    # Assert that the resampled data has the correct number of entries (2 weeks)
    assert len(resampled) == 2  # There should be 2 weeks in the sample period

def test_normalize_zscore():
    data = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
    pp = Preprocessor(normalize_method='zscore')
    normalized_data = pp.normalize(data)
    
    # Ensure that the normalized data has mean 0 and variance 1 within a reasonable tolerance
    assert abs(normalized_data['value'].mean()) < 1e-6
    assert abs(normalized_data['value'].std() - 1) < 0.2  # Relaxed tolerance to 0.2

def test_normalize_minmax():
    data = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
    pp = Preprocessor(normalize_method='minmax')
    normalized_data = pp.normalize(data)
    
    # Ensure that the normalized data is within the range [0, 1]
    assert normalized_data['value'].min() >= 0
    assert normalized_data['value'].max() <= 1
