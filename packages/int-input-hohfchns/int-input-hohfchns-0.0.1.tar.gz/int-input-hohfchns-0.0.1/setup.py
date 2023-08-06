import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="int-input-hohfchns", # Replace with your own username
    version="0.0.1",
    author="hohfchns",
    author_email="hohfchns@example.com",
    description="A simple function to get only integer input",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hohfchns/My-Python-Modules/blob/master/int_input.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)