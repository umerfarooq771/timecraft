from setuptools import setup, find_packages

setup(
    name="TIMECRAFTPRO",
    version="0.1.0",
    long_description="Time series data processing and analysis toolkit.",
    author="Muhammad Umer",
    author_email="umerdiwan3@gmail.com",
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
