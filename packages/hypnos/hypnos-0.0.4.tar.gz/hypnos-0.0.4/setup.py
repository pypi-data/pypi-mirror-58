import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hypnos", 
    version="0.0.4",
    author="Rafal Zajac",
    author_email="rafal@xiontz.com",
    description="Tools related to sleep research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RafalZajac/hypnos",
    packages=setuptools.find_packages(),
    install_requires=['pandas>=0.25.1', 'mne>=0.19.1'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)