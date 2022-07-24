# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Path setup --------------------------------------------------------------
# Porque no encuentra mi directorio donde tengo el código
import os, sys, django

sys.path.insert(0, os.path.join(os.path.abspath('.'), '../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'RebuildOfGGHYN.settings'
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RebuildOfGGHYN.settings')
django.setup()


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Rebuild of GGHYN'
copyright = '2022, Roberto Beneitez Vaquero'
author = 'Roberto Beneitez Vaquero'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    # 'rhino.frontend.sphinx',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
