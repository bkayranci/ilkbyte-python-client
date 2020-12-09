import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="ilkbyte",
    version="1.0.1",
    author="Türkalp Burak Kayrancıoğlu",
    author_email="bkayranci@gmail.com",
    description="Ilkbyte python client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bkayranci/ilkbyte-python-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)
