import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mvstd",
    version="1.0.1",
    author="Jon Craton",
    author_email="jon@joncraton.com",
    description="Rename files using a standard format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jncraton/mvstd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'mvstd=mvstd:main',
        ],
    },
    install_requires=[
    ],
)