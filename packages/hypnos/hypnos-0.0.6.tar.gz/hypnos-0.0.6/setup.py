import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hypnos", 
    version="0.0.6",
    author="Rafal Zajac",
    author_email="rafal@xiontz.com",
    description="Tools related to sleep research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RafalZajac/hypnos",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas>=0.25.1', 
        'numpy>=1.16.5',
        'mne>=0.19.1', 
        'lxml>=4.4.1', 
        'xlrd >= 1.0.0',
        'plotly>=4.2.1',
        'graphviz>=0.10.1',
        'scipy>=1.3.1'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)