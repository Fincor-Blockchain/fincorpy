import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fincorpy", # Replace with your own username
    version="1.0.0",
    author="@fincordev",
    author_email="info@fincor.io",
    description="Package for transaction offline transaction signing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fincor-blockchain/fincorpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)