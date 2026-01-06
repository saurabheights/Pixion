from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))


project = "Pixion"
copyright = "2025, Saurabh Khanduja"
author = "Saurabh Khanduja"
release = "0.1.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  #  "sphinx.ext.autodoc",   Import code & docstrings
    "sphinx.ext.napoleon",  # Google / NumPy style docstrings
  #  "sphinx.ext.autosummary",   Auto-generate API summaries
    "sphinx.ext.viewcode",  # Add links to source code
    "autoapi.extension",
]
# autosummary_generate = True

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

# Theme overrides
html_css_files = ['css/furo_override.css']

autoapi_type = "python"

# Point to your source directories
autoapi_dirs = [
    "../../pixion",
]

# Keep generated files (useful while learning)
autoapi_keep_files = True

autoapi_generate_package_index = False


# What AutoAPI should include
autoapi_options = [
    "members",
    "undoc-members",
    "show-module-summary",
    "show-inheritance",
]

