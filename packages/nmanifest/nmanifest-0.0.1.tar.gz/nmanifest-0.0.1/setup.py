import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nmanifest",
    version="0.0.1",
    author="Steffen Vinther Sørensen",
    author_email="svs@logiva.dk",
    description="Generate dynamic number of manifest repetitions using minimum configuration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/logiva/nmanifest",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
