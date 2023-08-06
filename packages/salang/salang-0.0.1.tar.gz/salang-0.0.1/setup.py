import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="salang",
    version="0.0.1",
    author="Samlet Wu",
    author_email="xiaofei.wu@gmail.com",
    description="A langpack package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samlet/salang",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

