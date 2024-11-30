import pytest
import pandas as pd
from timecraft.model import Model
from sklearn.model_selection import train_test_split

def test_train_and_evaluate():
    # Create sample data
    data = pd.DataFrame({'feature1': [1, 2, 3, 4, 5, 6],
                         'feature2': [1, 2, 3, 4, 5, 6],
                         'target': [1, 2, 3, 4, 5, 6]})
    
    X = data[['feature1', 'feature2']]
    y = data['target']
    
    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    
    # Initialize model and train
    model = Model()
    model.train(X_train, y_train)
    
    # Evaluate model
    mse = model.evaluate(X_test, y_test)
    
    assert mse >= 0  # MSE should always be non-negative
