from setuptools import setup, find_packages

setup(
    name="project-template",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
    ],
    author="ChubbyChuckles",
    author_email="christian.rickert.1989@gmail.com",
    description="TODO Add Description",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ChubbyChuckles/project-template",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
