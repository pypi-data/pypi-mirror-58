import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="melipayamakwebservice",
    version="1.0.1",
    author="Amirhossein Mehrvarzi",
    author_email="melipayamak@gmail.com",
    description="Melipayamak Web Service Wrapper (Soap and Rest)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/melipayamak/melipayamak-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.3',
)