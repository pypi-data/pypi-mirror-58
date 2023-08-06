import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CandleView",
    version="0.0.2",
    author="Krzysztof Mizgała",
    author_email="KMChris007@gmail.com",
    description="Candle chart and other stuff",
    url="https://github.com/KMChris",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
