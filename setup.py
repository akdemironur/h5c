from setuptools import setup, find_packages

setup(
    name="h5c",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "h5py",
    ],
    entry_points={
        "console_scripts": [
            "h5c = h5c.__main__:main",
        ],
    },
    author="Onur Akdemir",
    author_email="onur.akdemir@icloud.com",
    description="A command line tool for viewing and updating HDF5 attributes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/akdemironur/h5c",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
