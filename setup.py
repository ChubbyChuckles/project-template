from setuptools import setup, find_packages

setup(
    name="project-template",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "sphinx",  # Add for documentation
        "sphinx-rtd-theme",  # If using Read the Docs theme
        "sphinxcontrib-napoleon",  # If using Google/NumPy docstrings
        "pre-commit",  # For pre-commit hooks
    ],
    author="ChubbyChuckles",
    author_email="christian.rickert.1989@gmail.com",
    description="A Python project template with automated setup and documentation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ChubbyChuckles/project-template",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
