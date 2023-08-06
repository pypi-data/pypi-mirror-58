import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tl100", # Replace with your own username
    version="0.0.2",
    author="AZ",
    author_email="adrian.zandberg@gmail.com",
    description="Beurer TL100",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/azac/tl100",
    packages=setuptools.find_packages(),
    install_requires=[
        'pexpect'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: Public Domain",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=2.7',
)