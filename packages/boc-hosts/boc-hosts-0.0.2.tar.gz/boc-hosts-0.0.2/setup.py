import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="boc-hosts",  # Replace with your own username
    version="0.0.2",
    author="Wassim Akachi",
    author_email="wassim@bitofcode.com",
    description="A tool to manage the hosts file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bitofcode/py-boc-hosts",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
