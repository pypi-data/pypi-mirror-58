import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysinewave",
    version="0.0.1",
    author="David Davini",
    author_email="daviddavini@ucla.com",
    description="Simple and lightweight pakage to generate and play (in real time) sine waves that can make smooth, continuous transitions in pitch and volume",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daviddavini/continuous-sine-wave",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)