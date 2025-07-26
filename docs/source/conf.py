import os
import sys

# Add project root to sys.path (adjust path to point to Categorical Trading)
sys.path.insert(0, os.path.abspath("../.."))

# Project information
project = "Categorical Trading"
copyright = "2025, Chuck"
author = "Chuck"
release = "0.1"

# General configuration
extensions = [
    "sphinx.ext.autodoc",  # For auto-generating documentation from docstrings
    "sphinx.ext.napoleon",  # For Google-style docstrings
    "sphinx.ext.viewcode",  # For linking to source code
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# HTML output options
html_theme = "alabaster"
html_static_path = ["_static"]

# Autodoc settings
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}
autodoc_typehints = "description"  # Include type hints in descriptions
napoleon_google_docstring = True  # Enable Google-style docstring parsing
