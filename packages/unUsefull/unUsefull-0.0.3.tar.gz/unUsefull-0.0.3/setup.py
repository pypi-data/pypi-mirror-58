import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unUsefull",
    version="0.0.3",
    author="outforpublic",
    author_email="fredboi207@gmail.com.com",
    description="Useless tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/outforpublic/uTools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.5',
)