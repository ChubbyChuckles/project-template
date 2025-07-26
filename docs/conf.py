import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

extensions = [
    "sphinx.ext.autodoc",  # For auto-generating docs from docstrings
    "sphinx.ext.napoleon",  # For Google-style docstrings
    "sphinx.ext.viewcode",  # For source code links
]
html_theme = "sphinx_rtd_theme"
# Point to project root for categorical_trading/

# -- Project information -----------------------------------------------------
project = "Categorical Trading"
copyright = "2025, ChubbyChuckles"
author = "ChubbyChuckles"
release = "0.1.0"
