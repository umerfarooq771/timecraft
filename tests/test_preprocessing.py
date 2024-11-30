import pandas as pd
from timecraft.preprocessing import Preprocessor

def test_resample_data():
    data = pd.DataFrame({'value': [1, 2, 3]}, index=pd.date_range(start='2023-01-01', periods=3, freq='D'))
    pp = Preprocessor()
    resampled = pp.resample_data(data, freq='W')
    assert len(resampled) == 1
