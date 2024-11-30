import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class Model:
    def __init__(self, model=None):
        """
        Initialize the model. If no model is provided, a default Linear Regression model will be used.

        Args:
            model (sklearn model, optional): A scikit-learn model to use for training and prediction.
        """
        if model is None:
            self.model = LinearRegression()
        else:
            self.model = model

    def train(self, X: pd.DataFrame, y: pd.Series) -> None:
        """
        Train the model on the provided features and target.

        Args:
            X (pd.DataFrame): The feature matrix.
            y (pd.Series): The target vector.
        """
        self.model.fit(X, y)

    def predict(self, X: pd.DataFrame) -> pd.Series:
        """
        Predict the target for the provided features.

        Args:
            X (pd.DataFrame): The feature matrix.

        Returns:
            pd.Series: The predicted target values.
        """
        return self.model.predict(X)

    def evaluate(self, X: pd.DataFrame, y: pd.Series) -> float:
        """
        Evaluate the model on the provided test set using Mean Squared Error.

        Args:
            X (pd.DataFrame): The feature matrix.
            y (pd.Series): The true target values.

        Returns:
            float: The Mean Squared Error of the model.
        """
        y_pred = self.predict(X)
        mse = mean_squared_error(y, y_pred)
        return mse
