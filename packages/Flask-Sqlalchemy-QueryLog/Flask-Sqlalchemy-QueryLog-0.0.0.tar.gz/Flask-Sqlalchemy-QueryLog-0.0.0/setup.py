import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Flask-Sqlalchemy-QueryLog",
    version="0.0.0",
    author="spyc",
    author_email="unknown@gmail.com",
    description="A personal package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=['flask_sqlalchemy_querylog'],
    license='MIT',
    install_requires=['Flask', 'Flask-Sqlalchemy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
