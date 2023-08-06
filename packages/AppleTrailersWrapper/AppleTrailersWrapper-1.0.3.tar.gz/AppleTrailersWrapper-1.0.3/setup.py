import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AppleTrailersWrapper",
    version="1.0.3",
    author="Puyodead1",
    author_email="puyodead@protonmail.com",
    description="Simple package that wraps Apple Trailers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Puyodead1/AppleTrailersWrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta"
    ],
    python_requires='>=3',
)
