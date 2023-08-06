import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="generate_acip_schema", # Replace with your own username
    version="0.0.2",
    author="Joel Crawford",
    author_email="joelrootcrawford@gmail.com",
    description="A small package mapping BDRC schema to ACIP's current Elasticsearch database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joelcrawford/generate-acip-schema",
    packages=setuptools.find_packages(),
    install_requires=[
        "elasticsearch",
        "gspread",
        "oauth2client"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
