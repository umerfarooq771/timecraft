from setuptools import setup, find_packages

setup(
    name="timecraft",
    version="0.1.0",
    description="Automated feature engineering for time series data",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/umerfarooq771/timecraft",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
