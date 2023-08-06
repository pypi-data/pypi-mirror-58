import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wordoftheday",
    version="0.0.1",
    author="Patrick C",
    author_email="52078333+patrickc-dev@users.noreply.github.com",
    description="get the word of the day from various sources",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patrickc-dev/wordoftheday",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
    python_requires='>=3.6',
)