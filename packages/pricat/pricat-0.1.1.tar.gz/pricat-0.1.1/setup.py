import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pricat",
    version="0.1.1",
    author="Matteo Redaelli",
    author_email="matteo.redaelli@gmail.com",
    description="pricat is a simple utility for parsing tire lists in the PRICAT format files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/matteo.redaelli/pricat.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=['pandas'],
    python_requires='>=3.5',
)
