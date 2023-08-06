import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hunterk", 
    version="0.0.1",
    author="Hunter Kempf",
    author_email="hunterkempf@gmail.com",
    description="Package to get Content data from wikipedia and IMDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hunterkempf/ContentData",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
