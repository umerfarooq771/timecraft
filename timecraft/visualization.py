import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def plot_time_series(df, title="Time Series Data"):
        """
        Plot time series data.

        Args:
            df (pd.DataFrame): Input time series data.
            title (str): Plot title.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(df)
        plt.title(title)
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.grid(True)
        plt.show()

    @staticmethod
    def plot_features(df, title="Generated Features"):
        """
        Plot generated features.

        Args:
            df (pd.DataFrame): Input features dataframe.
            title (str): Plot title.
        """
        plt.figure(figsize=(12, 6))
        for column in df.columns:
            plt.plot(df.index, df[column], label=column)
        plt.title(title)
        plt.xlabel('Time')
        plt.ylabel('Feature Value')
        plt.legend()
        plt.grid(True)
        plt.show()
