# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "APS Bluesky Training"
copyright = "2024, APS BCDA"
author = "APS BCDA"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = """
    IPython.sphinxext.ipython_console_highlighting
    IPython.sphinxext.ipython_directive
    sphinx.ext.autodoc
    sphinx.ext.autosummary
    sphinx.ext.coverage
    sphinx.ext.githubpages
    sphinx.ext.inheritance_diagram
    sphinx.ext.mathjax
    sphinx.ext.todo
    sphinx.ext.viewcode
    nbsphinx
    myst_parser
    sphinx_design
""".split()
extensions.append("sphinx_tabs.tabs")  # issue #129: this must be last
myst_enable_extensions = ["colon_fence"]

templates_path = ["_templates"]
source_suffix = ".rst .md".split()
exclude_patterns = ["**.ipynb_checkpoints"]

today_fmt = "%Y-%m-%d %H:%M"

# Ignore errors in notebooks while documenting them
nbsphinx_allow_errors = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]
html_theme = "pydata_sphinx_theme"
html_title = project

autodoc_mock_imports = """
    bluesky
    dask
    databroker
    databroker_pack
    epics
    h5py
    intake
    numpy
    openpyxl
    ophyd
    pandas
    pint
    psutil
    pyRestTable
    pysumreg
    spec2nexus
    xarray
""".split()
