import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="confluence-cloud-python", # Replace with your own username
    version="1.1.0",
    author="Ashwani Sharma",
    author_email="er.ashwani.it@gmail.com",
    description="This package will provide access to Atlassian Confluence REST APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erashwani",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
